import csv
import json

with open('devices.csv') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    ICCN_Switches = {}
    for row in reader:
        switch = {'ipaddr': row[1], 'port': 22, 'usr': row[2], 'pswd': row[3]}
        tmp = {}
        for switch_version in [row[0]]:
            tmp["switch_%s" % switch_version] = switch
            ICCN_Switches.update(tmp)

with open('test.json', 'w') as f:
    json.dump(ICCN_Switches, f)
with open('test.json') as f:
    data = json.load(f)
print(data)

