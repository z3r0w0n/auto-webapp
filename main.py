#!/usr/bin/env python

import os
import sys

import variables as vars

def run_ansible(config_dir):
    ret = os.system("python utils/gen_inventory.py")
    if ret != 0:
        print("ERROR: Error creating Ansible inventory")
        sys.exit(1)

    ansible_inventory = os.path.join(config_dir, 'hosts')
    ret = os.system("ansible-playbook -i "+ansible_inventory+" play.yml")
    if ret != 0:
        print("ERROR: Error running Ansible playbook")
        sys.exit(1)

def run_terraform(terraform_dir):
    cmd = "terraform apply -var-file " + var_file + " -state " + state_file + " -state-out " + out_state_file + " " + terraform_dir
    # cmd = "terraform destroy -var-file " + var_file + " -state " + state_file + " -state-out " + out_state_file + " " + terraform_dir
    ret = os.system(cmd)
    if ret != 0 :
        print("Failure while provisioning. Exiting.")
        sys.exit(1)
    return True

if __name__ == "__main__":

    config_dir = vars.config_dir
    terraform_dir = vars.terraform_dir

    var_file = vars.var_file
    state_file = vars.state_file
    out_state_file = vars.out_state_file

    if run_terraform(terraform_dir):
        aflag = run_ansible(config_dir)
