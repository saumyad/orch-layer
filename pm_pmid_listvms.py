import get
from get import json_out

def request(server, attrs):
	get.intialize(server,200)
	try:
		pmid = attrs["pmid"]
		
		ids = []
		for i in get.reqs:
			if get.reqs[i][2] == pmid:
				ids.append(get.reqs[i][2])
		server.write(json_out({"vmids":ids}))


	except:
		server.write(json_out({"vmids":[]}))
