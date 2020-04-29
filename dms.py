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

# -*- coding: UTF-8 -*-

import sys
sys.path.insert(0, './src/')
import os.path
import cherrypy
from dsl import *

from _dms_pipeline import pipeline
from _dms_component import component
from _dms_branch import branch
from _dms_source import source
from _dms_gie import gie
from _dms_tracker import tracker
from _dms_tiler import tiler
from _dms_tee import tee
from _dms_osd import osd
from _dms_sink import sink
from _dms_main_loop import main_loop
        
class Root(object):

    def __init__(self):
        print('init root')
        self.pipeline = pipeline()
        self.component = component()
        self.branch = branch()
        self.source = source()
        self.gie = gie()
        self.tracker = tracker()
        self.tiler = tiler()
        self.tee = tee()
        self.osd = osd()
        self.sink = sink()
        self.main_loop = main_loop()
        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def version(self):
        try:
            retval = dsl_version_get()
            result = { "service": "dsl_version_get", "result": retval }
        except:
            result = { "service": "dsl_version_get", "result": { "exception" : formatEx() } }
        return result
        
        

root = Root()

dmsconf = os.path.join(os.path.dirname(__file__), 'dms.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to Root().index().
    cherrypy.quickstart(root, config=dmsconf)