################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################
#!/usr/bin/env python

import sys
sys.path.insert(0, '../')
from dms_client import *

tracker_config_file = './test/configs/iou_config.txt'

def main(args):

    dms_pipeline_delete_all()
    dms_component_delete_all()

    while True:
    
        print(dms_version_get())

        retval = dms_tracker_ktl_new('ktl-tracker', 480, 272)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_tracker_iou_new('iou-tracker', tracker_config_file, 480, 272)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval, max_width, max_height = dms_tracker_max_dimensions_get('ktl-tracker')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('max_width =',max_width, 'max_height =',max_height)

        retval = dms_tracker_max_dimensions_set('ktl-tracker', 400, 250)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # done - break out of while
        break

    # Print out the final result
    print(retval)

    dms_component_delete_all()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
