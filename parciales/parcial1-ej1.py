import numpy as np
from numpy.linalg import inv, det
import random

A=[]
B=[]
C=[]
n=4

# crear_matriz: list, int -> None
# crear matriz recibe una lista vacia m y un entero n
# crea un ciclo para crear una matriz nxn con numeros entre 0 y 10
def crear_matriz(m:list,n:int):
    for i in range(n):
        aux=[]
        for j in range(n):
            num = random.randint(0,10)
            aux.append(num)
        m.append(aux)
    

crear_matriz(A,n)
crear_matriz(B,n)
crear_matriz(C,n)
A=np.array(A)
B=np.array(B)
C=np.array(C)

print("Las 3 matrices son las siguientes: \n")
print(f"A: {A}",f"B: {B}",f"C: {C}",sep="\n\n")

print("\nLa operacion que se quiere realizar es: (a^3 * b^-1 * c)+[(a^3)^-1]\n")

# (a*a)*a; a elevado a 3
a3=np.dot(A,A)
a3=np.dot(a3,A)

# b inversa
if det(B)!=0:
    b1=inv(B)
else:
    print("la matriz B no es invertible")
    exit()
#lo siguiente continua si y solo si B es invertible

#(a^3)inversa
if det(a3)!=0:
    a31=inv(a3)
else:
    print("la matriz (A^3) no es invertible")
    exit()
#lo siguiente continua si y solo si A**3 es invertible

# D = (a^3 * b^-1 * c)+[(a^3)^-1]

# (a^3 * b^-1 * c)
D=np.dot(a3,b1)
D=np.dot(D,C)

# (a^3 * b^-1 * c)+[(a^3)^-1]
D=np.add(D,a31)

print(f"El resultado de la operacion es: \n{D}")

