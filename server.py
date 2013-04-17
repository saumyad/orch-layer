#!/usr/bin/env python
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import parser
import get
import sys

PORT_NUMBER = 80;
HOST_NAME = "";

class Server(ThreadingMixIn, HTTPServer):
	pass

class Request_handler(BaseHTTPRequestHandler):
	def do_GET(self):
		url = self.path
		if url[-1:] == '/':
			url = url[:-1]
		
		#split at max once for getting variables...
		attrs = ""
		if '?' in url:
			url, attrs = url.split('?',1)
		
		vm_attributes = parser.url_parse(attrs)
		
		if url[-1:] == '/':
			url = url[:-1]

		parser.redirect(self,url, vm_attributes)

		print vm_attributes
		print url

	def write(self, output):
		self.wfile.write(output)



if __name__ == "__main__":

	if len(sys.argv) < 3:
		print "Format: ./script pm_file image_file"
		exit(1)

	get.create_machines(sys.argv[1])
	get.create_images(sys.argv[2])

	request = Server((HOST_NAME, PORT_NUMBER), Request_handler)
	
	print "Server at PORT:" ,PORT_NUMBER, "started\n"
	#while(1):
	try:
		request.handle_request()
	except:
		print "Error: Cannot handle request\n"


