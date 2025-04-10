# program zwraca łańcuch unikalnych liter występujących w podanym wyrazie

#import random
word = input("Podaj słowo minimum 10-literowe:")
if len(word) < 10:
    print("Słowo jest za krótkie!")
else:
    string = ""
    for i in set(word):
        string = string + i
    print(string)

