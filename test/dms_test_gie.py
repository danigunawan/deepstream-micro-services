################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
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

    dms_pipeline_delete_all()
    dms_component_delete_all()

    while True:
    
        print(dms_version_get())

        retval = dms_gie_infer_config_file_upload(upload_config_file)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        retval = dms_gie_model_engine_file_upload(upload_model_file)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_gie_primary_new('primary-gie', primary_config_file, primary_model_file, 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_gie_secondary_new('secondary-gie', secondary_config_file, secondary_model_file, 'primary-gie', 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break
            
        retval, file = dms_gie_infer_config_file_get('secondary-gie')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('secondary-config-file =', file)

        retval = dms_gie_infer_config_file_set('secondary-gie', new_config_file)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval, file = dms_gie_model_engine_file_get('secondary-gie')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('secondary-model-file =', file)

        retval = dms_gie_model_engine_file_set('secondary-gie', new_model_file)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # done - break out of while
        break

    # Print out the final result
    print(retval)

    dms_component_delete_all()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
