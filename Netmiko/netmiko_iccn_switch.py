from netmiko import ConnectHandler
import json

switch = {'device_type': 'broadcom_icos', 'host': '172.16.0.3', 'port': 22, 'username': 'admin', 'password': 'admin'}

print(f'Connecting to {switch["host"]}...')
con = ConnectHandler(**switch)
# prompt = con.find_prompt()
# Output is Switch#, which implies that the default mode of ICCN Switch is enable mode.

# print(con.check_config_mode())  # To check if it is in global configuration mode, it returns False if not in
# global config mode
con.send_command('ter len 0')
showVersion = con.send_command('show switch')

# print(showVersion)

with open('config.cfg', 'w') as f:
    f.write(showVersion)

with open('config.cfg') as f:
    reader = f.read()
with open('config.json', 'w') as f:
    json.dump(reader, f)
with open('config.json') as f:
    data = json.load(f)
print(data)

# to enter global configuration mod in ICCN switch
con.config_mode('config terminal')
con.send_command('hostname Switch7053')
print(f'')

# print(con.check_config_mode())

print('Disconnecting...')
con.disconnect()
