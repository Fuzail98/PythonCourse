import myparamiko_functions
import getpass

pswd = getpass.getpass('Enter Root password: ')
iccngw = {'ipaddr': '192.168.192.88', 'portno': '22', 'user': 'root', 'pswd': pswd}

client = myparamiko_functions.connect(**iccngw)
shell = myparamiko_functions.invoke(client)


myparamiko_functions.send(shell, '8')
myparamiko_functions.send(shell, 'git clone https://github.com/Fuzail98/iccn-theme.git')
myparamiko_functions.send(shell, 'cd iccn-theme/')
myparamiko_functions.send(shell, 'cp *.* /usr/local/opnsense/www/themes/tukan/build/images/')
# myparamiko_functions.send(shell, 'echo "Done!!"')

output = myparamiko_functions.o_p(shell)
print(output)

myparamiko_functions.close(client)
