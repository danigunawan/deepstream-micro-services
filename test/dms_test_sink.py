################################################################################
# The MIT License
#
# Copyright (c) 2019-2020, Robert Howell. All rights reserved.
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

# update host URL to 
host_uri = 'username-desktop.local'

def main(args):

    retval = dms_target_new('nano1', 'http://127.0.0.1:8080')
    if retval == 'DSL_RESULT_SUCCESS':
    
        while True:
            print(dms_target_version_get('nano1'))

            # Ensure that we're starting with empty containers
            dms_pipeline_delete_all('nano1')
            dms_component_delete_all('nano1')

            retval = dms_sink_fake_new('nano1', 'fake-sink')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_sink_overlay_new('nano1', 'overlay-sink', 1, 0, 0, 0, 0, 1280, 720)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_sink_window_new('nano1', 'window-sink', 100, 100, 1280, 720)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_sink_file_new('nano1', 'file-sink', './output.mp4', DMS_CODEC_H265, DMS_CONTAINER_MP4, 2000000, 0)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_sink_image_new('nano1', 'image-sink', './')
            if retval != 'DSL_RESULT_SUCCESS':
                break
                
            retval = dms_sink_image_frame_capture_enabled_set('nano1', 'image-sink', True)
            if retval != 'DSL_RESULT_SUCCESS':
                break
            retval, enabled = dms_sink_image_frame_capture_enabled_get('nano1', 'image-sink')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            print('enabled =', enabled)
                
            retval = dms_sink_image_frame_capture_interval_set('nano1', 'image-sink', 30)
            if retval != 'DSL_RESULT_SUCCESS':
                break
            retval, interval = dms_sink_image_frame_capture_interval_get('nano1', 'image-sink')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            print('interval =', interval)
                
            retval = dms_sink_image_object_capture_enabled_set('nano1', 'image-sink', True)
            if retval != 'DSL_RESULT_SUCCESS':
                break
            retval, enabled = dms_sink_image_object_capture_enabled_get('nano1', 'image-sink')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            print('enabled =', enabled)

            retval = dms_sink_image_object_capture_class_add('nano1', 'image-sink', 0, False, 10)
            if retval != 'DSL_RESULT_SUCCESS':
                break
            retval = dms_sink_image_object_capture_class_remove('nano1', 'image-sink', 0)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retVal = dms_sink_rtsp_new('nano1', 'rtsp-sink', host_uri, 5400, 8554, DMS_CODEC_H264, 4000000, 0)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            num = dms_sink_num_in_use_get('nano1')
            num = dms_sink_num_in_use_max_get('nano1')
            
            success = dms_sink_num_in_use_max_set('nano1', 6)

            # done - break out of while
            break

        # Delete all components created
        dms_component_delete_all('nano1')

    # Print out the final result
    print(retval)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
