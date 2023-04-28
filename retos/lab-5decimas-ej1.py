#Niska Silva
#Ignacio Vega

import numpy as np

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m1 = np.ones((filas,columnas))
for i in range(filas):
    for j in range(columnas):
        m1[i][j] = int(input(f"Ingrese el elemento de la fila {i+1}, columna {j+1}: "))
m2 = np.ones((filas,columnas))
for i in range(filas):
    for j in range(columnas):
        m2[i][j] = int(input(f"Ingrese el elemento de la fila {i+1}, columna {j+1}: "))

def sumaMatrices(x,y):
    return np.add(x,y)

def restaMatrices(x,y):
    return np.subtract(x,y)

print(f"\nLa primera matriz sera:\n {m1}")
print(f"\nLa segunda matriz sera:\n {m2}")
print(f"\nLa suma es: \n{sumaMatrices(m1,m2)}")
print(f"\nLa resta es: \n{restaMatrices(m1,m2)}")


