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

class demuxer(object):

    ## tee/demuxer/new
    ## dsl_tee_demuxer_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_tee_demuxer_new(params["name"])
            result = { "service": "dsl_tee_demuxer_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_tee_demuxer_new", "result": sys.exc_info()[0] }
        return result

class splitter(object):

    ## tee/splitter/new
    ## dsl_tee_splitter_new
    ##

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def new(self):
        try:
            params = cherrypy.request.json
            retval = dsl_tee_splitter_new(params["name"])
            result = { "service": "dsl_tee_splitter_new", "result": dsl_return_value_to_string(retval) }
        except:
            result = { "service": "dsl_tee_splitter_new", "result": sys.exc_info()[0] }
        return result

class tee(object):

    def __init__(self):
        self.demuxer = demuxer()
        self.splitter = splitter()
    