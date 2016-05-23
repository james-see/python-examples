#!/usr/bin/python
# Author: James Campbell
# Date: May 23rd 2016
# Date Updated:
# What: Starts a http server as an example (works in Python 3)
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

hostPort = 10010

hostName = "localhost"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

#Handler = SimpleHTTPServer.SimpleHTTPRequestHandler(path='/Users/jclabpro/projects/testweb/')
#httpd = SocketServer.TCPServer(("", PORT), Handler)
#httpd.path = '/Users/jclabpro/projects/testweb/'
#print("serving at port {}".format(PORT))
#httpd.serve_forever()

# can also do this from the command line via
# python3 -m http.server 10010 --bind 127.0.0.1
