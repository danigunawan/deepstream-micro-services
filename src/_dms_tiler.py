################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################


import sys
import cherrypy
from dsl import *

class tiler(object):

    ## /tiler/new
    ## dsl_tiler_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_tiler_new(params["name"], params["width"], params["height"])
            result = { "service": "dsl_tiler_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_tiler_new", "result": { "exception" : formatEx() } }
        return result

