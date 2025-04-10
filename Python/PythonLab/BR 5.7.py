# Program czyta wiersze pliku tekstowego we7.txt.
# Za każdym razem po napotkaniu wiersza, którego
# pierwszym znakiem jest 'A'..'Z' rozpoczyna łączenie
# (sklejanie) kolejnych wierszy, rozdzielając je spacją.
# Sklejony wiersz jest zapisywany do pliku wy7.txt,
# przy czym na początku w nawiasach jest wypisywana
# jego ilość znaków.

plik1=open('we7.txt', 'r')
plik2=open('wy7.txt', 'w')
checkList=[]
tabWE=[]

for wiersz in plik1:
    if wiersz[-1] == '\n':
        wiersz = wiersz[:len(wiersz)-1]
    else:
        wiersz = wiersz
    tabWE.append(wiersz)
for w in tabWE:
    if w[0] >= 'A' and w[0] <= 'Z':
        lanTym = w
        tabTym = []
        for i in range(tabWE.index(w)+1, len(tabWE)):
            tabTym.append(tabWE[i])
        for wNext in tabTym:
            if wNext[0] >= 'A' and wNext[0] <= 'Z':
                break
            else:
                lanTym = lanTym+' '+wNext
        plik2.write('('+str(len(lanTym))+')'+lanTym+'\n')

plik1.close()
plik2.close()
