#reto vocales

palabra = str(input("Ingrese la palabra:"))
palabra = palabra.lower()
palabra = list(palabra)
a=0
e=0
i=0
o=0
u=0
for j in range(len(palabra)):   
    if palabra[j]=="a":
        a=a+1
    elif palabra[j]=="e":
        e=e+1
    elif palabra[j]=="i":
        i=i+1
    elif palabra[j]=="o":
        o=o+1
    elif palabra[j]=="u":
        u=u+1

print(palabra)
print(f"La palabra contiene {a} a's, {e} e's, {i} i's, {o} o's, y {u} u's")