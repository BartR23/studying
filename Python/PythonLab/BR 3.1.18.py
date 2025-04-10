#program tworzy n-elementową listę składającą się z <1-x> znakowych ciągów

import random
Lista = []
n = int(input("Podaj liczbę elementów listy n = "))
x = int(input("Podaj maksymalną liczbę znaków łańcucha x = "))

for i in range(n):
    element = []
    qtyOfChar = random.randint(1,x)
    for j in range(qtyOfChar):
        a = random.randint(97,122)
        char = chr(a)
        element.append(char)
    Lista.append(''.join(element))
print(Lista)
    
# a) sprawdzenie,  ile liter ‘k’ zawiera lista
liczniK = 0
for i in range(n):
    for j in range(len(Lista[i])):
        if Lista[i][j] == "k":
            liczniK += 1
print("Liczba liter 'k' występujących w liście:", liczniK)

# b) sprawdzenie, ile ciągów znaków: ‘ak’ zawiera lista
licznikAK = 0
for i in range(n):
    for j in range(len(Lista[i]) - 1):
        if Lista[i][j] == "a" and Lista[i][j+1] == "k":
            licznikAK += 1
print("Liczba ciągów 'ak' występujących w liście:", licznikAK)

# c) wypisanie tylko dwuliterowych słów
lista2 = []
for i in range(n):
    if len(Lista[i]) == 2:
        lista2.append(Lista[i])
print("Słowa dwuliterowe:", lista2)

# d) sprawdzenie,  ile ciągów znaków dłuższych niż k zawiera lista
k = int(input("Aby sprawdzić ile ciągów znaków dłuższych niż k zawiera lista, podaj k = "))
licznikK = 0
for i in range(n):
    if len(Lista[i]) > k:
        licznikK += 1
print("Liczba słów dłuższych niż", k, "wynosi:", licznikK)

# e) dodanie na początku każdego elementu listy litery a, a na końcu litery z
for i in range(n):
    Lista[i] = "a" + Lista[i] + "z"
print("Lista po dodaniu a/z na początku/końcu każdego elementu:", Lista)
