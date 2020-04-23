################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################

import cherrypy
from dsl import *

class ktl(object):

    ## /tracker/ktl/new
    ## dsl_tracker_ktl_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_tracker_ktl_new(params["name"], params["max_width"], params["max_height"])
            result = { "service": "dsl_tracker_ktl_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_tracker_ktl_new", "result": { "exception" : formatEx() } }
        return result

class iou(object):

    ## /tracker/iou/new
    ## dsl_tracker_iou_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_tracker_iou_new(params["name"], params['config_file'], params["max_width"], params["max_height"])
            result = { "service": "dsl_tracker_iou_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_tracker_iou_new", "result": { "exception" : formatEx() } }
        return result

class max_dimensions(object):

    ##
    ## /tracker/max_dimensions/get
    ## dsl_tracker_max_dimensions_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, max_width, max_height = dsl_tracker_max_dimensions_get(params['name'])
            result = { 'service': 'dsl_tracker_max_dimensions_get', 
                'result': dsl_return_value_to_string(retval), 'max_width': max_width, 'max_height': max_height }
        except:
            result = { 'service': 'dsl_tracker_max_dimensions_get', 
                'result': { 'exception' :  sys.exc_info()[0] }, 'max_width': 0, 'max_height': 0 }
        return result

    ##
    ## /tracker/max_dimensions/set
    ## dsl_tracker_max_dimensions_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_tracker_max_dimensions_set(params['name'], params['max_width'], params['max_height'])
            result = { 'service': 'dsl_tracker_max_dimensions_get', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_tracker_max_dimensions_get', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

class tracker(object):
    def __init__(self):
        self.ktl = ktl()
        self.iou = iou()
        self.max_dimensions = max_dimensions()

