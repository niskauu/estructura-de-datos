#laboratorio-ej2
import random

filas= int(input("ingrese las filas de la matriz: "))
columnas= int(input("ingrese las columnas de la matriz: "))
escalar= int(input("ingrese el escalar por el cual desea multiplicar la matriz: "))

m=[]
for i in range(filas):
    aux=[]
    for j in range(columnas):
        aux.append(random.randint(0,10))
    m.append(aux)

print(f"la matriz resultante fue {m}")

for i in range(filas):
    for j in range(columnas):
        m[i][j]=m[i][j]*escalar
    
print(f"la matriz multiplicada por el escalar es: {m}")



        