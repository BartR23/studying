'''
Generowanie kombinacji k-elementowych zbioru n-elementowego na podstawie jej numeru porządkowego.
'''

from  time  import  perf_counter

def WyznaczLiczbyWystępująceNaKolejnychPozycjachWKombinacji(n, k):

    liczba_wierszy = n-k+1
    liczby = [ list( range(i+1, k+i+1) )  for i in range(liczba_wierszy) ]
    return(liczby)

def ObliczWartosciDwumianówJakoSumyIWygenerujKombinacje(n, k):
    
    liczba_wierszy = n-k+1
    sumy = [ k*[1]  for _ in range(liczba_wierszy) ]

    for j in range (k-2, -1, -1):
        for i in range (n-k-1, -1, -1):
            sumy[i][j] = sumy[i+1][j] + sumy[i][j+1]

    for wiersze in sumy:
        print(wiersze)
     
    n_nad_k = (sumy[0][0]*n)//k
    kombinacja = k*[0]
    liczby =  WyznaczLiczbyWystępująceNaKolejnychPozycjachWKombinacji(n, k)
    
    for nr in range(n_nad_k):
        
        koniec = False;
        wier = 0; kol = 0; x = 0;

        while not koniec:
            if nr >= sumy[wier][kol]:
                nr = nr - sumy[wier][kol]
                wier += 1
            else:
                kombinacja[x] = liczby[wier][kol]
                x += 1
                if kol < k-1:
                    kol += 1
                else:
                    koniec = True
                    
        yield  tuple( kombinacja )


n = 24;  k = 12;
#n = 15;  k = 8;
#n = 8;  k = 5;
#n = 6; k = 4;
#n = 9; k = 6;

liczby =  WyznaczLiczbyWystępująceNaKolejnychPozycjachWKombinacji(n, k)

for lista in liczby:
    print(lista)

print("------------------------------------------------------")

start = perf_counter()

Kombinacje = list( ObliczWartosciDwumianówJakoSumyIWygenerujKombinacje(n, k) )

stop  = perf_counter()

ile = len(Kombinacje)

print("n =", n, " k =", k)
print("Liczba kombinacji bez powtórzeń:", ile)
print("Generowanie trwało:", stop - start, "sekund!")
print("Średni czas generowania jednej kombinacji:", (stop - start) / ile * 1000000, "mikrosekundy!" )
print("Średnia szybkość generowania kombinacji  :", int( ile / (stop - start) ), "kombinacji na sekundę!" )

#if ile <= 126:
    #print(Kombinacje)
    #for k in Kombinacje:
        #print(nr, k)
        #nr=nr+1
