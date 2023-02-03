# Telnet custom class for one device

import time
from datetime import datetime


class Device:

    def __init__(self, host, username, password, tn=None):
        self.host = host
        self.username = username
        self.password = password
        self.tn = tn

    def connect(self):
        import telnetlib
        self.tn = telnetlib.Telnet(self.host)

    def authenticate(self):
        self.tn.read_until(b'Username:')
        self.tn.write(self.username.encode() + b'\n')

        self.tn.read_until(b'Password:')
        self.tn.write(self.password.encode() + b'\n')

    def send(self, command, timeout=0.5):
        print(f'Sending command: {command}')
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

    def send_from_list(self, commands):
        for cmd in commands:
            self.send(cmd)

    def send_from_file(self, fname):
        with open(fname) as f:
            cmnds = f.read().splitlines()
            # print(cmnds)
        s.send_from_list(cmnds)

    def show(self):
        output = self.tn.read_all().decode('utf-8')
        return output


# Telnet custom class for one device

# switch6012 = Device('10.0.0.3', 'admin', 'admin')
# switch6012.connect()
# switch6012.authenticate()
# switch6012.send('terminal length 0')
# switch6012.send('en')
# switch6012.send('show running-config')
# switch6012.send('exit')
# print('#'*50)
# output = switch6012.show()

# The below block of code is used to save the running config of the ICCN switch specifically

# # output_list = output.splitlines()
# # output_list = output_list[4:-2]
# # output = '\n'.join(output_list)
# print(output)

# Telnet class for multiple devices

# switch6012 = {'host': '10.0.0.3', 'username': 'admin', 'password': 'admin', 'config_mode': 'configure terminal'}
# switch7028 = {'host': '10.0.0.2', 'username': 'admin', 'password': 'admin', 'config_mode': 'configure terminal'}

# # One can add other parameters if they are different with respect to other devices and use them accordingly.

# switches = [switch7028, switch6012]

# for switch in switches:
#     print(f'Connecting to {switch["host"]}...\n')
#     time.sleep(2)
#     s = Device(host=switch['host'], username=switch['username'], password=switch['password'])
#     s.connect()
#     s.authenticate()
#     s.send('terminal length 0')
#     s.send('en')
#     s.send('show running-config')
#     s.send('exit')
#     print('#'*50)
#     output = s.show()

# The below block of code is used to save the running config of the ICCN switch specifically

#     # output_list = output.splitlines()
#     # output_list = output_list[4:-2]
#     # output = '\n'.join(output_list)
#     print(output)

# Modifying the above code by adding a new function in class Device

switch6012 = {'host': '10.0.0.3', 'username': 'admin', 'password': 'admin', 'config_mode': 'configure terminal'}
switch7028 = {'host': '10.0.0.2', 'username': 'admin', 'password': 'admin', 'config_mode': 'configure terminal'}

# One can add other parameters if they are different with respect to other devices and use them accordingly.

switches = [switch7028, switch6012]

for switch in switches:
    print(f'Connecting to {switch["host"]}...\n')
    # time.sleep(2)
    s = Device(host=switch['host'], username=switch['username'], password=switch['password'])
    s.connect()
    s.authenticate()

    # Instead of writing commands by calling the function one by one, we are writing a list of commands and then
    # calling another defined function def send_from_list()

    # commands = ['terminal length 0', 'en', 'show running-config', 'exit']
    # s.send_from_list(commands)

    # Taking commands list from a text file

    # with open('cmnds.txt', 'r') as f:
    #     cmnds = f.read().splitlines()
    #     # print(cmnds)
    # s.send_from_list(cmnds)

    s.send_from_file('cmnds.txt')

    print('#'*50)
    output = s.show()

    # The below block of code is used to save the running config of the ICCN switches specifically

    output_list = output.splitlines()
    output_list = output_list[4:-2]
    output = '\n'.join(output_list)
    # print(output)


# To write the configuration on to a file
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    fname = f'{switch["host"]}_{year}-{month}-{day}.txt'

    with open(fname, 'w') as f:
        f.write(output)
