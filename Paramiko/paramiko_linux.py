import time
import myparamiko_functions
# import getpass
"""
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname': '10.0.0.52', 'port': '22', 'username': 'iccn', 'password': 'iccn'}

print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)
"""


# One way to write command to linux


"""
 shell = ssh_client.invoke_shell()
 shell.send('ip a\n')
 time.sleep(1)

 output = shell.recv(10000)
 output = output.decode('utf-8')
 print(output)
"""


# another way to write commands to linux using exec_command

"""
stdin, stdout, stderr = ssh_client.exec_command('sudo useradd iccn2\n', get_pty=True)
stdin.write('iccn\n')
time.sleep(0.5)
output = stdout.read().decode()
print(output)

stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n')
print(stdout.read().decode())

if ssh_client.get_transport().is_active():
    print('Closing connection.')
    ssh_client.close()
"""

# Another way to send commands to devices is to create a script with functions with respect to connecting to
# device through ssh, invoking the shell, sending the commands on the shell, receiving the output and
# closing the ssh connection. We have already imported the myparamiko_functions.py file for that.

client = myparamiko_functions.connect('10.0.0.52', '22', 'iccn', 'iccn')
shell = myparamiko_functions.invoke(client)
myparamiko_functions.send(shell, 'ip a')
output = myparamiko_functions.o_p(shell)
print(output)
myparamiko_functions.close(client)
