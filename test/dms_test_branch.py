################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################
from dms_client import *

def main(args):

    dms_pipeline_delete_all()
    dms_component_delete_all()

    while True:
    
        print(dms_version_get())

        retval = dms_branch_new('branch')
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_tracker_ktl_new('tracker', 480, 272)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # New OSD with clock enabled... using default values.
        retval = dms_osd_new('on-screen-display', True)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        retval = dms_tiler_new('tiler', 1280, 720)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        
        retval = dms_branch_component_add('branch', 'tracker')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        
        retval = dms_branch_component_add_many('branch', 
            ['tiler', 'on-screen-display', None])
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # done - break out of while
        break


    # Print out the final result
    print(retval)

    dms_component_delete_all()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
