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

def main(args):

    retval = dms_target_new('nano1', 'http://127.0.0.1:8080')

    if retval == 'DSL_RESULT_SUCCESS':
        while True:

            # Ensure that we're starting with empty containers
            dms_pipeline_delete_all('nano1')
            dms_component_delete_all('nano1')

            retval = dms_pipeline_new('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break
                
            retval, state = dms_pipeline_state_get('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_source_csi_new('nano1', 'csi-source', 1280, 720, 30, 1)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_tiler_new('nano1', 'tiler', 1280, 720)
            if retval != 'DSL_RESULT_SUCCESS':
                break
            
            retval = dms_sink_fake_new('nano1', 'fake-sink')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            
            retval = dms_pipeline_component_add('nano1', 'pipeline', 'csi-source')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            
            retval = dms_pipeline_component_add_many('nano1', 'pipeline', 
                ['tiler', 'fake-sink', None])
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_pipeline_streammux_dimensions_set('nano1', 'pipeline', 1280, 720)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, width, height = dms_pipeline_streammux_dimensions_get('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_pipeline_streammux_batch_properties_set('nano1', 'pipeline', 2, 50000)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, batch_size, batch_timeout = dms_pipeline_streammux_batch_properties_get('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_pipeline_play('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, state = dms_pipeline_state_get('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, is_live = dms_pipeline_is_live('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_pipeline_streammux_padding_set('nano1', 'pipeline', True)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, enabled = dms_pipeline_streammux_padding_get('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            #retval = dms_pipeline_pause('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_pipeline_stop('nano1', 'pipeline')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            # done - break out of while
            break

        # Delete the pipeline and all components created
        dms_pipeline_delete_all('nano1')
        dms_component_delete_all('nano1')


    # Print out the final result
    print(retval)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
