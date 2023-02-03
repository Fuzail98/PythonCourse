import paramiko
import time
# import getpass

ssh_cli = paramiko.SSHClient()
ssh_cli.load_system_host_keys()
ssh_cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)


switch7028 = {'hostname': '10.0.0.2', 'port': '22', 'username': 'admin', 'password': 'admin'}
switch6012 = {'hostname': '10.0.0.5', 'port': '22', 'username': 'admin', 'password': 'admin'}
switch6010 = {'hostname': '10.0.0.6', 'port': '22', 'username': 'admin', 'password': 'admin'}

switches = [switch6012, switch6010, switch7028]

for switch in switches:
    print(f'Connecting to {switch["hostname"]}')
    ssh_cli.connect(**switch, look_for_keys=False, allow_agent=False)

    shell = ssh_cli.invoke_shell()
    print('Connected!!!')

    shell.send('show version\n')
    time.sleep(1)

    output = shell.recv(10000).decode()
    print(output)


if ssh_cli.get_transport().is_active():
    print('Closing connection')
    ssh_cli.close()
