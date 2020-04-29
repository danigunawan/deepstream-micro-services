################################################################################
# The MIT License
#
# Copyright (c) 2019-2020, Robert Howell. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the 'Software'),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
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

##
## /pipeline/...
## dsl_pipeline_...
##
class pipeline(object):        

    def __init__(self):
        self.delete = delete()
        self.component = component()
        self.streammux = streammux()

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
            retval = dsl_pipeline_new(params['name'])
            result = { 'service': 'dsl_pipeline_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_new', 'result': sys.exc_info()[0] }
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
            retval = dsl_pipeline_play(params['name'])
            result = { 'service': 'dsl_pipeline_play', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_play', 'result': sys.exc_info()[0] }
        
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
            retval = dsl_pipeline_pause(params['name'])
            result = { 'service': 'dsl_pipeline_pause', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_pause', 'result': sys.exc_info()[0] }
        
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
            retval = dsl_pipeline_stop(params['name'])
            result = { 'service': 'dsl_pipeline_stop', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_stop', 'result': sys.exc_info()[0] }
        
        return result
        
    ##
    ## /pipeline/state_get
    ## dsl_pipeline_state_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def state_get(self):
        try:
            params = cherrypy.request.json
            retval, state = dsl_pipeline_state_get(params['name'])
            result = { 'service': 'dsl_pipeline_state_get', 
                'result': dsl_return_value_to_string(retval), 'state':  dsl_state_value_to_string(state)}
        except:
            result = { 'service': 'dsl_pipeline_state_get', 'result': sys.exc_info()[0] }
        
        return result
        
    ##
    ## /pipeline/is_live
    ## dsl_pipeline_is_live
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def is_live(self):
        try:
            params = cherrypy.request.json
            retval, is_live = dsl_pipeline_is_live(params['name'])
            result = { 'service': 'dsl_pipeline_is_live', 
                'result': dsl_return_value_to_string(retval), 'is_live':  is_live}
        except:
            result = { 'service': 'dsl_pipeline_is_live', 
                'result': sys.exc_info()[0], 'is_live': 0 }
        
        return result
        
##
## /pipeline/delete/...
## dsl_pipeline_delete...
##
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
            retval = dsl_pipeline_delete(params['name'])
            result = { 'service': 'dsl_pipeline_delete', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_delete', 'result': sys.exc_info()[0] }
        
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
            result = { 'service': 'dsl_pipeline_delete_all', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_delete_all', 'result': sys.exc_info()[0] }
        return result

##
## /pipeline/component/...
## dsl_pipeline_component...
##
class component(object):

    def __init__(self):
        self.add = add()

##
## /pipeline/component/add/...
## dsl_pipeline_component_add...
##
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
            retval = dsl_pipeline_component_add(params['pipeline'], params['component'])
            result = { 'service': 'dsl_pipeline_component_add', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_component_add', 'result': sys.exc_info()[0] }
        
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
            retval = dsl_pipeline_component_add_many(params['pipeline'], params['components'])
            result = { 'service': 'dsl_pipeline_component_add_many', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_component_add_many', 'result': sys.exc_info()[0] }
        
        return result

##
## /pipeline/streammux/...
## dsl_pipeline_streammux...
##
class streammux(object):

    def __init__(self):
        self.batch_properties = batch_properties()
        self.dimensions = dimensions()
        self.padding = padding()

##
## /pipeline/streammux/batch_properties/...
## dsl_pipeline_streammux_batch_properties...
##
class batch_properties(object):

    ##
    ## /pipeline/streammux/batch_properties/get
    ## dsl_pipeline_streammux_batch_properties_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, batch_size, batch_timeout = dsl_pipeline_streammux_batch_properties_get(params['name'])
            result = { 'service': 'dsl_pipeline_streammux_batch_properties_get', 
                'result': dsl_return_value_to_string(retval), 'batch_size': batch_size, 'batch_timeout': batch_timeout }
        except:
            result = { 'service': 'dsl_pipeline_streammux_batch_properties_get', 
                'result': sys.exc_info()[0], 'batch_size': 0, 'batch_timeout': 0 }
        return result

    ##
    ## /pipeline/streammux/batch_properties/set
    ## dsl_pipeline_streammux_batch_properties_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_streammux_batch_properties_set(params['name'], params['batch_size'], params['batch_timeout'])
            result = { 'service': 'dsl_pipeline_streammux_batch_properties_set', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_streammux_batch_properties_set', 'result': sys.exc_info()[0] }
        return result

##
## /pipeline/streammux/dimensions/...
## dsl_pipeline_streammux_dimensions...
##
class dimensions(object):

    ##
    ## /pipeline/streammux/dimensions/get
    ## dsl_pipeline_streammux_dimensions_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, width, height = dsl_pipeline_streammux_dimensions_get(params['name'])
            result = { 'service': 'dsl_pipeline_streammux_dimensions_get', 
                'result': dsl_return_value_to_string(retval), 'width': width, 'height': height }
        except:
            result = { 'service': 'dsl_pipeline_streammux_dimensions_get', 
                'result': sys.exc_info()[0], 'width': 0, 'height': 0 }
        return result

    ##
    ## /pipeline/streammux/dimensions/set
    ## dsl_pipeline_streammux_dimensions_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_streammux_dimensions_set(params['name'], params['width'], params['height'])
            result = { 'service': 'dsl_pipeline_streammux_dimensions_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_streammux_dimensions_set', 
                'result': sys.exc_info()[0] }
        return result

##
## /pipeline/streammux/padding/...
## dsl_pipeline_streammux_padding...
##
class padding(object):

    ##
    ## /pipeline/streammux/padding/get
    ## dsl_pipeline_streammux_padding_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, enabled = dsl_pipeline_streammux_padding_get(params['name'])
            result = { 'service': 'dsl_pipeline_streammux_padding_get', 
                'result': dsl_return_value_to_string(retval), 'enabled': enabled }
        except:
            result = { 'service': 'dsl_pipeline_streammux_padding_get', 
                'result': sys.exc_info()[0], 'enabled': 0 }
        return result

    ##
    ## /pipeline/streammux/padding/set
    ## dsl_pipeline_streammux_padding_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_pipeline_streammux_padding_set(params['name'], params['enabled'])
            result = { 'service': 'dsl_pipeline_streammux_padding_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_pipeline_streammux_padding_set', 
                'result': sys.exc_info()[0] }
        return result

