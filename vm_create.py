import libvirt as libv
import get
from get import json_out
import server
from random import random

def create_xml(vm_name, instance_type):
	xml = r"<domain type='" + instance_type + 			\
	    r"'><name>" + vm_name + r"</name>				\
	      <memory>100428</memory>					\
	      <vcpu>1</vcpu>						\
	      <os>							\
	        <type arch='x86_64' machine='pc'>hvm</type>		\
		<boot dev='hd'/>					\
	      </os>							\
	      <features>						\
	        <acpi/>							\
          	<apic/>							\
	      	<pae/>							\
	      </features>						\
	      <on_poweroff>destroy</on_poweroff>			\
  	      <on_reboot>restart</on_reboot>				\
	      <on_crash>restart</on_crash>				\
	      <devices>							\
	        <emulator>/usr/bin/qemu-system-x86_64</emulator>	\
	        <disk type='file' device='disk'>			\
  	        <driver name='qemu' type='raw'/>			\
		<source file='/root/images/VM-linux-0.2.img'/>		\
		<target dev='hda' bus='ide'/>				\
		<address type='drive' controller='0' bus='0' unit='0'/>	\
		</disk>							\
	      </devices>						\
   	      </domain>"

	return xml


def request(server, attrs):
	get.intialize(server, 200)

	try:
		name = attrs["name"]
		instance_type = int(attrs["instance_type"])
		#addr = "root@127.0.0.1/"
		
		machine = get.machine_list[random()*len(get.machines_list)]
		user = machine[0]
		ip = machine[1]
		connect = libv.open(get.make_path(user, ip))
		req = connect.defineXML(create_xml(name, connect.getType().lower()))
		try:
			req.create()
		except:
			server.write(json_out({"vmid":0}))

		vmid = get.next_vmid()
		get.req[vmid] = [name, instance_type, machine[2]]

		server.write(json_out({"vmid":vmid}))
	except:
		server.write(json_out({"vmid":0}))
