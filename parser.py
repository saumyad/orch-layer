import vm_create
import json
import vm_query
import vm_destroy
#import vm_types
import pm_list
import pm_pmid_listvms
import pm_pmid
import image_list

def redirect(server, url_string, vm_attrs):
	if url_string == "/vm/create":
		vm_create.request(server, vm_attrs);

	elif url_string == "/vm/query":
		vm_query.request(server, vm_attrs)

	elif url_string == "/vm/destroy":
		vm_destroy.request(server, vm_attrs)

	elif url_string == "/vm/types":
		pass;

	elif url_string == "/pm/list":
		pm_list.request(server, vm_attrs)

	elif url_string == "/pm/pmid/listvms":
		pm_pmid_listvms.request(server, vm_attrs)

	elif url_string == "/pm/pmid":
		pm_pmid.request(server, vm_attrs)

	elif url_string == "/image/list":
		image_list.request(server, vm_attrs)
	
	elif url_string == "/quit":
		exit(1)

	else:
		pass;
		#server.send_response(404)
		#server.end_headers()
		#server.write("Webpage not found\n");

		#raise an Exception

def url_parse(url_string):
	attrs = []
	attr_values = {}
	if '&' in url_string:
		attrs = url_string.split('&');
	else:
		if '=' in url_string:
			attrs.append(url_string)
	if attrs:
		for x in attrs:
			var_name, value = x.split('=')
			attr_values[var_name] = value
	return attr_values

def out_json(out):
	return json.dumps(out, indent=4)
