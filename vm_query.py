from get import json_out
import get

def request(server, attrs):
	get.intialize(server,200)
	try:
		vmid = int(attrs["vmid"])
		vm = get.reqs[vmid]

		server.write(json_out({"vmid":vmid, "name":vm[0],"instance_type":vm[1],"pmid":vm[2]}))
	except:
		server.write(json_out({"vmid":0,"name":"","instance_type":0,"pmid":0}))
