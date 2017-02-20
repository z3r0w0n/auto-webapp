#!/usr/bin/env python
import variables as vars
import subprocess
import json

def get_publicip():
    get_op = subprocess.Popen("terraform output -state="+vars.state_file+" -json ip", stdout=subprocess.PIPE, shell=True)
    (out, err) = get_op.communicate()
    ec2_ips = json.loads(out)
    for ip in ec2_ips['value']:
        public_ip = ip
    return public_ip
