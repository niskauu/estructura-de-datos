#laboratorio-ej1
import random

filas= int(input("ingrese las filas de la primera y segunda matriz: "))
columnas= int(input("ingrese las columnas de la primera y segunda matriz: "))

m1=[]
for i in range(filas):
    aux=[]
    for j in range(columnas):
        aux.append(random.randint(0,5))
    m1.append(aux)
    
m2=[]
for i in range(filas):
    aux=[]
    for j in range(columnas):
        aux.append(random.randint(0,5))
    m2.append(aux)

print(f"la primera matriz es: {m1}")
print(f"la segunda matriz es: {m2}")

mr=[]
for i in range(filas):
    aux=[]
    for j in range(columnas):
        aux.append((m1[i][j])+(m2[i][j]))
    mr.append(aux)
    
print(f"la suma resultante entre las matrices es: {mr}")

filas3= int(input("ingrese las filas de la tercera matriz: "))
columnas3= int(input("ingrese las columnas de la tercera matriz: "))

m3=[]
for i in range(filas3):
    aux=[]
    for j in range(columnas3):
        aux.append(random.randint(0,5))
    m3.append(aux)

print(f"la tercera matriz es: {m3}")

if filas3 == filas and columnas3==columnas:
    for i in range(filas):
        for j in range(columnas):
            mr[i][j]=(mr[i][j])-(m3[i][j])
    print(f"la resta resultante es: {mr}")
else:
    print("la tercera matriz no es posible sumarla por tener distintas dimensiones a las otras matrices")