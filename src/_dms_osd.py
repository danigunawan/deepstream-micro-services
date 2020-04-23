################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
################################################################################
import sys
import cherrypy
from dsl import *

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
                'result': { 'exception' :  sys.exc_info()[0] } }
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
                'result': { 'exception' :  sys.exc_info()[0] } }
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
                'result': { 'exception' :  sys.exc_info()[0] } }
        return result

class redaction(object):

    def __init__(self):
        self.enabled = redaction_enabled()
        self.classid = redaction_class()

class osd(object):

    def __init__(self):
        self.redaction = redaction()

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

