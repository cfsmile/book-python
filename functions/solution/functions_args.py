# https://raw.githubusercontent.com/AstroMatt/book-python/master/database/data/iris.csv


def print_iris(sepal_length, sepal_width, *args, **kwargs):
    print(locals())


with open(r'../data/iris.csv') as file:

    # skip first line in file
    file.readline()

    for line in file.readlines():
        *features, labels = line.strip().split(',')

        d = {'species': labels}
        print_iris(*features, **d)
