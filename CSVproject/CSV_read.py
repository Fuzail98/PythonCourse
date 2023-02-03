import csv
with open('abc.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    year_1958 = dict()
    for row in reader:
        #print(row)
        year_1958[row[0]] = row[1]
    #print('\n')
    print(year_1958)
    #print('\n')
    max_1958 = max(year_1958.values())
    #print(max_1958)

    for k, v in year_1958.items():
        if max_1958 == v:
            print(f'Busiest month is {k} with flights {v.strip()}.')
        #print('\n')
        #print(f'{k}, {v}')