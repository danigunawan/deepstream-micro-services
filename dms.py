################################################################################
#
# Copyright (c) 2020, Robert Howell. All rights reserved.
#
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