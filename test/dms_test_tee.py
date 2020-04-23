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

        retval = dms_tee_demuxer_new('demuxer')
        if retval != 'DSL_RESULT_SUCCESS':
            break
            
        retval = dms_tee_splitter_new('splitter')
        if retval != 'DSL_RESULT_SUCCESS':
            break

        # done - break out of while
        break

    # Print out the final result
    print(retval)

    dms_component_delete_all()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
