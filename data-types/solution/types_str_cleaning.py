a = 'Jana III Sobieskiego 1 apt 2'
b = 'ul Jana III SobIESkiego 1/2'
c = 'ul. Jana trzeciego Sobieskiego 1/2'
d = 'ul.Jana III Sobieskiego 1/2'
e = 'ulicaJana III Sobieskiego 1/2'
F = 'UL. JANA 3 SOBIESKIEGO 1/2'
G = 'UL. III SOBiesKIEGO 1/2'
H = 'ULICA JANA III SOBIESKIEGO 1/2'
I = 'ULICA. JANA III SOBI'
j = ' Jana 3 Sobieskiego 1/2 '
k = 'Jana III Sobieskiego 1 m. 2'


a = a.replace(' 1 apt 2', '')
b = b.replace('ul ', '').replace(' 1/2', '').title().replace('Iii', 'III')
c = c.replace('trzeciego', 'III').replace(' 1/2', '').replace('ul. ', '')
d = d.replace('ul.', '').replace(' 1/2', '')
e = e.replace('ulica', '').replace(' 1/2', '')

from pprint import pprint
pprint(locals())
