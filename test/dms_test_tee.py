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

def main(args):

    retval = dms_target_new('nano1', 'http://127.0.0.1:8080')
    if retval == 'DSL_RESULT_SUCCESS':
    
        while True:
            print(dms_target_version_get('nano1'))

            # Ensure that we're starting with empty containers
            dms_pipeline_delete_all('nano1')
            dms_component_delete_all('nano1')

            retval = dms_tee_demuxer_new('nano1', 'demuxer')
            if retval != 'DSL_RESULT_SUCCESS':
                break
                
            retval = dms_tee_splitter_new('nano1', 'splitter')
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
