#!/usr/bin/env python

import sys
sys.path.append('./')

import os
import subprocess
import json
import variables as vars

if __name__ == "__main__":
    state_file = vars.state_file
    out_file = os.path.join(vars.config_dir, "hosts")
    in_file = os.path.join(vars.config_dir, "hosts.tmpl")

    private_key_path = vars.private_key_path
    ssh_user = vars.ssh_user

    get_op = subprocess.Popen("terraform output -state="+state_file+" -json ip", stdout=subprocess.PIPE, shell=True)
    (out, err) = get_op.communicate()
    ec2_ips = json.loads(out)

    ip_str = ""
    for ip in ec2_ips['value']:
        ip_str += ip+"\n"

    replacements = {'ansible_ssh_private_key_file':'ansible_ssh_private_key_file='+private_key_path,
                    'ansible_ssh_user':'ansible_ssh_user='+ssh_user,
                    'xxx.xxx.xxx.xxx': ip_str}

    with open(in_file) as infile, open(out_file, 'w') as outfile:
        for line in infile:
            for src, target in replacements.iteritems():
                line = line.replace(src, target)
            outfile.write(line)
