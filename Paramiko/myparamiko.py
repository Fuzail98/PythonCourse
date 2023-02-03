# Creating functions for the different processing involved in sending commands to devices

import paramiko
import time


# Connecting to the device which has parameters about info of device


def connect(server_ip, server_port, user, passwd):
    print(f'Connecting to {server_ip}')
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=server_ip, port=server_port, username=user, password=passwd, look_for_keys=False,
                       allow_agent=False)
    return ssh_client


# invoking the shell of the device

def get_shell(ssh_client):
    print('Invoking shell!!!')
    shell = ssh_client.invoke_shell()
    return shell


# sending commands to the device

def send_command(shell, command, timeout=2):
    print(f'Sending command: {command} ')
    shell.send(command + '\n')
    time.sleep(timeout)


# recieving the output

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode()


# closing ssh connectivity

def close(client):
    print(f'Closing the connection...')
    if client.get_transport().is_active():
        client.close()


#if __name__ == "__main__": # This instruction if uncommented and the following block of code indented, then
# importing this 'myparamiko' module in other scripts won't execute the below code
client = connect('10.0.0.2', '22', 'admin', 'admin')

shell = get_shell(client)

send_command(shell, 'enable')
send_command(shell, 'show version')
    # send_command(shell, 'term len 0')
    # send_command(shell, 'show version')
    # send_command(shell, 'sh ip int brief')

output = show(shell)
print(output)

close(client)
