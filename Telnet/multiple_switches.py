import telnetlib
import time
import getpass

# Getpass module doesn't work in PyCharm. Run this script in cmd to execute it.

switch7028 = {'host': '10.0.0.2', 'username': 'admin'}
switch6012 = {'host': '10.0.0.3', 'username': 'admin'}

switches = [switch7028, switch6012]

for switch in switches:
    print(f'Connecting to {switch["host"]}...')
    password = getpass.getpass(f'Enter the password for {switch["host"]}: ')

    tn = telnetlib.Telnet(host=switch['host'])

    tn.read_until(b'Username:')
    tn.write(switch['username'].encode() + b'\n')
    tn.read_until(b'Password:')
    tn.write(password.encode() + b'\n')

    tn.write(b'terminal length 0\n')
    tn.write(b'en\n')
    tn.write(b'show running-config\n')
    tn.write(b'exit\n')

    time.sleep(2)

    output = tn.read_all()
    output = output.decode()
    output_list = output.splitlines()
    op = output_list[4:-3]
    op = '\n'.join(op)
    print(op)
    print('#'*50)

# To write the configuration into a file
    # fname = switch['host'] + '.conf'
    # with open(fname, 'w') as f:
    #    f.write(op)
