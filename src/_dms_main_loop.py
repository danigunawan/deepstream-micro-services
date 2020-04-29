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
import threading
import cherrypy
from dsl import *

class main_loop(object):

    ## /main_loop/run
    ## dsl_main_loop_quit
    ##

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def run(self):
        try:
            dsl_main_loop = threading.Thread(target=thread_loop)
            dsl_main_loop.start()
            result = { 'service': 'dsl_main_loop_run', 'result': 'DSL_RESULT_SUCCESS' }
        except:
            result = { 'service': 'dsl_main_loop_run', 'result': sys.exc_info()[0] }
        return result

    ## /main_loop/run
    ## dsl_main_loop_quit
    ##

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def quit(self):
        try:
            dsl_main_loop_quit()
            result = { 'service': 'dsl_main_loop_quit', 'result': 'DSL_RESULT_SUCCESS' }
        except:
            result = { 'service': 'dsl_main_loop_quite', 'result': sys.exc_info()[0] }
        return result

##
## Thread to block on the DSL/GStreamer Main Loop
def thread_loop():
    try:
        print('entering DSL Main Loop')
        dsl_main_loop_run()
        print('exiting DSL Main Loop')
    except:
        pass

