import paramiko
import time


def connect(ipaddr, portno, user, pswd):
    sshcli = paramiko.SSHClient()
    sshcli.load_system_host_keys()
    sshcli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {ipaddr}')
    sshcli.connect(hostname=ipaddr, port=portno, username=user, password=pswd, look_for_keys=False, allow_agent=False)
    return sshcli


def invoke(sshcli):
    print('Invoking Shell!!!')
    shell = sshcli.invoke_shell()
    return shell


def send(shell, cmnd, ipaddr, timeout=1):
    print(f'Sending Command to {ipaddr}: {cmnd}')
    shell.send(cmnd + '\n')
    time.sleep(timeout)


def o_p(shell, n=10000):
    output = shell.recv(n)
    return output.decode()


def close(client):
    if client.get_transport().is_active():
        print('Closing Connection!!!')
        client.close()


if __name__ == '__main__':
    client = connect('10.0.0.2', '22', 'admin', 'admin')
    shell = invoke(client)
    send(shell, 'show version')
    output = o_p(shell)
    print(output)
    close(client)
