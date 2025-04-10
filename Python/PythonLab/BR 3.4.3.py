# utworzenie słownika, w którym kluczem jest nazwa waluty,
#a wartością krotka złożona z kodu waluty oraz średniego
#jej kursu w PLN

waluty = dict()
waluty['dolar amerykański'] = ('1 USD', 3.9850)
waluty['dolar australijski'] = ('1 AUD', 2.6627)
waluty['dolar Hongkongu'] = ('1 HKD', 0.5101)
waluty['dolar kanadyjski'] = ('1 CAD', 2.9797)
waluty['euro'] = ('1 EUR', 4.3484)
waluty['frank szwajcarski'] = ('1 CHF', 4.6714)
waluty['funt szterling'] = ('1 GBP', 5.0440)
waluty['jen (Japonia)'] = ('1 JPY', 2.7443)
waluty['yuan renminbi (Chiny)'] = ('1 CNY', 0.5569)
print("Słownik walut - stan początkowy:\n", waluty, "\n")

# dodanie elementu
#waluty['peso chilijskie'] = ('100 CLP', 0.4483)
#peso = {"peso chilijskie": ('100 CLP', 0.4483)}
#waluty.update(peso)
#print("Słownik walut po dodaniu peso:\n", waluty, "\n")

# usuwanie elementu
del waluty['dolar australijski']
#print("Słownik walut po usunięciu dolara australijskiego:\n", waluty, "\n")

# wyświetlanie całego słownika
print("Słownik walut w kolumnie:")
for i in waluty:
    print(i, waluty[i])
print("")

# wyświetlanie tylko kluczy
#print("Klucze słownika walut:\n", waluty.keys(), "\n")
print("Klucze słownika walut:")
for i in waluty.keys():
    print(i)
print("")

# wyświetlanie tylko wartości
#print("Wartości słownika walut:\n", waluty.values(), "\n")
print("Wartości słownika walut:")
for i in waluty.values():
    print(i)
print("")

# liczba kluczy
print("Liczba kluczy:", len(waluty), "\n")

# modyfikowanie wybranych wartości
waluty['dolar kanadyjski'] = ('1 CAD', 2.7979)
print("Słownik walut po zmianie kursu dolara kanadyjskiego:")
for i in waluty:
    print(i, waluty[i])
print("")

# średni kurs wszystkich walut
suma = 0
for i in waluty.values():
    suma += i[1]
print("Średni kurs wszystkich walut wynosi:", suma/len(waluty), "\n")

# mediana, najtańsza, najdroższa
sorted = []
for i in waluty.values():
    sorted.append(i[1])
    sorted.sort()
#print(sorted)

for i in waluty:
    if waluty[i][1] == sorted[0]:
        print("Najtańsza waluta:", i, waluty[i])

for i in waluty:
    if waluty[i][1] == sorted[len(waluty) - 1]:
        print("Najdroższa waluta:", i, waluty[i])

if len(sorted)%2 == 1:
    indexM = len(sorted)//2 - 1
    print("Mediana kursów walut wynosi:", sorted[indexM])
elif len(sorted)%2 == 0:
    indexM1 = int(len(sorted)/2)
    indexM2 = int(len(sorted)/2 + 1)
    mediana = (sorted[indexM1] + sorted[indexM2])/2
    print("Mediana kursów walut wynosi:", mediana) 

# waluty posortowane rosnąco
print("\nPosortowane rosnąco kursy walut:")
for i in sorted:
    for key, value in waluty.items():
        if i == waluty[key][1]:
            print(key, value)
    
