from netmiko import Netmiko
# from netmiko import ConnectHandler
"""
iccn_gw = {'device_type': 'broadcom_icos', 'host': '10.0.0.1', 'port': 22, 'username': 'root',
           'password': 'opnsense', 'secret': 'opnsense', 'verbose': True}

con = ConnectHandler(**iccn_gw)
con.enable('8')
# con.send_command('8')
prompt = con.find_prompt()
print(prompt)
# con.enable('8')
"""
con = Netmiko(host='10.0.0.1', port='22', username='root', password='opnsense', device_type='broadcom_icos')
print('Connecting...')

prompt = con.find_prompt()
print(prompt)

con.send_command('8')
output = con.send_command('opnsense-version')
print(output)

print('Closing connection')
con.disconnect()