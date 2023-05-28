import numpy as np
import random

matriz1=[]
matriz2=[]
matriz3=[]
n=3


# crear_matriz: list int int int -> None
# crear matriz recibe una lista vacia m, un entero n
# y dos numeros llamados min y max
# crea un ciclo para crear una matriz nxn con numeros
# enteros que van desde min a max
def crear_matriz(m:list,n:int,min:int,max:int):
    for i in range(n):
        aux=[]
        for j in range(n):
            num = random.randint(min,max)
            aux.append(num)
        m.append(aux)
    
crear_matriz(matriz1,n,1,10)
crear_matriz(matriz2,n,11,30)
crear_matriz(matriz3,n,-10,-1)
matriz1=np.array(matriz1)
matriz2=np.array(matriz2)
matriz3=np.array(matriz3)

print("Las 3 matrices son las siguientes: ")
print(f"A: {matriz1}",f"B: {matriz2}",f"C: {matriz3}",sep="\n\n")

print("\nSe quiere demostrar que: (A+B)*C == A*C + B*C\n")

a_add_b = np.add(matriz1,matriz2)

print(f"A+B resulta en:\n{a_add_b}\n")
print(f"Al multiplicar el resultado por C es:\n{np.dot(a_add_b,matriz3)}\n")

a_mul_c = np.dot(matriz1,matriz3)
b_mul_c = np.dot(matriz2,matriz3)

print(f"Por otro lado A*C resulta en:\n {a_mul_c}\n")
print(f"B*C resulta en:\n {b_mul_c}\n")

print(f"y A*C + B*C resulta en:\n {np.add(a_mul_c,b_mul_c)}\n")

print(f"Se demuestra que (A+B)*C:\n{np.dot(a_add_b,matriz3)}\n es igual a A*C + B*C:\n{np.add(a_mul_c,b_mul_c)}")