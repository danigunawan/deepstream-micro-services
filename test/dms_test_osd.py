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

        retval = dms_osd_new('on-screen-display', True)
        if retval != 'DSL_RESULT_SUCCESS':
            break
            
        retval = dms_osd_redaction_enabled_set('on-screen-display', True)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        retval, enabled = dms_osd_redaction_enabled_get('on-screen-display')
        if retval != 'DSL_RESULT_SUCCESS':
            break
        print('enabled =', enabled)
            
        retval = dms_osd_redaction_class_add('on-screen-display', 0, 0.0, 0.0, 0.0, 1.0)
        if retval != 'DSL_RESULT_SUCCESS':
            break
        retval = dms_osd_redaction_class_remove('on-screen-display', 0)
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # done - break out of while
        break

    # Print out the final result
    print(retval)

    dms_component_delete_all()

if __name__ == '__main__':
    sys.exit(main(sys.argv))