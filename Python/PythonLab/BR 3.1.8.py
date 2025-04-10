#program tworzy NxN-elementową zagnieżdżoną listę
#o elementach całkowitych imitujących Macierz kwadratową

import random
A = []
n = int(input("Podaj rozmiar macierzy n = "))

# a) wypełnienie tablicy losowymi danymi z zakresu -10 : +10
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(-10,10))
    A.append(row)

# b) wyświetlenie tablicy w formie macierzy
print("Macierz A:")
for i in range(n): 
    print(A[i])

# c) wyświetlenie tylko pierwszej kolumny
print("Pierwsza kolumna macierzy:")
for i in range(n):
    print(A[i][0])

# d) średnia ujemnych/dodatnich elementów macierzy
sumaU = 0
licznikU = 0
for i in range(n):
    for j in range(n):
        if A[i][j] < 0:
            sumaU += A[i][j]
            licznikU += 1
print("Średnia liczb ujemnych:", sumaU/licznikU)

sumaD = 0
licznikD = 0
for i in range(n):
    for j in range(n):
        if A[i][j] > 0:
            sumaD += A[i][j]
            licznikD += 1
print("Średnia liczb dodatnich:", sumaD/licznikD)

# e) suma elementów na przekątnej
sumaP = 0
for i in range(n):
    for j in range(n):
        if i==j:
            sumaP += A[i][j]
print("Suma elementów na przekątnej:", sumaP)

# f) suma elementów z wyłączeniem obwodu
sumaS = 0
for i in range(1,n-1):
    for j in range(1,n-1):
        sumaS += A[i][j]
print("Suma z wyłączeniem elementów na obwodzie:", sumaS)

# g) wyznaczenie minimum każdej kolumny
for i in range(n):
    mincolumn = A[0][i]
    for j in range(1,n):
        if A[j][i] < mincolumn:
            mincolumn = A[j][i]
    print("Minimalna wartość kolumny",i+1,"wynosi",mincolumn)

# h) suma liczb dodatnich nieparzystych na nieparzystych pozycjach w macierzy
sumaND = 0
if n%2 == 0:
    for i in range(n):
        for j in range(0,n,2):
            if (A[i][j]%2 != 0) and (A[i][j]>0):
                sumaND += A[i][j]
if n%2 != 0:
    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 0:
                if (A[i][j]%2 != 0) and (A[i][j]>0):
                    sumaND += A[i][j]
print("Suma liczba dodatnich nieparzystych na nieparzystych pozycjach macierzy:", sumaND)

# i)  ilość liczb z przedziału <1,9> w parzystych wierszach
licznikL = 0
for i in range(1,n,2):
    for j in range(n):
        if A[i][j]>=1 and A[i][j]<=9:
            licznikL += 1
print("Ilość liczb z przedziału <1,9> w parzystych wierszach:", licznikL)
