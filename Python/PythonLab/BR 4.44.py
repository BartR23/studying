# funkcja, dla dowolnej liczby zbiorów, podawanych jako kolejne
# argumenty tej funkcji oddzielane przecinkiem, wyznacza iloczyn
# kartezjański tych zbiorów i wynik zwraca w postaci listy krotek

def iloczyn(*Listy):
    wynik=[[]]
    if len(Listy) < 2:
        print("Za mało argumentów.")
    else:
        for lista in Listy:
            wynik = [x + [y] for x in wynik for y in lista]
        krotki=[]
        for lista in wynik:
            krotka = tuple(lista)
            krotki.append(krotka)
        print(krotki)
            
A=[1,2,3]
B=['a','b','c','d']
C=[5,6,7,8]
D=['x','y','z']
W=[1,2]
X=['a','b']
Y=[8,9]
Z=['x','y']

#iloczyn(A,B)
#iloczyn(A,B,C)
iloczyn(A,B,C,D)
#iloczyn(W,X,Y,Z)
#iloczyn(A)

