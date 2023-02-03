import paramiko
import time

sshcli = paramiko.SSHClient()
sshcli.load_system_host_keys()
sshcli.set_missing_host_key_policy(paramiko.AutoAddPolicy())

sshcli.connect(hostname='30.0.0.2', port=22, username='admin', password='admin', look_for_keys=False, allow_agent=False)

shell = sshcli.invoke_shell()

list = [1,2,3,4,5]
for i in list:
    shell.send(f"while true; do zabbix_sender -z 18.237.29.71 -s 'Custom Server' -k shazabkey -o {i}; sleep 1; done" + '\n')
    time.sleep(2)
    print(f"while true; do zabbix_sender -z 18.237.29.71 -s 'Custom Server' -k shazabkey -o {i}; sleep 1; done")



if sshcli.get_transport().is_active():
    print('Closing connection...')
    sshcli.close()