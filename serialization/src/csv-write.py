import csv

DATA = [
    {'first_name': 'José', 'last_name': 'Jiménez'},
    {'first_name': 'Mark', 'last_name': 'Watney'},
    {'first_name': 'Иван', 'last_name': 'Иванович'},
    {'first_name': 'Alex', 'last_name': 'Vogel'},
]


with open(r'filename.csv', mode='w') as file:
    writer = csv.DictWriter(
        f=file,
        fieldnames=['first_name', 'last_name'],
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()

    for row in DATA:
        writer.writerow(row)
