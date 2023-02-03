import json

with open ('config.txt') as f:
    reader = f.read()
    # print(reader)

with open('config.json', 'w') as f:
    json.dump(reader, f)
with open('config.json') as f:
    data = json.load(f)
print(data)