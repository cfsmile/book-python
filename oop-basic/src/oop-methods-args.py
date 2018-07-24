class Astronaut:
    name = 'José Jiménez'

    def say_hello(self, text='¡Hola'):
        print(f'{text} {self.name}!')


jose = Astronaut()

jose.say_hello()
# ¡Hola José Jiménez!

jose.say_hello('My name')
# My name José Jiménez!
