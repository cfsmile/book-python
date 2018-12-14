import csv

DATA = [
    {'first_name': 'José'},
    {'last_name': 'Jiménez'},
    {'first_name': 'Иван', 'last_name': 'Иванович'},
    {'first_name': 'Mark', 'last_name': 'Watney', 'born': 1961},
    {'first_name': 'José', 'born': 1961, 'first_step': 1969},
]

fieldnames = set()

for row in DATA:
    fieldnames.update(row.keys())


with open(r'../data/iris.csv', mode='w') as file:
    writer = csv.DictWriter(
        f=file,
        fieldnames=fieldnames,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in DATA:
        writer.writerow(row)
