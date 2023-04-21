#reto en clase1
import random

a = [6,5,7,9]

for i in range(len(a)):
    print(a[i])

#imprimir aleatorio
for i in range(len(a)):
    aux=random.randrange(len(a))
    print(a[aux])
    a.remove(a[aux])