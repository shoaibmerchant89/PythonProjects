lines = []

with open('config.txt') as f:
    for line in f:
        lines.append(line)
print(lines)

with open('config.txt') as f:
    print(f.read().splitlines(keepends=False))

with open('config.txt') as f:
    print(f.readlines())

#------------WRITING TO TEXT FILES----------------


#with open('file1.txt', 'a+') as f1:
#    f1.write('\nAppended content2')
#    f1.seek(0)
#    print(f1.read())

#------------WRITING TO CSV FILES----------------

import csv

with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
#    next(reader)
    data = {}
    months = {}
    columns = []
    for row in reader:
        if 'Month' in row:
            row.pop(0)
            years = row
        else:
            months[row[0]] = row[1]

#        else:

#            months[row[0]] = ''
#            col1 = [row[1]]
#            col2 = [row[2]]
#            col3 = [row[3]]
    for y in years:
        data[y] = months
    print(data)

with open('airtravel.csv', 'r+') as f:
    reader = csv.reader(f)
    next(reader)
    year_1958 = {}
    for row in reader:
        year_1958[row[0]] = row[1]

    max_1958 = max(year_1958.values())

    for k, v in year_1958.items():
        if v == max_1958:
            print(f'Busiest Month in 1958:{k}, Flights:{v}')

#with open('airtravel.csv', 'a+') as csvfile:
#    writer = csv.field_size_limit(2)
#    writer = csv.writer(csvfile, delimiter=',')
#    writer.writerow(('TOTAL',1000,2000,3000))

with open('testcsv.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1,101):
        writer.writerow([x, x**2, x**3, x**4])

#with open('airtravel.csv', 'r+') as f:
#    data = {}
#    dictreader = csv.DictReader(f)
#    for row in dictreader:
#        print(row)

# with open('passwd.csv', 'r+') as f:
#     reader = csv.reader(f, delimiter=':', lineterminator='\n')
#     for row in reader:
#         print(row)
#
# print(csv.list_dialects())

csv.register_dialect('hashes', delimiter='#', lineterminator='\n', quoting=csv.QUOTE_NONE)

with open('items.csv', 'r+') as f:
    reader = csv.reader(f, dialect='hashes')
    for row in reader:
        print(row)

with open('items.csv', 'a+', newline='') as f:
    writer = csv.writer(f, dialect='hashes')
    writer.writerow(['shoes',10,5.5])

with open('devices.txt', 'r+') as f:
    parent = []
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        parent.append(row)
    print(parent)