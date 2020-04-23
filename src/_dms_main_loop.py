################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################
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
            result = { 'service': 'dsl_main_loop_run', 
                'result': { 'exception' :  sys.exc_info()[0] } }
        return result

    ## /main_loop/run
    ## dsl_main_loop_quit
    ##

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def quit(self):
        try:
            dsl_main_loop_quit()
            result = { 'service': 'dsl_main_loop_quite', 'result': 'DSL_RESULT_SUCCESS' }
        except:
            result = { 'service': 'dsl_main_loop_run', 
                'result': { 'exception' :  sys.exc_info()[0] } }
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

