#  funkcja  na obliczanie sumy szeregu dla podanego n (max składnik  licznika)
#  π/2 = (2x2x4x4x6x6...)/(1x3x3x5x5...)

def szereg(n):
    suma = 1
    elementy = []
    a=0
    b=1

    for i in range(0,n):
        if i%2 == 0:
            a+=2
            b=b
            el_1 = a/b
            elementy.append(el_1)
        elif i%2==1:
            a=a
            b+=2
            el_2 = a/b
            elementy.append(el_2)
    #print(elementy)

    for x in elementy:
        suma=suma*x
    return suma

print(szereg(1))
print(szereg(2))
print(szereg(3))
print(szereg(4))
print(szereg(5))
print(szereg(6))
print(szereg(7))
print(szereg(8))
        
