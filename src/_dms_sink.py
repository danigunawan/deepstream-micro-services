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
## /sink/...
## dsl_sink_...
##

class sink(object):
    def __init__(self):
        self.fake = fake()
        self.overlay = overlay()
        self.window = window()
        self.file = file()
        self.image = image()
        self.rtsp = rtsp()
        self.num_in_use = num_in_use()

##
## /sink/fake/...
## dsl_sink_fake_...
##

class fake(object):

    ## /sink/fake/new
    ## dsl_sink_fake_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_fake_new(params['name'])
            result = { 'service': 'dsl_sink_fake_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_fake_new', 'result': sys.exc_info()[0] }
        return result

##
## /sink/overlay/...
## dsl_sink_overlay_...
##

class overlay(object):

    ## /sink/overlay/new
    ## dsl_sink_overlay_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_overlay_new(params['name'], params['overlay_id'], params['display_id'], params['depth'],
                params['offsetX'], params['offsetY'], params['width'], params['height'])
            result = { 'service': 'dsl_sink_overlay_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_overlay_new', 'result': sys.exc_info()[0] }
        return result

##
## /sink/window/...
## dsl_sink_window_...
##

class window(object):

    ## /sink/window/new
    ## dsl_sink_window_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_window_new(params['name'], 
                params['offsetX'], params['offsetY'], params['width'], params['height'])
            result = { 'service': 'dsl_sink_window_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_window_new', 'result': sys.exc_info()[0] }
        return result

##
## /sink/file/...
## dsl_sink_file_...
##

class file(object):

    ## /sink/file/new
    ## dsl_sink_file_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_file_new(params['name'], params['filepath'],
                params['codec'], params['container'], params['bitrate'], params['interval'])
            result = { 'service': 'dsl_sink_file_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_file_new', 'result': sys.exc_info()[0] }
        return result

    ## /sink/file/download
    ## dsl_sink_file_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            result = { 'service': 'dsl_sink_file_new', 'result': "DSL_RESULT_SUCCESS" }
        except:
            result = { 'service': 'dsl_sink_file_new', 'result': sys.exc_info()[0] }
        return result
    def download(self):
        path = os.path.join(absDir, 'pdf_file.pdf')
        return static.serve_file(path, 'application/x-download',
            'attachment', os.path.basename(path))

##
## /sink/image/...
## dsl_sink_image...
##

class image(object):

    def __init__(self):
        self.frame_capture = frame_capture()
        self.object_capture = object_capture()

    ## /sink/image/new
    ## dsl_sink_image_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_image_new(params['name'], params['outdir'])
            result = { 'service': 'dsl_sink_image_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_image_new', 'result': sys.exc_info()[0] }
        return result

##
## /sink/image/frame_capture/...
## dsl_sink_image_frame_capture_...
##

class frame_capture(object):
    def __init__(self):
        self.enabled = frame_capture_enabled()
        self.interval = frame_capture_interval()
        
##
## /sink/image/object_capture/...
## dsl_sink_image_object_capture...
##
class object_capture(object):
    def __init__(self):
        self.enabled = object_capture_enabled()
        self.classid = object_capture_class()

##
## /sink/image/frame_capture/enabled/...
## dsl_sink_image_frame_capture_enabled_...
##

class frame_capture_enabled(object):

    ## /sink/image/frame_capture/enabled/get
    ## dsl_sink_image_frame_capture_enabled_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, enabled = dsl_sink_image_frame_capture_enabled_get(params['name'])
            result = { 'service': 'dsl_sink_image_frame_capture_enabled_get', 
                'result': dsl_return_value_to_string(retval), 'enabled': enabled }
        except:
            result = { 'service': 'dsl_sink_image_frame_capture_enabled_get', 
                'result': { 'exception' :  sys.exc_info()[0],  'enabled': 0 } }
        return result

    ## /sink/image/frame_capture/enabled/set
    ## dsl_sink_image_frame_capture_enabled_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_image_frame_capture_enabled_set(params['name'], params['enabled'])
            result = { 'service': 'dsl_sink_image_frame_capture_enabled_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_image_frame_capture_enabled_get', 
                'result': sys.exc_info()[0] }
        return result

