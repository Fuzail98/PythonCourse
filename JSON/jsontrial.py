import json
import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/users')

users = json.loads(response.text)
# opening the csv file for writing
with open('users.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # write a header to file
    writer.writerow(("Name", "City", "GPS", "Company"))

    # iterating over the users list
    for user in users:
        # getting the data from the dictionary
        name = user['name']
        city = user['address']['city']
        lat = user['address']['geo']['lat']
        lng = user['address']['geo']['lng']
        # constructing the GPS coordinates in form of (lat, lng)
        geo = f'({lat},{lng})'
        company_name = user['company']['name']

        # writing to csv file
        csv_data = (name, city, geo, company_name)
        writer.writerow(csv_data)

"""
def serialize(f_name, pyt_obj, srlzn_prot):
    srlzn_prot = input('Enter JSON / Pickle: ')
    if srlzn_prot == 'JSON':
        import json
        with open(f_name, 'w') as f:
            json.dump(pyt_obj, f)

    elif srlzn_prot == 'Pickle':
        import pickle
        with open(f_name, 'wb') as f:
            pickle.dump(pyt_obj, f)
    else:
        print('Invalid choice!')

def deserialize(f_name, srlzn_prot):
    if srlzn_prot == 'JSON':
        import json
        with open(f_name, 'r') as f:
            obj = json.load(f)
        return obj

    elif srlzn_prot == 'Pickle':
        import pickle
        with open(f_name, 'rb') as f:
            obj = pickle.load(f)
        return obj
    else:
        print('Invalid choice!')

d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}
serialize('jsonass.json', d1, 'JSON')

mydict1 = deserialize('jsonass.json', 'JSON')
print(mydict1)

serialize('jsonass.dat', d1, 'Pickle')
mydict2 = deserialize('jsonass.dat', 'Pickle')
print(mydict2)
"""