import csv

FILENAME = r'filename.csv'
"""
    "first_name", "last_name"
    "José", "Jiménez"
    "Max", "Peck"
    "Ivan", "Иванович"
"""


with open(FILENAME, encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=',', quotechar='"')

    for row in data:
        print(row['first_name'], row['last_name'])
