################################################################################
#
# Copyright (c) 2019-2020, Robert Howell. All rights reserved.
#
################################################################################
import sys
import cherrypy
from dsl import *

class add(object):

    ##
    ## /pipeline/component/add
    ## dsl_pipeline_component_add
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def default(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_component_add(params["pipeline"], params["component"])
            result = { "service": "dsl_pipeline_component_add", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_component_add", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

    ##
    ## /pipeline/component/add/many
    ## dsl_pipeline_component_add_many
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def many(self):
        try:
            params = cherrypy.request.json
            print(params["components"])
            retval = dsl_pipeline_component_add_many(params["pipeline"], params["components"])
            result = { "service": "dsl_pipeline_component_add_many", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_component_add_many", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

class component(object):

    def __init__(self):
        print('init pipeline')
        self.add = add()

class delete(object):

    ##
    ## /pipeline/delete
    ## dsl_pipeline_delete
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def default(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_delete(params["name"])
            result = { "service": "dsl_pipeline_delete", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_delete", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

    ##
    ## /pipeline/delete/all
    ## dsl_pipeline_delete_all
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def all(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_delete_all()
            result = { "service": "dsl_pipeline_delete_all", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_delete_all", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

class pipeline(object):        

    def __init__(self):
        print('init pipeline')
        self.delete = delete()
        self.component = component()

    ##
    ## /pipeline/new
    ## dsl_pipeline_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            print(params)
            retval = dsl_pipeline_new(params["name"])
            print(dsl_return_value_to_string(retval))
            result = { "service": "dsl_pipeline_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_new", "result": { "exception" :  sys.exc_info()[0] } }
        return result

    ##
    ## /pipeline/play
    ## dsl_pipeline_play
    ##
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    
    def play(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_play(params["name"])
            result = { "service": "dsl_pipeline_play", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_play", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

    ##
    ## /pipeline/pause
    ## dsl_pipeline_pause
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def pause(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_pause(params["name"])
            result = { "service": "dsl_pipeline_pause", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_pause", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

    ##
    ## /pipeline/stop
    ## dsl_pipeline_stop
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def stop(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_stop(params["name"])
            result = { "service": "dsl_pipeline_stop", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_stop", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result
        
