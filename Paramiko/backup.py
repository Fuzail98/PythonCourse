import myparamiko_functions

switch7028 = {'ipaddr': '10.0.0.2', 'portno': '22', 'user': 'admin', 'pswd': 'admin'}
switch6012 = {'ipaddr': '10.0.0.3', 'portno': '22', 'user': 'admin', 'pswd': 'admin'}


switches = [switch7028, switch6012]

for switch in switches:
    client = myparamiko_functions.connect(**switch)
    shell = myparamiko_functions.invoke(client)

    myparamiko_functions.send(shell, 'en')
    myparamiko_functions.send(shell, 'terminal length 0')
    myparamiko_functions.o_p(shell)
    myparamiko_functions.send(shell, 'show running-config')

    output = myparamiko_functions.o_p(shell)
    print(output)

    myparamiko_functions.close(client)

    output_list = output.splitlines()
    output_list = output_list[1:-1]
    output = '\n'.join(output_list)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    # hour = now.hour
    # minute = now.minute

    file_name = f'{switch["ipaddr"]}_{year}-{month}-{day}.txt'
    # print(file_name)

    with open(file_name, 'w') as f:
        f.write(output)

# This script will iterate and get executed for one device at a time. That is a lot of time for a company with
# 100s of devices. So we have a concept of multi-threading. See multithreading.py in this same directory.
# Multithreading will execute commands for each device simultaneously.
