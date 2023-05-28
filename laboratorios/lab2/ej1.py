import numpy as np
import random

# pt 1

filas1=random.randint(2,5)
columnas1=random.randint(2,5)
print(f"las dimensiones de las primeras matrices es filas: {filas1}, columnas: {columnas1}\n")

matriz1=[]
for i in range(filas1):
    aux=[]
    for j in range(columnas1):
        num = int(input(f"Ingrese el elemento {i+1},{j+1} de la primera matriz: "))
        aux.append(num)
    matriz1.append(aux)

print(f"\nla primera matriz es: {matriz1}\n")

matriz2=[]
for i in range(filas1):
    aux=[]
    for j in range(columnas1):
        num = int(input(f"Ingrese el elemento {i+1},{j+1} de la segunda matriz: "))
        aux.append(num)
    matriz2.append(aux)

print(f"\nla segunda matriz es: {matriz2}\n")

matriz_resta=[]
for i in range(filas1):
    aux=[]
    for j in range(columnas1):
        num=matriz1[i][j]-matriz2[i][j]
        aux.append(num)
    matriz_resta.append(aux)

print(f"las matrices restadas dan como resultado: {matriz_resta}\n") 

# pt 2
matriz_resta = np.array(matriz_resta)

filas2=int(input("Ingrese filas de la matriz que será multiplicada: "))
columnas2=int(input("Ingrese columnas de la matriz que será multiplicada: "))

if filas2==columnas1:
    matriz_mul=[]
    for i in range(filas2):
        aux=[]
        for j in range(columnas2):
            num=int(input(f"ingrese el elemento {i+1},{j+1} de la matriz: "))
            aux.append(num)
        matriz_mul.append(aux)
    print(f"la matriz ingresada es: {matriz_mul}")
    matriz_mul=np.array(matriz_mul)
    matriz= matriz_resta.dot(matriz_mul)
    print(f"las matrices multiplicadas dan como resultado:\n{matriz}")
else:
    print("Las matrices no se pueden multiplicar")

# pt 3; comprobar (ab)transpuesta == atranspuesta*btranspuesta

print("comprobar propiedad: (ab)transpuesta == a transpuesta*b transpuesta")
print(matriz_resta)
print(matriz_mul)

matrizab = matriz_resta.dot(matriz_mul) #matrices multiplicadas
matrizab_t = matrizab.transpose() #matrices multiplicadas transpuestas

matrizat = matriz_resta.transpose() #matriz a transpuesta
matrizbt = matriz_mul.transpose() #matriz b transpuesta
matrizat_bt = matrizbt.dot(matrizat) #multiplicacion transpuestas

print(f"la matriz (a*b)transpuesta es {matrizab_t}")
print(f"la matriz (a transpuesta)*(b transpuesta) es {matrizat_bt}")
print("se comprueba que ambas son iguales")