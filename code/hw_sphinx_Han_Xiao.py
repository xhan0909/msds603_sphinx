import paramiko
from os.path import expanduser

def ssh_client():
    """Return ssh client object"""
    return paramiko.SSHClient()

def ssh_connection(ssh, ec2_address, user, key_file):
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ec2_address, username=user, key_filename=expanduser("~") + key_file)
    return ssh

def create_or_update_environment(ssh):
    stdin, stdout, stderr = \
                    ssh.exec_command("conda env create -f "
                             "~/msds603_hw/env_MSDS603.yml")
    if (b'already exists' in stderr.read()):
        stdin, stdout, stderr = \
                    ssh.exec_command("conda env update -f "
                             "~/msds603_hw/env_MSDS603.yml")
        print(stdout.read())

def main():
    ec2_address = "ec2-54-212-242-75.us-west-2.compute.amazonaws.com"
    user = "ec2-user"
    key_file = "/OneDrive/licenses/xhan-oregon.pem"

    ssh = ssh_client()
    ssh_connection(ssh, ec2_address, user, key_file)
    create_or_update_environment(ssh)


if __name__=='__main__':
    main()
