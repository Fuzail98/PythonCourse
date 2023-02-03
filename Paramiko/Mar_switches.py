import myparamiko_functions
# import threading


def configure(switch):
    client = myparamiko_functions.connect(**switch)
    shell = myparamiko_functions.invoke(client)

    myparamiko_functions.send(shell, 'terminal length 0')
    myparamiko_functions.send(shell, 'show version')  # this is the enable command

    output = myparamiko_functions.o_p(shell)
    # print(output)
    output_list = output.splitlines()
    # print(output_list)
    output_list = output_list[6:13]
    print(output_list)
    output = '\n'.join(output_list)
    print(output)

    # from datetime import datetime
    # now = datetime.now()
    # year = now.year
    # month = now.month
    # day = now.day
    # hour = now.hour
    # minute = now.minute

    # file_name = f'{switch["ipaddr"]}_{year}-{month}-{day}.txt'
    # with open(file_name, 'w') as f:
    #     f.write(output)

    myparamiko_functions.close(client)

# creating a dictionary for each device to connect to


switch7028 = {'ipaddr': '10.0.0.6', 'portno': '22', 'user': 'admin', 'pswd': 'admin'}
configure(switch7028)
#switch6012 = {'ipaddr': '10.0.0.3', 'portno': '22', 'user': 'admin', 'pswd': 'admin'}

# creating a list of dictionaries (of devices)
#switches = [switch7028, switch6012]

# creating an empty list (it will store the threads)
# threads = list()
# for switch in switches:
#     # creating a thread for each router that executes the backup function
#     th = threading.Thread(target=configure, args=(switch,))  # args is a tuple hence the comma
#     threads.append(th)  # appending the thread to the list
#
# # starting the threads
# for th in threads:
#     th.start()

# waiting for the threads to finish
# for th in threads:
#     th.join()


