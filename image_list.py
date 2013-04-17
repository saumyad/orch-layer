import get
from get import json_out
import libvirt as libv

def request(server, attrs):
	get.intialize(server,200)
	out = []
	try:
		for i in get.images:
			out.append({"id":i[3], "name":find_image_name(i[2])})

		server.write(json_out({"images":out}))

	except:
		server.write(json_out({"images":[]}))
