import subprocess
import prerequisites

def run_terraform(terraform_dir):
    # os.system("cd "+terraform_dir)
    # os.system("terraform apply")
    p = subprocess.Popen("terraform apply", cwd=terraform_dir)
    p.wait()

if __name__ == "__main__":
    prerequisites.run()

    terraform_dir = "./terraform/"
    run_terraform(terraform_dir)
