import libvirt as libv
import get
from get import json_out

def request(server, attrs):
	get.intialize(server,200)
	try:
		ids = []
		for i in get.machines:
			ids.append(i[2])
		server.write(json_out({"pmids":ids}))

	except:
		server.write(json_out({"pmids":[]}))
