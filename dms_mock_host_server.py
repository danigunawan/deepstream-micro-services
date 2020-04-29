
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
sys.path.insert(0, '../')
import os.path
import cherrypy

from dms_client import *
        
class Root(object):

    def __init__(self):
        print('init root')
        
    @cherrypy.expose
    def index(self):
        # Ask for the user's name.
        return '''
            <h2>DMS Target API</h2>
                <form action="TargetNew" method="GET">
                    dms_target_new ( 
                        name = <input type="text" name="name" />
                        url = <input type="text" name="url" />
                    )
                    <input type="submit" /> 
                </form>

            <h2>DMS Pipeline API</h2>
                <form action="PipelineNew" method="GET">
                    dms_pipeline_new ( 
                        name = <input type="text" name="name" />
                    )
                    <input type="submit" /> 
                </form>
                <form action="PipelineDelete" method="GET">
                    dms_pipeline_delete ( 
                        name = <input type="text" name="name" />
                    )
                    <input type="submit" />
                </form>
                <form action="PipelineDeleteAll" method="GET">
                    dms_pipeline_delete_all ( )
                    <input type="submit" />
                </form>

            <h2>DMS Source API</h2>
                <form action="SourceCsiNew" method="GET">
                    dms_source_csi_new ( 
                        name=<input type="text" name="name" />
                        width=<input type="number" name="width" />
                        height=<input type="number" name="height" />
                        fps_n=<input type="number" name="fps_n" />
                        fps_d=<input type="number" name="fps_d" />
                    )
                    <input type="submit" />
                </form>
                <form action="SourceUsbNew" method="GET">
                    dms_source_usb_new ( 
                        name=<input type="text" name="name" />
                        width=<input type="number" name="width" />
                        height=<input type="number" name="height" />
                        fps_n=<input type="number" name="fps_n" />
                        fps_d=<input type="number" name="fps_d" />
                    )
                    <input type="submit" />
                </form>
            '''


    @cherrypy.expose
    def TargetNew(self, name=None, url=None):

        if name and url:
            try:
                retval = dms_target_new(name, url)
            except:
                retval = sys.exc_info()[0]
            return retval
        else:
            return 'Invalid input parameter(s)'

    @cherrypy.expose
    def PipelineNew(self, name=None):

        if name:
            try:
                retval = dms_pipeline_new(name)
            except:
                retval = sys.exc_info()[0]
            return retval
        else:
            return 'Invalid input parameter(s)'

    @cherrypy.expose
    def PipelineDelete(self, name=None):

        if name:
            try:
                retval = dms_pipeline_delete(name)
            except:
                retval = sys.exc_info()[0]
            return retval
        else:
            return 'Invalid input parameter(s)'

    @cherrypy.expose
    def PipelineDeleteAll(self):

        try:
            retval = dms_pipeline_delete_all()
        except:
            retval = sys.exc_info()[0]
        return retval

    @cherrypy.expose
    def SourceCsiNew(self, name=None, width=None, height=None, fps_n=None, fps_d=None):
        if name and width and height and fps_n and fps_d:
            try:
                retval = dms_source_csi_new(name, int(width), int(height), int(fps_n), int(fps_d))
            except:
                retval = sys.exc_info()[0]
            return retval
            
        else:
            return 'Invalid input parameter(s)'

    @cherrypy.expose
    def SourceUsbNew(self, name=None, width=None, height=None, fps_n=None, fps_d=None):
        if name and width and height and fps_n and fps_d:
            try:
                retval = dms_source_usb_new(name, int(width), int(height), int(fps_n), int(fps_d))
            except:
                retval = sys.exc_info()[0]
            return retval
            
        else:
            return 'Invalid input parameter(s)'


root = Root()

hostconf = os.path.join(os.path.dirname(__file__), 'host.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to Root().index().
    cherrypy.quickstart(root, config=hostconf)