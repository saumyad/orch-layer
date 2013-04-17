from get import json_out
import get
import libvirt as libv

def request(server, attrs):
	get.intialize(server,200)
	try:
		connect = libv.open("qemu:///system")
		vmid = int(attrs["vmid"])
		req = connect.lookupByName(get.reqs[vmid][0])

		if req.isActive():
			req.destroy()

		req.undefine()
		del get.reqs[vmid]

		server.write(json_out({"status":1}))
	except:
		server.write(json_out({"status":0}))
