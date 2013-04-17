import json
from uuid import uuid4


def json_out(out):
	return json.dumps(out, indent=4)

#[[user,ip][user,ip][user,ip]]
machine_list = []
def create_machines(filename):
	mf = open(filename)
	for line in mf.readlines():
		line = line[:-1]
		if line:
			machines = line.split("@")
			machine_list.append(machines + [str(uuid4())])
	print machine_list

#[[user,ip,path][user,ip,path][user,ip,path]]
img_list = []
def create_images(filename):	
	imgf = open(filename)
	for line in imgf.readlines():
		line = line[:-1]
		if line:
			img1 = line.split("@")
			img2 = img1[1].split(":")
			img = []
			img.append(img1[0])
			img.append(img2[0])
			img.append(img2[1])
			img_list.append(img)
	print img_list

def intialize(server, attrs):
	server.send_response(attrs)
	server.send_header("content-type" , "application/json")
	server.end_headers()

next_vmid=0
def next_vmid():
	global next_vmid
	next_vmid+=1
	return next_vmid

reqs = {}

def vmid_reqs(vmid):
	for uid in reqs:
		if reqs[uid][0] == vmid:
			print uid
			return uid

def make_path(user,ip):
	path = 'remote+ssh://' + user + '@' + ip + '/'
	return path

def find_machine_pmid(pmid):
	global machine_list
	for i in machine_list:
		if i[2] == pmid:
			return i

