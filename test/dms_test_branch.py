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
            print(dms_target_version_get('nano1'))

            # Ensure that we're starting with empty containers
            dms_pipeline_delete_all('nano1')
            dms_component_delete_all('nano1')

            retval = dms_branch_new('nano1', 'branch')
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_tracker_ktl_new('nano1', 'tracker', 480, 272)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            # New OSD with clock enabled... using default values.
            retval = dms_osd_new('nano1', 'on-screen-display', True)
            if retval != 'DSL_RESULT_SUCCESS':
                break

            retval = dms_tiler_new('nano1', 'tiler', 1280, 720)
            if retval != 'DSL_RESULT_SUCCESS':
                break
            
            retval = dms_branch_component_add('nano1', 'branch', 'tracker')
            if retval != 'DSL_RESULT_SUCCESS':
                break
            
            retval = dms_branch_component_add_many('nano1', 'branch', 
                ['tiler', 'on-screen-display', None])
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
