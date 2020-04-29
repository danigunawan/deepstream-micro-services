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
## /source/...
## dsl_source_...
##

class source(object):
    def __init__(self):
        self.csi = csi()
        self.usb = usb()
        self.uri = uri()
        self.rtsp = rtsp()
        self.dimensions = dimensions()
        self.frame_rate = frame_rate()
        self.decode = decode()
        self.num_in_use = num_in_use()

##
## /source/csi/...
## dsl_source_csi...
##

class csi(object):

    ##
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
            result = { 'service': 'dsl_source_csi_new', 'result': sys.exc_info()[0] }
        return result

##
## /source/usb/...
## dsl_source_usb...
##

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
            result = { 'service': 'dsl_source_usb_new', 'result': sys.exc_info()[0] }
        return result

##
## /source/uri/...
## dsl_source_uri...
##

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
            result = { 'service': 'dsl_source_uri_new', 'result': sys.exc_info()[0] }
        return result

##
## /source/rtsp/...
## dsl_source_rtsp...
##

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
            result = { 'service': 'dsl_source_rtsp_new', 'result': sys.exc_info()[0] }
        return result

##
## /source/dimensions/...
## dsl_source_dimensions_...
##

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
                'result': sys.exc_info()[0], 'width': 0, 'height': 0 }
        return result

##
## /source/frame_rate/get
## dsl_source_frame_rate_get
##
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
                'result': sys.exc_info()[0], 'fps_n': 0, 'fps_d': 0 }
        return result

##
## /source/decode/...
## dsl_source_decode_...
##
class decode(object):
    def __init__(self):
        self.uri = uri_path()

##
## /source/decode/uri/...
## dsl_source_decode_uri_...
##

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
                'result': sys.exc_info()[0], 'uri': 0 }
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
            result = { 'service': 'dsl_source_decode_uri_set', 
                'result': sys.exc_info()[0] }
        return result

##
## /source/num_in_use/...
## dsl_source_num_in_use_...
##

class num_in_use(object):

    def __init__(self):
        self.max = max()

    ##
    ## /source/num_in_use/get
    ## dsl_source_num_in_use_get
    ##
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get(self):
        try:
            num = dsl_source_num_in_use_get()
            result = { 'service': 'dsl_source_num_in_use_get', 
                'num': num }
        except:
            result = { 'service': 'dsl_source_decode_uri_get', 
                'num': sys.exc_info()[0] }
        return result

##
## /source/num_in_use/max/...
## dsl_source_num_in_use_max...
##

class max(object):

    ##
    ## /source/num_in_use/max/get
    ## dsl_source_num_in_use_max_get
    ##
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get(self):
        try:
            num = dsl_source_num_in_use_max_get()
            result = { 'service': 'dsl_source_num_in_use_max_get', 
                'num': num }
        except:
            result = { 'service': 'dsl_source_num_in_use_max_get', 
                'num': sys.exc_info()[0] }
        return result

    ##
    ## /source/num_in_use/max/get
    ## dsl_source_num_in_use_max_set
    ##
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            success = dsl_source_num_in_use_max_set(params['num'])
            result = { 'service': 'dsl_source_num_in_use_max_set', 
                'result': success }
        except:
            result = { 'service': 'dsl_source_num_in_use_max_set', 
                'result': sys.exc_info()[0] }
        return result

