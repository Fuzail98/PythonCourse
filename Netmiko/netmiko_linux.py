from netmiko import ConnectHandler
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

linux = {'device_type': 'linux',
         'host': '10.0.0.52',
         'username': 'iccn',
         'password': 'iccn',
         'port': 22,
         'secret': 'iccn',
         'verbose': True
         }
con = ConnectHandler(**linux)
print(con)
print(con.find_prompt())
# con.enable('sudo su')  # this instruction doesn't work for linux by me.
con.send_command('sudo su', '$')
con.send_command('iccn')
ip = con.send_command('ip a')
print(ip)
