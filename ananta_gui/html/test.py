import BaseHTTPServer
import urllib2
import time 
import sys
import os

REDIRECTIONS = {"/index/": "file:///home/gilgamesh/Documents/Ananta/Source/Ananta_vis/index.html",
                "/google/": "http://google.com/"}
LAST_RESORT = "http://google.com/"

class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_GET(s):
	curdir= os.path.dirname(os.path.realpath(__file__))

        f=open(curdir+s.path)
	s.send_response(200)
	s.send_header('Content-type', 'text/html')
	s.end_headers()
	s.wfile.write(f.read())
	f.close()
	return

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(('', 9000), RedirectHandler)
    print time.asctime(), "Server Starts - %s:%s" % ('', 9000)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % ('', 9000)
