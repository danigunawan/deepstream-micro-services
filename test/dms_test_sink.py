################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################
#!/usr/bin/env python

import sys
sys.path.insert(0, '../')
from dms_client import *

# update host URL to 
host_uri = 'username-desktop.local'

def main(args):

    dms_pipeline_delete_all()
    dms_component_delete_all()

    while True:
    
        print(dms_version_get())

        retval = dms_sink_fake_new('fake-sink')
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_sink_overlay_new('overlay-sink', 1, 0, 0, 0, 0, 1280, 720)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_sink_window_new('window-sink', 100, 100, 1280, 720)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_sink_file_new('file-sink', './output.mp4', DMS_CODEC_H265, DMS_CONTAINER_MP4, 2000000, 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_sink_image_new('image-sink', './')
        if retval != 'DSL_RESULT_SUCCESS':
            break
            
        retval = dms_sink_image_frame_capture_enabled_set('image-sink', True)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        retval, enabled = dms_sink_image_frame_capture_enabled_get('image-sink')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('enabled =', enabled)
            
        retval = dms_sink_image_frame_capture_interval_set('image-sink', 30)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        retval, interval = dms_sink_image_frame_capture_interval_get('image-sink')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('interval =', interval)
            
        retval = dms_sink_image_object_capture_enabled_set('image-sink', True)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        retval, enabled = dms_sink_image_object_capture_enabled_get('image-sink')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('enabled =', enabled)

        retval = dms_sink_image_object_capture_class_add('image-sink', 0, False, 10)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        retval = dms_sink_image_object_capture_class_remove('image-sink', 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retVal = dms_sink_rtsp_new('rtsp-sink', host_uri, 5400, 8554, DMS_CODEC_H264, 4000000, 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # done - break out of while
        break

    # Print out the final result
    print(retval)

    dms_component_delete_all()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
