""" Ejercicio 1: Generar 30 valores comprendidos entre 1000 y 10000, correspondientes
a los codigos de repuestos de un electrodomestico.
• Cargar los valores a una lista cod.
• Generar una segunda lista (stock) con valores entre 0 y 100 siendo el
stock de cada repuesto.
• Cargar una tercera lista, aquellos codigos de repuestos cuyo stock
sea menor a 10 unidades.
Mostar la ultima lista ordenada, mostrando los codigos en una fila."""

import random

cod=[]
stock=[]
lista=[]

for i in range(30):

#Generación de valores
    
    cod.append(random.randint(1000, 10000))
    stock.append (random.randint(0, 100))

#Para agregar a la tercer lista

    if stock[i]< 10:
        lista.append(cod[i])
        
#Para ordenar lista
        
    señal=1
    while señal==1:
        señal=0
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux=lista[i+1]
                lista[i+1]= lista[i]
                lista[i]= aux
                señal=1
print(cod)
print(stock)
print(lista)
                
for i in range(len(lista)):
    print(lista[i], end=' ')

""" Ejercicio 2: Dados los valores 0 y 1, de la sucesión de Fibonacci, generarlos
hasta la posicion 20.
Crear una lista con los valores pares.
Ordenar la lista de mayor a menor y mostrarla."""

vA, vB= 0,1
cont= 0
pares=[]

#Fibonacci
while cont<20:
    vC= vA + vB
    print(vC, end=' ')
    vA=vB
    vB=vC
    cont=cont+1

#Seleccion de pares
    if vC%2==0:
        pares.append(vC)
        
#Ordena de mayor a menor
    señal= 1
    while señal==1:
        señal=0
        for i in range(len(pares)-1):
            if pares[i]<pares[i+1]:
                aux= pares[i+1]
                pares[i+1]= pares[i]
                pares[i]=aux
                señal=1
                
print(pares)

"""Ejercicio 3: Crear una lista con 50 valores comprendidos entre 10 y 300.
Ingresar un valor por teclado e informar en que posicion se
encuentra o, si no está en la lista """

import random

lista=[]
cont= 0

for i in range(50):
    lista.append(random.randint(10,300))

print(lista)

valor= int(input("Ingresa un valor entre 10 y 300: "))

señal=0

while cont<50 and señal==0:
    if valor== lista[cont]:
        posicion=cont
        señal=1
    cont=cont+1
if señal==1:
    print("El numero se encuentra en la posicion ",posicion)
else:
    print("No se encuentra en la lista.")



