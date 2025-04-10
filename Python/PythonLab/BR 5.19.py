'''
Program transformacji macierzy kwadratowej za
pisanej w  pliku wm1.txt do pliku wt1.txt.
Macierz zawiera liczby całkowite, ale nieznana
jest jej liczba wierszy (i liczba kolumn).
Program wyświetla na ekranie odczytaną macierz,
oblicza średnią arytmetyczną jej elementów, 
oblicza ślad macierzy, czyli sumę elementów na
jej głównej przekątnej. Rozstrzyga, czy macierz
jest symetryczna względem głównej przekątnej
i czy jest symetryczna względem drugiej przekątnej.
Wszystkie wyniki zapisywane są do pliku.
Do innego pliku wynikowego zapisywana jest 
macierz wejściowa obrócona o 90 stopni w lewo, o 90 
stopni w prawo, obrócona o 180 stopni, symetrycznie
odbita względem prostej pionowej, symetrycznie
odbita względem prostej poziomej.
'''

plik1=open('wm1.txt', 'r')
plik2=open('wt1.txt', 'w')
plik3=open('wt2.txt', 'w')
macierz=[]

for w in plik1:
    w=w.strip().split()
    wiersz=[]
    for el in w:
        el=int(el)
        wiersz.append(el)
    macierz.append(wiersz)
 
for w in macierz:
    print(w)

#średnia arytmetyczna elementów
suma=0
for w in macierz:
    for i in w:
        suma+=i
#print(suma)

#suma elementów na głównej przekątnej
slad=0
for x in range(len(macierz)):
    for y in range(len(macierz[x])):
        if x==y:
            slad+=macierz[x][y]
#print(slad)

#czy symetryczna 1
licznik1=0
for x in range(len(macierz)):
    for y in range(len(macierz[x])):
        if macierz[x][y] != macierz[y][x]:
            licznik1+=1
if licznik1 != 0:
    sym1='Niesymetryczna względem głównej przekątnej'
else:
    sym1='Symetryczna względem głównej przekątnej'

#czy symetryczna 2
licznik2=0
for x in range(len(macierz)):
    for y in range(len(macierz)):
        if macierz[x][y] != macierz[len(macierz)-1-y][len(macierz)-1-x]:
            licznik2+=1
if licznik2 != 0:
    sym2='Niesymetryczna względem drugiej przekątnej'
else:
    sym2='Symetryczna względem drugiej przekątnej'

#zapisy do pliku2
plik2.write('Macierz:\n')
for w in macierz:
    plik2.write(str(w)+'\n')
plik2.write('Średnia arytmetyczna elementów: '+str(suma)+'\n')
plik2.write('Ślad macierzy: '+str(slad)+'\n')
plik2.write(sym1+'\n')
plik2.write(sym2+'\n')

#obrót o 90 w lewo 
macierz90L=[]
for x in range(len(macierz)-1, -1, -1):
    wiersz=[]
    for y in range(len(macierz)):
        wiersz.append(macierz[y][x])
    macierz90L.append(wiersz)
#for w in macierz90L:
    #print(w)

#obrót o 90 w prawo 
macierz90P=[]
for x in range(len(macierz)):
    wiersz=[]
    for y in range(len(macierz)-1, -1, -1):
        wiersz.append(macierz[y][x])
    macierz90P.append(wiersz)
#for w in macierz90P:
    #print(w)

#obrót o 180
macierz180=[]
for x in range(len(macierz)-1, -1, -1):
    wiersz=[]
    for y in range(len(macierz)-1, -1, -1):
        wiersz.append(macierz[x][y])
    macierz180.append(wiersz)
#for w in macierz180:
    #print(w)

#odbicie wg pionowej
macierzOpion=[]
for x in range(len(macierz)):
    wiersz=[]
    for y in range(len(macierz)-1, -1, -1):
        wiersz.append(macierz[x][y])
    macierzOpion.append(wiersz)
#for w in macierzOpion:
    #print(w)

#odbicie wg poziomej
macierzOpoziom=[]
for x in range(len(macierz)-1, -1, -1):
    wiersz=[]
    for y in range(len(macierz)):
        wiersz.append(macierz[x][y])
    macierzOpoziom.append(wiersz)
#for w in macierzOpoziom:
    #print(w)

#zapisy do pliku3
plik3.write('Macierz:\n')
for w in macierz:
    plik3.write(str(w)+'\n')
plik3.write('Macierz obrócona o 90st w lewo:\n')
for w in macierz90L:
    plik3.write(str(w)+'\n')
plik3.write('Macierz obrócona o 90st w prawo:\n')
for w in macierz90P:
    plik3.write(str(w)+'\n')
plik3.write('Macierz obrócona o 180st:\n')
for w in macierz180:
    plik3.write(str(w)+'\n')
plik3.write('Macierz odbita symetrycznie wg prostej pionowej:\n')
for w in macierzOpion:
    plik3.write(str(w)+'\n')
plik3.write('Macierz odbita symetrycznie wg prostej poziomej:\n')
for w in macierzOpoziom:
    plik3.write(str(w)+'\n')

plik1.close()
plik2.close()
plik3.close()
