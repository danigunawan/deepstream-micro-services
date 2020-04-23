################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################

from dms_client import *

uri_file_h264 = "../test/streams/sample_1080p_h264.mp4"
uri_file_h265 = "../test/streams/sample_1080p_h265.mp4"

# RTSP Source URI
rtsp_uri = 'rtsp://raspberrypi.local:8554/'

def main(args):

    dms_pipeline_delete_all()
    dms_component_delete_all()

    # Since we're not using args, we can Let DSL initialize GST on first call
    while True:
    
        print(dms_version_get())

        # New CSI Live Camera Source
        retval = dms_source_csi_new('csi-source', 1280, 720, 30, 1)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # New USB Live Camera Source
        retval = dms_source_usb_new('usb-source', 1280, 720, 30, 1)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # New URI File Source using the filespec defined above
        retval = dms_source_uri_new('uri-source', uri_file_h264, False, 0, 0, 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_source_rtsp_new('rtsp-source', rtsp_uri, DMS_RTP_ALL, DMS_CUDADEC_MEMTYPE_DEVICE, False, 1)
        if retval != 'DSL_RESULT_SUCCESS':
            break
            
        retval, width, height = dms_source_dimensions_get('csi-source')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('width =',width, 'height =',height)

        retval, fps_n, fps_d = dms_source_frame_rate_get('csi-source')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('fps_n =', fps_n, 'fps_d =', fps_d)

        retval, uri = dms_source_decode_uri_get('uri-source')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('uir =', uri)

#        retval = dms_source_decode_uri_set('uri-source', uri_file_h265)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval, uri = dms_source_decode_uri_get('uri-source')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('uir =', uri)

        # done - break out of while
        break

    # Print out the final result
    print(retval)

    dms_pipeline_delete_all()
    dms_component_delete_all()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
