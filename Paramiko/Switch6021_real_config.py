import myparamiko_functions

# Configuring all ports of the switch as access vlan 3

switch6012 = {'ipaddr': '10.0.0.2', 'portno': '22', 'user': 'admin', 'pswd': 'admin'}

client = myparamiko_functions.connect(**switch6012)
shell = myparamiko_functions.invoke(client)


myparamiko_functions.send(shell, 'terminal length 0')
myparamiko_functions.send(shell, 'en')
myparamiko_functions.send(shell, 'configure terminal')

for i in range(9, 17):
    if i == 10:
        continue
    myparamiko_functions.send(shell, f'interface ge1/{i}')
    myparamiko_functions.send(shell, 'switchport access vlan 20')
    myparamiko_functions.send(shell, 'exit')
myparamiko_functions.send(shell, 'exit')
myparamiko_functions.o_p(shell)
myparamiko_functions.send(shell, 'show running-config')
myparamiko_functions.send(shell, 'write')

output = myparamiko_functions.o_p(shell)
print(output)
# output_list = output.splitlines()
# output_list = output_list[1:-1]
# print(output_list)
# out_put = '\n'.join(output_list)
# print(out_put)

# with open('switch6012_config', 'r+') as f:
#     f.write(out_put)

myparamiko_functions.close(client)
