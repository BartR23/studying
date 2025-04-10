'''
Generowanie wszystkich podzbiorów zbioru n-elementowego
'''

import time
from time import perf_counter

def WszystkiePodzbiory(n):
    kombinacja = list(range(1,n+1))
    yield tuple ( kombinacja )
    
    while kombinacja != []:
        if kombinacja[-1] == n:
            kombinacja.pop()                                             
        else:
            ostatnia = kombinacja.pop() + 1                                     
            kombinacja.extend(list(range(ostatnia,n+1)))
        yield tuple ( kombinacja )
 
#--------------------------------------------------------
n = 8

start = perf_counter()
Podzbiory = list(WszystkiePodzbiory(n))
stop  = perf_counter()

print( "Liczba podzbiorów =", len(Podzbiory) )
print( "Generowanie trwało:", stop-start, " sekund!") 
print( "Średni czas generowania jednego podzbioru =", (stop-start)*1000000/len(Podzbiory), "mikrosekudy!")

for podzbior in Podzbiory: print(podzbior)

#print(Podzbiory)


