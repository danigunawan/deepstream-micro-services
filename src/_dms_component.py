################################################################################
#
# Copyright (c) 2019-2020, Robert Howell. All rights reserved.
#
################################################################################
import sys
import cherrypy
from dsl import *

class component(object):        

    def __init__(self):
        print('init component')
        self.delete = delete()

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
            retval = dsl_component_delete(params["name"])
            result = { "service": "dsl_pipeline_delete", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_delete", "result": { "exception" :  sys.exc_info()[0] } }
        return result

    ##
    ## /pipeline/delete/all
    ## dsl_component_delete_all
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def all(self):
        try:
            params = cherrypy.request.json
            retval = dsl_component_delete_all()
            print(retval)
            result = { "service": "dsl_pipeline_delete_all", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_pipeline_delete_all", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result
