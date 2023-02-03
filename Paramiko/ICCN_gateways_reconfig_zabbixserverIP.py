import threading
import paramiko
import time

def reconfig(gw):
    sshcli = paramiko.SSHClient()
    sshcli.load_system_host_keys()
    sshcli.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Connecting to {gw['ipaddr']}...")
    sshcli.connect(hostname=gw['ipaddr'], port=22, username=gw['usr'], password=gw['pswd'], look_for_keys=False,
                   allow_agent=False)
    shell = sshcli.invoke_shell()
    shell.send('8' + '\n')
    time.sleep(1)
    print(f'Connected to {gw["ipaddr"]}!!!')
    with open('ICCN_switch_SNMPCommands.txt') as c:
        commands = c.read().splitlines()
        print(f'Reconfiguring zabbix service on {gw["ipaddr"]}...')
        for command in commands:
            shell.send(command + '\n')
            time.sleep(2)
