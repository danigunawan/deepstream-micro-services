################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################


import sys
import cherrypy
from dsl import *

class demuxer(object):

    ## tee/demuxer/new
    ## dsl_tee_demuxer_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_tee_demuxer_new(params["name"])
            result = { "service": "dsl_tee_demuxer_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_tee_demuxer_new", "result": { "exception" : formatEx() } }
        return result

class splitter(object):

    ## tee/splitter/new
    ## dsl_tee_splitter_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_tee_splitter_new(params["name"])
            result = { "service": "dsl_tee_splitter_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_tee_splitter_new", "result": { "exception" : formatEx() } }
        return result

class tee(object):

    def __init__(self):
        self.demuxer = demuxer()
        self.splitter = splitter()
    