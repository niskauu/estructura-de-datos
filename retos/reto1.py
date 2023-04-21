#reto en clase1
import random

a = [6,5,7]

#imprimir aleatorio
aux1=[]
for i in range(len(a)):
    aux=random.randrange(len(a))
    aux1.append(a[aux])
    a.remove(a[aux])
print(aux1)

#imprimir en descendente
aux2=[]
for i in range(len(a)):
    aux=0
    for j in range(len(a)):
        if a[i]>a[j+1]:
            aux=a[i]
    aux2.append(aux)

print(aux2)