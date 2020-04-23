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
    ## /branch/component/add
    ## dsl_branch_component_add
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def default(self):
        try:
            params = cherrypy.request.json
            retval = dsl_branch_component_add(params["branch"], params["component"])
            result = { "service": "dsl_branch_component_add", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_branch_component_add", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

    ##
    ## /branch/component/add/many
    ## dsl_branch_component_add_many
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def many(self):
        try:
            params = cherrypy.request.json
            print(params["components"])
            retval = dsl_branch_component_add_many(params["branch"], params["components"])
            result = { "service": "dsl_branch_component_add_many", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_branch_component_add_many", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

class component(object):

    def __init__(self):
        print('init branch')
        self.add = add()

class delete(object):

    ##
    ## /branch/delete
    ## dsl_branch_delete
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def default(self):
        try:
            params = cherrypy.request.json
            retval = dsl_branch_delete(params["name"])
            result = { "service": "dsl_branch_delete", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_branch_delete", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

    ##
    ## /branch/delete/all
    ## dsl_branch_delete_all
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def all(self):
        try:
            params = cherrypy.request.json
            retval = dsl_branch_delete_all()
            result = { "service": "dsl_branch_delete_all", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_branch_delete_all", "result": { "exception" :  sys.exc_info()[0] } }
        
        return result

class branch(object):        

    def __init__(self):
        print('init branch')
        self.delete = delete()
        self.component = component()

    ##
    ## /branch/new
    ## dsl_branch_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            print(params)
            retval = dsl_branch_new(params["name"])
            print(dsl_return_value_to_string(retval))
            result = { "service": "dsl_branch_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_branch_new", "result": { "exception" :  sys.exc_info()[0] } }
        return result
