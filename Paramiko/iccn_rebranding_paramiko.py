import paramiko
import getpass
import time

sshcli = paramiko.SSHClient()
sshcli.load_system_host_keys()
sshcli.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ipaddr = input('Enter the IP address of the host: ')
print('Logging in as root...')
time.sleep(1)
pswd = getpass.getpass('Enter the root password: ')
print('\n')

print(f'Connecting to {ipaddr}...')
sshcli.connect(hostname=ipaddr, port=22, username='root', password=pswd, look_for_keys=False, allow_agent=False)
time.sleep(1)

shell = sshcli.invoke_shell()
print('Connected!!!')
time.sleep(1)
print('\n')

shell.send('pkg info bash' + '\n')
time.sleep(2)
out = shell.recv(10000)
if "pkg: No package(s) matching bash" in out.decode():
    shell.send('pkg install bash' + '\n')
    time.sleep(2)
    shell.send('y' + '\n')
    time.sleep(2)

with open('commands.txt') as f:
    commands = f.read().splitlines()

print(f'Changes taking place on {ipaddr}, Please wait...')
for cmnd in commands:
    # print(f'Sending command: {cmnd}')
    shell.send(cmnd + '\n')
    time.sleep(4)
out1 = shell.recv(10000)

shell.send('ls /usr/local/opnsense/www/themes/tukan/build/images/' + '\n')
time.sleep(2)
output1 = shell.recv(10000)
# print(output.decode())

shell.send('cd /usr/local/opnsense/version/' + '\n')
time.sleep(2)
out2 = shell.recv(10000)
shell.send("jq '' core | grep ICCN" + '\n')
time.sleep(2)
output2 = shell.recv(10000)
# print(output2.decode())

print('#' * 100)

if 'iccn' in output1.decode() and 'ICCN' in output2.decode():
    print('Changes have been changed! Please refresh your GUI and/or clear the cache on your browser.')
else:
    print("Changes haven't been made!!! Please try again.")

if sshcli.get_transport().is_active():
    print('Closing connection...')
    sshcli.close()
