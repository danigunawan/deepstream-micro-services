################################################################################
#
# Copyright (c) 2019-2020, Robert Howell. All rights reserved.
#
################################################################################
import sys
import cherrypy
from dsl import *

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
            result = { 'service': 'dsl_sink_fake_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

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
            result = { 'service': 'dsl_sink_overlay_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

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
            result = { 'service': 'dsl_sink_window_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

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
            result = { 'service': 'dsl_sink_file_new', 'result': { 'exception' :  sys.exc_info()[0] } }
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
            result = { 'service': 'dsl_sink_file_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result
    def download(self):
        path = os.path.join(absDir, 'pdf_file.pdf')
        return static.serve_file(path, 'application/x-download',
            'attachment', os.path.basename(path))

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
                'result': { 'exception' :  sys.exc_info()[0] } }
        return result

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
                'result': { 'exception' :  sys.exc_info()[0] } }
        return result

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
                'result': { 'exception' :  sys.exc_info()[0] } }
        return result

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
                'result': { 'exception' :  sys.exc_info()[0] } }
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
                'result': { 'exception' :  sys.exc_info()[0] } }
        return result


class frame_capture(object):
    def __init__(self):
        self.enabled = frame_capture_enabled()
        self.interval = frame_capture_interval()

class object_capture(object):
    def __init__(self):
        self.enabled = object_capture_enabled()
        self.classid = object_capture_class()

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
            result = { 'service': 'dsl_sink_image_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

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
            result = { 'service': 'dsl_sink_rtsp_new', 'result': { 'exception' :  sys.exc_info()[0] } }
        return result

class sink(object):
    def __init__(self):
        self.fake = fake()
        self.overlay = overlay()
        self.window = window()
        self.file = file()
        self.image = image()
        self.rtsp = rtsp()

