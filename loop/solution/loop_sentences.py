TEXT = 'We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win'

wynik = list()

for sentence in TEXT.split('.'):
    sentence = sentence.strip()
    words = sentence.split(' ')
    count = len(words)
    wynik.append({sentence: count})

from pprint import pprint
pprint(wynik)
