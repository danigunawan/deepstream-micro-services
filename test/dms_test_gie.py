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
import os
from dms_client import *

# These PATHS are from DMS server perspective

# Filespecs for the Primary GIE
primary_config_file = './test/configs/config_infer_primary_nano.txt'
primary_model_file = './test/models/Primary_Detector_Nano/resnet10.caffemodel_b1_fp16.engine'

# Filespecs for the Secondary GIE
secondary_config_file = './test/configs/config_infer_secondary_carcolor_nano.txt'
secondary_model_file = './test/models/Secondary_CarColor/resnet18.caffemodel_b2_fp16.engine'

new_config_file = './test/configs/config_infer_secondary_carmake_nano.txt'
new_model_file = './test/models/Secondary_CarMake/resnet18.caffemodel_b2_fp16.engine'

# These PATHS are from test case perspective

upload_config_file = os.path.normpath('./configs/config_infer_secondary_carmake_nano.txt')

upload_model_file = os.path.normpath('./models/Secondary_CarMake/resnet18.caffemodel')


def main(args):

    retval = dms_target_new('nano1', 'http://127.0.0.1:8080')
    if retval == 'DSL_RESULT_SUCCESS':
    
        while True:
            print(dms_target_version_get('nano1'))

            # Ensure that we're starting with empty containers
            dms_pipeline_delete_all('nano1')
            dms_component_delete_all('nano1')

            retval = dms_gie_infer_config_file_upload('nano1', upload_config_file)
            if retval != 'DSL_RESULT_SUCCESS':
                break
            retval = dms_gie_model_engine_file_upload('nano1', upload_model_file)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_gie_primary_new('nano1', 'primary-gie', primary_config_file, primary_model_file, 0)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_gie_secondary_new('nano1', 'secondary-gie', secondary_config_file, secondary_model_file, 'primary-gie', 0)
            if retval != 'DSL_RESULT_SUCCESS':
                break
                
            retval, file = dms_gie_infer_config_file_get('nano1', 'secondary-gie')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            print('secondary-config-file =', file)

            retval = dms_gie_infer_config_file_set('nano1', 'secondary-gie', new_config_file)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, file = dms_gie_model_engine_file_get('nano1', 'secondary-gie')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            print('secondary-model-file =', file)

            retval = dms_gie_model_engine_file_set('nano1', 'secondary-gie', new_model_file)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            # done - break out of while
            break

        # Delete all components created
        dms_component_delete_all('nano1')

    # Print out the final result
    print(retval)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
