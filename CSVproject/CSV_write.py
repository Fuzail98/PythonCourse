import csv
with open ('numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Number', '   Square', '    Cube', '   Power4'])
    for x in range(1,101):
        writer.writerow([x, x**2, x**3, x**4])