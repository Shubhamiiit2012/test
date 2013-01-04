from boto.ec2.connection import EC2Connection
import boto
AWS_ACCESS_KEY_ID = 'AKIAIKGBMWUN7KOJ5PEQ'
AWS_SECRET_ACCESS_KEY = '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'

def get_security_group_port_status():
    conn=EC2Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
    
    rs=conn.get_all_security_groups()
    #blocked_ports_string=#raw_input("Type ports seperated by commas and no spaces.\n")
    blocked_port_list=[1000,20000,3000,4000]#create_list_comma_seperated(blocked_ports_string)
    security_groups_map={}
    
    for sec_group in rs:
        security_groups_map[sec_group]=[]
        print("Security group name - "+str(sec_group.name))
        for rule in sec_group.rules:
            port = extract_ports(rule)
            try:
                port_floor_value=int(port[0])
                port_ciel_value=int(port[1])
                if port_floor_value == port_ciel_value:
                    if port_floor_value == 80 or port_floor_value == 443:
                        security_groups_map[sec_group].append("Correct port is open. Port :"+str(port_floor_value))
                        #print(str(port_floor_value)+ " ")
                    else:
                        if port_floor_value in blocked_port_list:
                            security_groups_map[sec_group].append("Error : Port " + str(port_floor_value) + " is supposed to be closed.")
                            #print("Error : Port " + str(port_floor_value) + " is supposed to be closed.")
                        else :
                            security_groups_map[sec_group].append("Error : Another port "+ str(port_floor_value) +" is open.")
                            print("Error : Another port "+ str(port_floor_value) +" is open.")
                else:
                    for port in blocked_port_list:
                        if int(port) > port_floor_value and int(port) < port_ciel_value:
                            security_groups_map[sec_group].append("Error : Port " + port + " is supposed to be closed.")
                            print("Error : Port " + port + " is supposed to be closed.")

            except Exception as value_error:
                print("Error: Unknown port is open.")
    for sec_group_id in security_groups_map:
        security_groups_map[sec_group_id].sort()
    return security_groups_map

def extract_ports(rule):
    tokken1 = str(rule).split("(")
    tokken2 = tokken1[1].split(")")
    port=tokken2[0].split("-")
    return port
    
def create_list_comma_seperated(blocked_port_string):
    tokken = blocked_port_string.split(",")
    return tokken
