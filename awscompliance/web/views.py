from ec2ports import get_security_group_port_status
from django.shortcuts import render_to_response

def return_port_details(request):
    port_status_list=get_security_group_port_status()
    #port_status_list = {'key':['da','we'], 'key1': ['sa','sw']}
    return render_to_response("web.html",{"ports_details_map":port_status_list})