import myparamiko_functions
import threading


def backup(switch):
    client = myparamiko_functions.connect(**switch)
    shell = myparamiko_functions.invoke(client)
    ipaddr = switch['ipaddr']

    myparamiko_functions.send(shell, 'terminal length 0', ipaddr)

    myparamiko_functions.send(shell, 'config terminal')
    # myparamiko_functions.send(shell, 'snmp-server community ro 0 public')
    # myparamiko_functions.send(shell, 'snmp-server securityip 192.168.32.1')
    # myparamiko_functions.send(shell, 'ip default-gateway 192.168.32.1')
    myparamiko_functions.send(shell, 'snmp-server securityip 10.185.155.115')
    myparamiko_functions.send(shell, 'snmp-server securityip 10.185.155.75')
    myparamiko_functions.send(shell, 'snmp-server securityip 10.185.155.8')
    myparamiko_functions.send(shell, 'exit')
    myparamiko_functions.send(shell, 'write')
    myparamiko_functions.send(shell, 'Y')

    # output = myparamiko_functions.o_p(shell)
    # # print(output)
    # output_list = output.splitlines()
    # output_list = output_list[1:-1]
    # print(output_list)
    # output = '\n'.join(output_list)
    # print(output)

    # from datetime import datetime
    # now = datetime.now()
    # year = now.year
    # month = now.month
    # day = now.day
    # # hour = now.hour
    # # minute = now.minute
    #
    # file_name = f'{switch["ipaddr"]}_{year}-{month}-{day}.txt'
    # with open(file_name, 'w') as f:
    #     f.write(output)

    myparamiko_functions.close(client)

# creating a dictionary for each device to connect to


switch1 = {'ipaddr': '192.168.32.7', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
switch2 = {'ipaddr': '192.168.32.8', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch3 = {'ipaddr': '192.168.32.11', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch4 = {'ipaddr': '192.168.32.12', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch5 = {'ipaddr': '192.168.32.13', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch6 = {'ipaddr': '192.168.32.14', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch7 = {'ipaddr': '192.168.32.16', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch8 = {'ipaddr': '192.168.32.17', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch9 = {'ipaddr': '192.168.32.18', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch10 = {'ipaddr': '192.168.32.19', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch11 = {'ipaddr': '192.168.32.20', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch12 = {'ipaddr': '192.168.32.21', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch13 = {'ipaddr': '192.168.32.23', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch14 = {'ipaddr': '192.168.32.24', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch15 = {'ipaddr': '192.168.32.25', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
# switch16 = {'ipaddr': '192.168.32.27', 'portno': '22', 'user': 'admin', 'pswd': 'LP3238'}
#
#
# # creating a list of dictionaries (of devices)
# switches = [switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8, switch9, switch10, switch11,
#             switch12, switch13, switch14, switch15, switch16]
#
switches = [switch1, switch2]
#
# creating an empty list (it will store the threads)
threads = list()
for switch in switches:
    # creating a thread for each router that executes the backup function
    th = threading.Thread(target=backup, args=(switch,))  # args is a tuple hence the comma
    threads.append(th)  # appending the thread to the list
#
# starting the threads
for th in threads:
    th.start()

# waiting for the threads to finish
for th in threads:
    th.join()
