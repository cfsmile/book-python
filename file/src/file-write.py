FILENAME = r'C:\Temp\bootfilure.txt'


with open(FILENAME, mode='w', encoding='utf-8') as file:
    file.write(':)')


with open(FILENAME, mode='a', encoding='utf-8') as file:
    file.write(':)')
