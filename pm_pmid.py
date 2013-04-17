import get
from get import json_out

def request(server, attrs):
	get.intialize(server,200)
	try:
		pmid = attrs["pmid"]
		machine = get.find_machine_pmid(pmid)
		user = machine[0]
		ip = machine[1]
		connect = libv.open(get.make_path(user,ip))
		
		#int numDomains;
		#numDomains = NumOfDomains(connect)
		
		#server.write(json_out({"pmid":pmid,"vms":numDomains}))		

		#int *activeDomains
		#activeDomains = malloc(sizeof(int) * numDomains)

		domains = connect.listDefinedDomains()

		out = {"pmid": pmid}

		for d in domains:
			out.append(find_vmid_name(d))
		server.write(json_out({"vmids":out}))

	except:
		server.write(json_out({"vmids":[]}))
