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
host_uri = 'rjhowell44-desktop.local'

uri_file = "../test/streams/sample_1080p_h264.mp4"

# Filespecs for the Primary GIE
primary_infer_config_file = './test/configs/config_infer_primary_nano.txt'
primary_model_engine_file = './test/models/Primary_Detector_Nano/resnet10.caffemodel_b1_fp16.engine'

def main(args):

    # ensure there is nothing currently running
    dms_main_loop_quit()
    dms_pipeline_delete_all()
    dms_component_delete_all()

    # Since we're not using args, we can Let DSL initialize GST on first call
    while True:
    
        retval = dms_target_new('nano1', 'http://127.0.0.1:8080')
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # New CSI Live Camera Source
        retval = dms_source_csi_new('csi-source', 1280, 720, 30, 1)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # New URI File Source using the filespec defined above
#        retval = dms_source_uri_new('uri-source', uri_file, False, 0, 0, 0)
#        if retval != 'DSL_RESULT_SUCCESS':
#            break

        # New Primary GIE using the filespecs above, with interval and Id
        retval = dms_gie_primary_new('primary-gie', primary_infer_config_file, primary_model_engine_file, 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_tracker_ktl_new('tracker', 480, 272)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # New OSD with clock enabled... using default values.
        retval = dms_osd_new('on-screen-display', True)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retVal = dms_sink_rtsp_new('rtsp-sink', host_uri, 5400, 8554, DMS_CODEC_H264, 4000000, 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_sink_window_new('window-sink', 100, 100, 1280, 720)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_tiler_new('tiler', 1280, 720)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        
        retval = dms_pipeline_new('pipeline')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        
        retval = dms_pipeline_component_add_many('pipeline', 
            ['csi-source', 'primary-gie', 'tracker', 'tiler', 'on-screen-display', 'rtsp-sink', 'window-sink', None])
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_pipeline_play('pipeline')
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_main_loop_run()
        break


    # Print out the final result
    print(retval)

if __name__ == '__main__':
    sys.exit(main(sys.argv))

