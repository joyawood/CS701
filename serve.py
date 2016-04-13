# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:43:04 2016

@author: Joy
"""

import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

def some_function():
    print ("some_function got called")

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/captureImage':
            # Insert your code here
            some_function()

        self.send_response(200)

httpd = SocketServer.TCPServer(("", 8080), MyHandler)
httpd.serve_forever()