'''
Generowanie wszystkich wariacji k-elemenetowych zbioru n-elementowego
'''

from time import perf_counter

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

def WszystkieWariacjeBezPowtórzenProsty(k, n):                                                          # k musi być mniejsze lub równe n i większe od zera!

    if k < 1 or k > n:
        raise  ValueError("Liczba k nie może być większa od n ani mniejsza od 1!  k =",k, "n =", n)
            
    lista = list( range(1,k+1) )   
    yield  tuple(lista)  
    lista.extend( list(range(k+1,n+1)) )                                                                
    liczba_wariacji = silnia(n)/silnia(n-k)
    nr=1;
    
    while nr < liczba_wariacji: 

        for i in range(k-1, -1, -1):
            prawa = lista[i+1: ]
            wieksze = []
            
            for j in range( len(list(prawa)) ):
                if lista[i]<prawa[j]:
                    wieksze.append(prawa[j])
            
            if len(list(wieksze)) != 0:
                wieksze.sort()
                prawa.append(lista[i])
                lista[i] = wieksze[0]
                prawa.remove(wieksze[0])
                prawa.sort()
                lista[i+1:] = prawa
                break
            
        yield  tuple( lista[0:k] )
        nr+=1
        
#--------------------------------------------------------------------
#k = 6;  n = 10;
k = 8;  n = 12;
#k = 4;  n = 6;

start = perf_counter()
Wariacje = WszystkieWariacjeBezPowtórzenProsty(k, n)
Wariacje = list(Wariacje)
stop  = perf_counter()

print("Liczba wariacji bez powtórzeń dla k =", k,"i n =",n,"to", len(Wariacje))
print("Generowanie trwało: ", stop - start, "sekund!") 
print("Średni czas generowania jednej wariacji to", (stop-start)/len(Wariacje)*1000000, "mikrosekund!")
#print (Wariacje)
#if n <= 6:
    #for i, wariacja in enumerate(Wariacje): print(i+1, wariacja)
