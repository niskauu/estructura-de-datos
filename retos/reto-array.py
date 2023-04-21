from array import array
import random

arreglo = array('i',[])
aux1= random.randint(10,30)

for i in range(aux1):
    aux2=random.randint(0,10)
    arreglo.extend([aux2])
    
print(arreglo)

buscar = int(input("ingrese el elemento que desea buscar: "))

aux3=[]
for i in range(len(arreglo)):
    if arreglo[i]==buscar:
        aux3.append(i)

if len(aux3)>0: 
    print(f"el elemento se encuentra en las posiciones {aux3}")
elif len(aux3)==0:
    print("el elemento no se encuentra")
