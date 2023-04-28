#Niska Silva
#Ignacio Vega

import random

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m1 = []
for i in range(filas):
    aux = []
    for j in range(columnas):
        aux = aux+[random.randint(1,5)]
    m1=m1+[aux]

m2 = []
for i in range(filas):
    aux = []
    for j in range(columnas):
        aux = aux+[random.randint(1,5)]
    m2=m2+[aux]
    
# def sumaMatrices(x,y):
#     for i in range(len(x)):
#         for j in range(len(x[0])):
#             x[i][j] = x[i][j] + y[i][j]
#     return x

# def restaMatrices(x,y):
#     for i in range(len(x)):
#         for j in range(len(x[0])):
#             x[i][j] = x[i][j] - y[i][j]
#     return x

def sumaMatrices(x,y):
    matriz=[]
    for i in range(len(x)):
        aux=[]
        for j in range(len(y[0])):
            aux = aux + [x[i][j] + y[i][j]]
        matriz=matriz+[aux]
    return matriz

def restaMatrices(x,y):
    matriz=[]
    for i in range(len(x)):
        aux=[]
        for j in range(len(y[0])):
            aux = aux + [x[i][j] - y[i][j]]
        matriz=matriz+[aux]
    return matriz

print(f"\nLa primera matriz sera:\n {m1}")
print(f"\nLa segunda matriz sera:\n {m2}")
print(f"\nLa suma es: \n{sumaMatrices(m1,m2)}")
print(f"\nLa resta es: \n{restaMatrices(m1,m2)}")