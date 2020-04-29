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
import os
import cherrypy
from dsl import *

class primary(object):

    ##
    ## /gie/primary/new
    ## dsl_gie_primary_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_gie_primary_new(params["name"], params["infer_config_file"],
                params["model_engine_file"], params["interval"])
            result = { "service": "dsl_gie_primary_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_gie_primary_new", "result": sys.exc_info()[0] }
        return result

class secondary(object):

    ##
    ## /gie/secondary/new
    ## dsl_gie_secondary_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            print(params["interval"])
            retval = dsl_gie_secondary_new(params["name"], params["infer_config_file"],
                params["model_engine_file"], params["infer_on_gie_name"], params["interval"])
            result = { "service": "dsl_gie_secondary_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_gie_secondary_new", "result": sys.exc_info()[0] }
        return result

##
## /gie/infer_config_file/...
##
class infer_config_file(object):

    ##
    ## /gie/infer_config_file/get
    ## dsl_gie_infer_config_file_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, file  = dsl_gie_infer_config_file_get(params['name'])
            result = { 'service': 'dsl_gie_infer_config_file_get', 
                'result': dsl_return_value_to_string(retval), 'file': file }
        except:
            result = { 'service': 'dsl_gie_infer_config_file_get', 
                'result': sys.exc_info()[0], 'file': 0 }
        return result

    ##
    ## /gie/infer_config_file/set
    ## dsl_gie_infer_config_file_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_gie_infer_config_file_set(params['name'], params['file'])
            result = { 'service': 'dsl_gie_infer_config_file_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_gie_infer_config_file_set', 
                'result': sys.exc_info()[0] }
        return result

    ##
    ## /gie/infer_config_file/upload
    ## dsl_gie_infer_config_file_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def upload(self, ufile):
        try:
            upload_path = os.path.normpath('/test/config_uploads/')
            upload_file = os.path.join(upload_path, ufile.filename)
            size = 0
            with open(ufile.filename, 'wb') as out:
                while True:
                    data = ufile.file.read(8192)
                    if not data:
                        break
                    out.write(data)
                    size += len(data)
            
            result = { 'service': 'dsl_gie_infer_config_file_upload', 
                'result': 'DSL_RESULT_SUCCESS' }
        except:
            result = { 'service': 'dsl_gie_infer_config_file_upload', 
                'result': sys.exc_info()[0] }
        return result

##
## /gie/model_engine_file/...
##
class model_engine_file(object):

    ##
    ## /gie/infer_config_file/get
    ## dsl_gie_model_engine_file_get
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def get(self):
        try:
            params = cherrypy.request.json
            retval, file  = dsl_gie_model_engine_file_get(params['name'])
            result = { 'service': 'dsl_gie_model_engine_file_get', 
                'result': dsl_return_value_to_string(retval), 'file': file }
        except:
            result = { 'service': 'dsl_gie_model_engine_file_get', 
                'result': sys.exc_info()[0], 'file': 0 }
        return result

    ##
    ## /gie/model_engine/set
    ## dsl_gie_model_engine_file_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def set(self):
        try:
            params = cherrypy.request.json
            retval = dsl_gie_model_engine_file_set(params['name'], params['file'])
            result = { 'service': 'dsl_gie_infer_config_file_set', 
                'result': dsl_return_value_to_string(retval) }
        except:
            result = { 'service': 'dsl_gie_infer_config_file_set', 
                'result': sys.exc_info()[0] }
        return result
        
    ##
    ## /gie/infer_config_file/upload
    ## dsl_gie_infer_config_file_set
    ##

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def upload(self, ufile):
        try:
            upload_path = os.path.normpath('/test/model_uploads/')
            upload_file = os.path.join(upload_path, ufile.filename)
            size = 0
            with open(ufile.filename, 'wb') as out:
                while True:
                    data = ufile.file.read(8192)
                    if not data:
                        break
                    out.write(data)
                    size += len(data)
            
            result = { 'service': 'dsl_gie_model_engine_file_upload', 
                'result': 'DSL_RESULT_SUCCESS' }
        except:
            result = { 'service': 'dsl_gie_infer_config_file_upload', 
                'result': sys.exc_info()[0] }
        return result


class gie(object):
    def __init__(self):
        self.primary = primary()
        self.secondary = secondary()
        self.infer_config_file = infer_config_file()
        self.model_engine_file = model_engine_file()
