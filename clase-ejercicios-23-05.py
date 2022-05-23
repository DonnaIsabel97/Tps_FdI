"""Ejercicio 1: Generar una lista con 20 valores entre 12 y 140.
Ingresar un valor por teclado e informar si el valor se encuentra o no en la lista."""
import random

lista=[]

for i in range(20):
    lista.append(random.randint(12,140))
    señal=1
    while señal==1:
        señal=0
        for j in range(len(lista)-1):
            if lista[j]>lista[j+1]:
                aux=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=aux
                señal=1
            
print(lista)    

mini, maxi, posicion=0, len(lista)-1,-1
valor=int(input("Ingrese un valor: "))

while mini<=maxi and posicion==-1:

   medio=(mini+maxi)//2

   if valor==lista[medio]:
      posicion=medio
   if valor>lista[medio]:
      mini=medio+1
   else:
      maxi=medio-1

if posicion !=-1:
    print("El valor se en encontró en la posición", posicion)
else:
    print("El dato no esta.. besito x")
    
    