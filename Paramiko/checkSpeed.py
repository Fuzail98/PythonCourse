import paramiko
import time

sshSwitch = paramiko.SSHClient()
sshSwitch.load_host_keys()
sshSwitch.set_missing_host_key_policy(paramiko.AutoAddPolicy())


switches = {'hostname' : '', 'port' : 22, 'username' : '', 'password' : ''}

sshSwitch.connect(**switches, look_for_keys=False, allow_agent=False)

shell = sshSwitch.invoke_shell()


shell.send('command\n')
time.sleep(2)

out = shell.recv(10000)
# print(out.decode())

if sshSwitch.get_transport().is_active():
    sshSwitch.close()
    