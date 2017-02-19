import os
import sys

import prerequisites

def run_terraform(terraform_dir):
    var_file = terraform_dir + '/override.tfvars'
    state_file = terraform_dir + '/terraform.tfstate'
    out_state_file = state_file

    cmd = "terraform apply -var-file " + var_file + " -state " + state_file + " -state-out " + out_state_file + " " + terraform_dir
    # cmd = "terraform destroy -var-file " + var_file + " " + terraform_dir
    ret = os.system(cmd)
    if ret != 0 :
        print("Failure while provisioning. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    terraform_dir = "./terraform/"
    run_terraform(terraform_dir)
