# from netmiko import Netmiko
from netmiko import ConnectHandler # for second basic script
# import time

# For ICCN switches the device type is broadcom_icos, and for that we import BroadcomIcoSSH from netmiko.broadcom.
# I got that from show version command on the switch CLI.
# Basic script for accessing ICCN WX6012 switch through SSH

"""
con = Netmiko(host='10.0.0.3', port='22', username='admin', password='admin', device_type='broadcom_icos')
print('Connecting...')

output = con.send_command('show version')
print(output)

print('Closing connection')
con.disconnect()
"""

# Another basic script is using ConnectHandler

switch = {'device_type': 'broadcom_icos', 'host': '10.0.0.3', 'port': '22', 'username': 'admin',
          'password': 'admin'}

con = ConnectHandler(**switch)
print('Connecting...')

output = con.send_command('show version')
print(output)

print('Closing connection')
con.disconnect()
