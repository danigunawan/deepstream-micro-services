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

##
## /osd/...
## dsl_osd_...
##

class osd(object):

    def __init__(self):
        self.clock = clock()
        self.redaction = redaction()

    ##
    ## /osd/new
    ## dsl_osd_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_osd_new(params["name"], params["is_clock_enabled"])
            result = { "service": "dsl_osd_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_osd_new", "result": { "exception" : sys.exc_info()[0] } }
        return result

##
## /osd/clock/...
## dsl_osd_clock_...
##

class clock(object):

    def __init__(self):
        self.enabled = clock_enabled()

##
## /osd/clock/enabled/...
## dsl_osd_clock_enabled...
##

class clock_enabled(object):

    ## /osd/clock/enabled/get
    ## dsl_osd_clock_enabled_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, enabled = dsl_osd_clock_enabled_get(params['name'])
            result = { 'service': 'dsl_osd_clock_enabled_get', 
                'result': dsl_return_value_to_string(retval), 'enabled': enabled }
        except:
            result = { 'service': 'dsl_osd_clock_enabled_get', 
                'result': { 'exception' :  sys.exc_info()[0],  'enabled': 0 } }
        return result

    ## /osd/clock/enabled/set
    ## dsl_osd_clock_enabled_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_osd_clock_enabled_set(params['name'], params['enabled'])
            result = { 'service': 'dsl_osd_clock_enabled_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_osd_clock_enabled_set', 
                'result': sys.exc_info()[0] }
        return result

##
## /osd/redaction/enabled...
## dsl_osd_...
##

class redaction(object):

    def __init__(self):
        self.enabled = redaction_enabled()
        self.classid = redaction_class()


class redaction_enabled(object):

    ## /osd/redaction/enabled/get
    ## dsl_osd_redaction_enabled_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, enabled = dsl_osd_redaction_enabled_get(params['name'])
            result = { 'service': 'dsl_osd_redaction_enabled_get', 
                'result': dsl_return_value_to_string(retval), 'enabled': enabled }
        except:
            result = { 'service': 'dsl_osd_redaction_enabled_get', 
                'result': { 'exception' :  sys.exc_info()[0],  'enabled': 0 } }
        return result

    ## /osd/redaction/enabled/set
    ## dsl_osd_redaction_enabled_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_osd_redaction_enabled_set(params['name'], params['enabled'])
            result = { 'service': 'dsl_osd_redaction_enabled_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_osd_redaction_enabled_set', 
                'result': sys.exc_info()[0] }
        return result

class redaction_class(object):

    ## /osd/redaction/class/add
    ## dsl_osd_redaction_class_add
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def add(self):
        try:
            params = cherrypy.request.json
            retval = dsl_osd_redaction_class_add(params['name'],
                params['class_id'], params['red'], params['green'], params['blue'], params['alpha'])
            result = { 'service': 'dsl_osd_redaction_class_add', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_osd_redaction_class_add', 
                'result': sys.exc_info()[0] }
        return result

    ## /osd/redaction/class/remove
    ## dsl_osd_redaction_class_remove
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def remove(self):
        try:
            params = cherrypy.request.json
            retval = dsl_osd_redaction_class_remove(params['name'], 
                params['class_id'])
            result = { 'service': 'dsl_osd_redaction_class_remove', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_osd_redaction_class_remove', 
                'result': sys.exc_info()[0] }
        return result

