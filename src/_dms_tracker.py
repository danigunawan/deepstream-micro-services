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
            result = { "service": "dsl_tracker_ktl_new", "result": sys.exc_info()[0] }
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
            result = { "service": "dsl_tracker_iou_new", "result": sys.exc_info()[0] }
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
                'result': sys.exc_info()[0], 'max_width': 0, 'max_height': 0 }
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
            result = { 'service': 'dsl_tracker_max_dimensions_get', 'result': sys.exc_info()[0] }
        return result

class tracker(object):
    def __init__(self):
        self.ktl = ktl()
        self.iou = iou()
        self.max_dimensions = max_dimensions()

