FILENAME = input('Podaj nazwę pliku: ')


try:
    with open(FILENAME, mode='w', encoding='utf-8') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File does not exists')

except PermissionError:
    print('Brak uprawnien')
