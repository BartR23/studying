'''
Generowanie wszystkich kompozycji liczby n 
'''

from time import perf_counter


def Ostatnia(n, kompozycja):
    ostatnia = n*[1]
    ost = True
    if len(kompozycja) != len(ostatnia):
        ost = False
    else:
        for i in range(len(ostatnia)):
            if kompozycja[i] != ostatnia[i]:
                ost = False
                break
    return ost

def WszystkieKompozycjeAntyleks(n):

    kompozycja = [n]
    yield  tuple(kompozycja)
    
    while True:                               
        
        if kompozycja[-1] != 1:
            kompozycja[-1] -= 1
            kompozycja.append(1)
            yield  tuple(kompozycja)    
        else:
            z = len(kompozycja) - 1
            suma = 1
            for j in range(z,-1,-1):
                if kompozycja[j] > 1:
                    kompozycja[j] -= 1
                    for y in range(len(kompozycja)-1,j,-1):
                        suma += 1
                    kompozycja[j+1:] = [suma]
                    break
            yield  tuple(kompozycja)

        if Ostatnia(n, kompozycja) == True:
            break
     
#--------------------------------------------
n = 8

start = perf_counter()
Kompozycje = list( WszystkieKompozycjeAntyleks(n) )
stop  = perf_counter()

print("n =", n)
ilosc = len(Kompozycje)
print("Wygenerowano", ilosc, "kompozycji(e).")
print("Generowanie trwało:", stop-start, " sekund!") 
print("Średni czas generowania jednej kompozycji to", (stop-start)/ilosc*1000000, "mikrosekundy!")

if n<=8:
    for kompozycja in Kompozycje: print(kompozycja)
    