##
## /sink/image/frame_capture/interval/...
## dsl_sink_image_frame_capture_interval_...
##
class frame_capture_interval(object):

    ## /sink/image/frame_capture/interval/get
    ## dsl_sink_image_frame_capture_interval_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, interval = dsl_sink_image_frame_capture_interval_get(params['name'])
            result = { 'service': 'dsl_sink_image_frame_capture_interval_get', 
                'result': dsl_return_value_to_string(retval), 'interval': interval }
        except:
            result = { 'service': 'dsl_sink_image_frame_capture_interval_get', 
                'result': { 'exception' :  sys.exc_info()[0],  'interval': 0 } }
        return result

    ## /sink/image/frame_capture/interval/set
    ## dsl_sink_image_frame_capture_interval_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_image_frame_capture_interval_set(params['name'], params['interval'])
            result = { 'service': 'dsl_sink_image_frame_capture_interval_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_image_frame_capture_interval_set', 
                'result': sys.exc_info()[0] }
        return result

##
## /sink/image/object_capture/enabled/...
## dsl_sink_image_object_capture_enabled_...
##

class object_capture_enabled(object):

    ## /sink/image/object_capture/enabled/get
    ## dsl_sink_image_object_capture_enabled_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, enabled = dsl_sink_image_object_capture_enabled_get(params['name'])
            result = { 'service': 'dsl_sink_image_object_capture_enabled_get', 
                'result': dsl_return_value_to_string(retval), 'enabled': enabled }
        except:
            result = { 'service': 'dsl_sink_image_object_capture_enabled_get', 
                'result': { 'exception' :  sys.exc_info()[0],  'enabled': 0 } }
        return result

    ## /sink/image/object_capture/enabled/set
    ## dsl_sink_image_object_capture_enabled_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_image_object_capture_enabled_set(params['name'], params['enabled'])
            result = { 'service': 'dsl_sink_image_object_capture_enabled_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_image_object_capture_enabled_set', 
                'result': sys.exc_info()[0] }
        return result

##
## /sink/image/object_capture/class/...
## dsl_sink_image_object_capture_class_...
##
class object_capture_class(object):

    ## /sink/image/object_capture/class/add
    ## dsl_sink_image_object_capture_class_a
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def add(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_image_object_capture_class_add(params['name'],
                params['class_id'], params['full_frame'], params['capture_limit'])
            result = { 'service': 'dsl_sink_image_object_capture_class_add', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_image_object_capture_class_add', 
                'result': sys.exc_info()[0] }
        return result

    ## /sink/object/object_capture/class/remove
    ## dsl_sink_image_object_capture_class_remove
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def remove(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_image_object_capture_class_remove(params['name'], 
                params['class_id'])
            result = { 'service': 'dsl_sink_image_object_capture_class_remove', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_image_object_capture_class_remove', 
                'result': sys.exc_info()[0] }
        return result

##
## /sink/rtsp/...
## dsl_sink_rtsp...
##

class rtsp(object):

    ## /sink/rtsp/new
    ## dsl_sink_rtsp_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_sink_rtsp_new(params['name'], params['host'],
                params['udp_port'], params['rtmp_port'], params['codec'], params['bitrate'], params['interval'])
            result = { 'service': 'dsl_sink_rtsp_new', 'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_sink_rtsp_new', 'result': sys.exc_info()[0] }
        return result

##
## /sink/num_in_use/...
## dsl_sink_num_in_use_...
##

class num_in_use(object):

    def __init__(self):
        self.max = max()

    ##
    ## /sink/num_in_use/get
    ## dsl_sink_num_in_use_get
    ##
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get(self):
        try:
            num = dsl_sink_num_in_use_get()
            result = { 'service': 'dsl_sink_num_in_use_get', 
                'num': num }
        except:
            result = { 'service': 'dsl_sink_decode_uri_get', 
                'num': sys.exc_info()[0] }
        return result

##
## /sink/num_in_use/max/...
## dsl_sink_num_in_use_max...
##

class max(object):

    ##
    ## /sink/num_in_use/max/get
    ## dsl_sink_num_in_use_max_get
    ##
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get(self):
        try:
            num = dsl_sink_num_in_use_max_get()
            result = { 'service': 'dsl_sink_num_in_use_max_get', 
                'num': num }
        except:
            result = { 'service': 'dsl_sink_num_in_use_max_get', 
                'num': sys.exc_info()[0] }
        return result

    ##
    ## /sink/num_in_use/max/get
    ## dsl_sink_num_in_use_max_set
    ##
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            success = dsl_sink_num_in_use_max_set(params['num'])
            result = { 'service': 'dsl_sink_num_in_use_max_set', 
                'result': success }
        except:
            result = { 'service': 'dsl_sink_num_in_use_max_set', 
                'result': sys.exc_info()[0] }
        return result

