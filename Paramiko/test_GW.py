import paramiko
import time

sshcli = paramiko.SSHClient()
sshcli.load_system_host_keys()
sshcli.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshcli.connect(hostname='10.0.0.1', port=22, username='root', password='opnsense', look_for_keys=False, allow_agent=False)

shell = sshcli.invoke_shell()
shell.send('8' + '\n')
time.sleep(2)

# Installing required packages if not installed

packages = ['bash', 'jq', 'wget']
for pkg in packages:
    shell.send(f'pkg info {pkg}' + '\n')
    time.sleep(2)
    tmpout2 = shell.recv(10000)
    if f"pkg: No package(s) matching {pkg}" in tmpout2.decode():
        shell.send(f'pkg install {pkg}' + '\n')
        time.sleep(2)
        shell.send('y' + '\n')
        time.sleep(2)
        print(f'{pkg} has been installed!')
    else:
        print(f'{pkg} already installed')


if sshcli.get_transport().is_active():
    print('Closing connection...')
    sshcli.close()
