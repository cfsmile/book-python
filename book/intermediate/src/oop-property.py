class Astronaut:
    def __init__(self):
        self._name = None

    @property
    def name(self):
        print(f'My name {self._name}')
        return self._name

    @name.setter
    def name(self, value):
        print(f'Changing "name" from {self._name} to {value}')
        self._name = value

    @name.deleter
    def name(self):
        raise PermissionError(f'You do not have permission to do that!')
        del self._name


jose = Astronaut()
jose.name = 'Jose Jimenez'  # Changing "name" from None to Jose Jimenez
print(jose.name)  # My name Jose Jimenez
# Jose Jimenez