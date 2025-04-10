#program losuje n liczb do  dwóch list A i B (elementy typu całkowitego)

import random

def listy(n):
    A=[]
    B=[]
    for i in range(n):
        a = random.randint(-10, 10)
        A.append(a)
    for j in range(n):
        b = random.randint(-10, 10)
        B.append(b)
    print(A, B)

    #a  dodawanie elementów z obu list, wynikiem jest lista
    listaA=[]
    for i in range(n):
        s = A[i] + B[i]
        listaA.append(s)
    print("Suma:",listaA)

    #b mnożenie elementów z obu list, wynikiem jest lista
    listaB=[]
    for i in range(n):
        m = A[i] * B[i]
        listaB.append(m)
    print("Mnożenie:",listaB)

    #c potęgowanie elementów z listy A przez elementy listy B,
    # wynikiem jest lista
    listaC=[]
    for i in range(n):
        p = A[i] ** B[i]
        listaC.append(p)
    print("Potęgowanie:",listaC)

    #d  obliczanie iloczynu kartezjańskiego dwóch list (tablic),
    # funkcja zwraca liczbę
    listaD=[]
    for i in range(n):
        for j in range(n):
            para = (A[i], B[j])
            listaD.append(para)
    print('Iloczyn kartezjański:',listaD)

listy(3)
print('\n')
listy(4)
print('\n')
listy(6)
