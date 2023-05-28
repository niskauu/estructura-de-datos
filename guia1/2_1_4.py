import random
import numpy as np #solo para visualizar las matrices

n = 3 #random.randint(3,5)
matriz=[[3,2,1],[3,1,2],[2,2,1]]
# for i in range(n):
#     aux=[]
#     for j in range(n):
#         num = random.randint(1,3)
#         aux.append(num)
#     matriz.append(aux)

print(f"{np.array(matriz)}\n")

def escalarxfila(escalar:float,fila:int,matriz:list):
    for i in range(len(matriz[fila])):
        matriz[fila][i] = matriz[fila][i]*escalar
    return matriz[fila]

def restarfilas(fila1:list,fila2:list):
    for i in range(len(fila1)):
        fila1[i] = fila1[i]-fila2[i]
    return fila1

def crear_identidad(a:list):
    filas = len(a)
    columnas = len(a[0])
    if filas == columnas:
        identidad = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            identidad.append(fila)
        return identidad
    else:
        return None
    
def aumentar_matriz(a:list,b:list):
    if len(a)==len(b):
        for i in range(len(a)):
            a[i] += b[i]
        return a
    else:
        return None

matriz_identidad = crear_identidad(matriz)

#Aumentar
matriz_a = aumentar_matriz(matriz,matriz_identidad)
print(f"{np.array(matriz_a)}\n")

for j in range(n):
    for i in range(n):
        escalarxfila(1/matriz_a[i][j],i,matriz_a)
    for i in range(n-1):
        restarfilas(matriz_a[i+1],matriz_a[j])
    #extra
    matrizaux=[]
    for i in range(len(matriz_a)):
        aux=[]
        for j in range(len(matriz_a[0])):
            aux.append(round(matriz_a[i][j],2))
        matrizaux.append(aux)

    print(f"{np.array(matrizaux)}\n")
    #fin del extra   

  


    