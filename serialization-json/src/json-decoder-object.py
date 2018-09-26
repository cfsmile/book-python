import json


class Kontakt:
    def __init__(self, imie, nazwisko, telefon=None, adresy=(), data_urodzenia=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.adresy = adresy
        self.data_urodzenia = data_urodzenia

class Adres:
    def __init__(self, ulica=None, miasto=None, stan=None, kod=None, panstwo=None):
        self.ulica = ulica
        self.miasto = miasto
        self.kod = kod
        self.stan = stan
        self.panstwo = panstwo


ksiazka_adresowa = [
    Kontakt(imie='Matt', nazwisko='Kowalski', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
]


class JSONObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return obj.__dict__


class JSONObjectDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_object)

    def decode_object(self, dictionary):
        if dictionary.get('miasto'):
            return Adres(**dictionary)
        else:
            return Kontakt(**dictionary)
