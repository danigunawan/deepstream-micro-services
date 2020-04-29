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
            result = { "service": "dsl_branch_component_add", "result": sys.exc_info()[0] }
        
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
            result = { "service": "dsl_branch_component_add_many", "result": sys.exc_info()[0] }
        
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
            result = { "service": "dsl_branch_delete", "result": sys.exc_info()[0] }
        
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
            result = { "service": "dsl_branch_delete_all", "result": sys.exc_info()[0] }
        
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
            result = { "service": "dsl_branch_new", "result": sys.exc_info()[0] }
        return result
