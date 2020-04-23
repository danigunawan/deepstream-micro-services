################################################################################
#
# Copyright (c) 2019-2020, Robert Howell. All rights reserved.
#
################################################################################
import sys
import cherrypy
from dsl import *

class csi(object):

    ## /source/csi/new
    ## dsl_source_csi_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_source_csi_new(params['name'], params['width'], params['height'], params['fps_n'], params['fps_d'])
            result = { 'service': 'dsl_source_csi_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_source_csi_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

class usb(object):

    ##
    ## /source/usb/new
    ## dsl_source_usb_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_source_usb_new(params['name'], params['width'], params['height'], params['fps_n'], params['fps_d'])
            result = { 'service': 'dsl_source_usb_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_source_usb_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

class uri(object):

    ##
    ## /source/uri/new
    ## dsl_source_uri_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_source_uri_new(params['name'], params['uri'], params['is_live'], 
                params['cudadec_mem_type'], params['intra_decode'], params['drop_frame_interval'])
            result = { 'service': 'dsl_source_uri_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_source_uri_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

class rtsp(object):

    ##
    ## /source/rtsp/new
    ## dsl_source_rtsp_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_source_rtsp_new(params['name'], params['uri'], params['protocol'], 
                params['cudadec_mem_type'], params['intra_decode'], params['drop_frame_interval'])
            result = { 'service': 'dsl_source_rtsp_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_source_rtsp_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

class dimensions(object):

    ##
    ## /source/dimensions/get
    ## dsl_source_dimensions_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, width, height = dsl_source_dimensions_get(params['name'])
            result = { 'service': 'dsl_source_dimensions_get', 
                'result': dsl_return_value_to_string(retval), 'width': width, 'height': height }
        except:
            result = { 'service': 'dsl_source_dimensions_get', 
                'result': { 'exception' :  sys.exc_info()[0] }, 'width': 0, 'height': 0 }
        return result

class frame_rate(object):

    ##
    ## /source/frame_rate/get
    ## dsl_source_frame_rate_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, fps_n, fps_d = dsl_source_frame_rate_get(params['name'])
            result = { 'service': 'dsl_source_framerate_get', 
                'result': dsl_return_value_to_string(retval), 'fps_n': fps_n, 'fps_d': fps_d }
        except:
            result = { 'service': 'dsl_source_framerate_get', 
                'result': { 'exception' :  sys.exc_info()[0] }, 'fps_n': 0, 'fps_d': 0 }
        return result


class uri_path(object):

    ##
    ## /source/decode/uri/get
    ## dsl_source_decode_uri_get
    ##
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, uri = dsl_source_decode_uri_get(params['name'])
            result = { 'service': 'dsl_source_decode_uri_get', 
                'result': dsl_return_value_to_string(retval), 'uri': uri }
        except:
            result = { 'service': 'dsl_source_decode_uri_get', 
                'result': { 'exception' :  sys.exc_info()[0] }, 'uri': 0 }
        return result

    ##
    ## /source/decode/uri/set
    ## dsl_source_decode_uri_set
    ##
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval, uri = dsl_source_decode_uri_set(params['name'], params['uri'])
            result = { 'service': 'dsl_source_decode_uri_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_source_decode_uri_get', 
                'result': { 'exception' :  sys.exc_info()[0] } }
        return result

class decode(object):
    def __init__(self):
        self.uri = uri_path()

class source(object):
    def __init__(self):
        self.csi = csi()
        self.usb = usb()
        self.uri = uri()
        self.rtsp = rtsp()
        self.dimensions = dimensions()
        self.frame_rate = frame_rate()
        self.decode = decode()

