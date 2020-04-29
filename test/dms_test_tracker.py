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

tracker_config_file = './test/configs/iou_config.txt'

def main(args):

    retval = dms_target_new('nano1', 'http://127.0.0.1:8080')
    if retval == 'DSL_RESULT_SUCCESS':
    
        while True:
            print(dms_target_version_get('nano1'))

            # Ensure that we're starting with empty containers
            dms_pipeline_delete_all('nano1')
            dms_component_delete_all('nano1')

            retval = dms_tracker_ktl_new('nano1', 'ktl-tracker', 480, 272)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_tracker_iou_new('nano1', 'iou-tracker', tracker_config_file, 480, 272)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval, max_width, max_height = dms_tracker_max_dimensions_get('nano1', 'ktl-tracker')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            print('max_width =',max_width, 'max_height =',max_height)

            retval = dms_tracker_max_dimensions_set('nano1', 'ktl-tracker', 400, 250)
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
