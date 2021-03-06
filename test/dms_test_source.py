################################################################################
# The MIT License
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
################################################################################
#!/usr/bin/env python

import sys
sys.path.insert(0, '../')

from dms_client import *

uri_file_h264 = "./test/streams/sample_1080p_h264.mp4"
uri_file_h265 = "./test/streams/sample_1080p_h265.mp4"

# RTSP Source URI
rtsp_uri = 'rtsp://raspberrypi.local:8554/'

def main(args):

    retval = dms_target_new('nano1', 'http://127.0.0.1:8080')
    if retval == 'DSL_RESULT_SUCCESS':
    
        while True:
            print(dms_target_version_get('nano1'))

            # Ensure that we're starting with empty containers
            dms_pipeline_delete_all('nano1')
            dms_component_delete_all('nano1')

            retval = dms_source_csi_new('nano1', 'csi-source', 1280, 720, 30, 1)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_source_usb_new('nano1', 'usb-source', 1280, 720, 30, 1)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_source_uri_new('nano1', 'uri-source', uri_file_h264, False, 0, 0, 0)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_source_rtsp_new('nano1', 'rtsp-source', rtsp_uri, DMS_RTP_ALL, DMS_CUDADEC_MEMTYPE_DEVICE, False, 1)
            if retval != 'DSL_RESULT_SUCCESS':
                break
                
            retval, width, height = dms_source_dimensions_get('nano1', 'csi-source')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, fps_n, fps_d = dms_source_frame_rate_get('nano1', 'csi-source')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, uri = dms_source_decode_uri_get('nano1', 'uri-source')
            if retval != 'DSL_RESULT_SUCCESS':
                break

    #        retval = dms_source_decode_uri_set('uri-source', uri_file_h265)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, uri = dms_source_decode_uri_get('nano1', 'uri-source')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            num = dms_source_num_in_use_get('nano1')
            num = dms_source_num_in_use_max_get('nano1')
            
            success = dms_source_num_in_use_max_set('nano1', 6)
            
            # done - break out of while
            break

        # Delete all components created
        dms_component_delete_all('nano1')

    # Print out the final result
    print(retval)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
