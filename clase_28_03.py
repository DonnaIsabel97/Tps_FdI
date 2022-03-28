'''Bucle While'''
''' While por conteo '''

suma, numero=0, 1

while numero<=10:
    suma=suma+numero
    numero=numero+1
    print( suma, end=' ')
   
print()
print("la suma es", suma )

''' While controlado x evento '''

suma=0
print("Ingrese un valor, para terminar -1")
numero=int(input())

while numero!=-1:
    suma=suma+numero
    print("Ingrese un valor, para terminar -1")
    numero=int(input())

print("La suma es : ", suma)

''' Operadores lógicos'''

#AND, se tiene que dar ambas condiciones para que sea V
num= int(input())

if num>50 and num%2==0 :
    print('algo')

#OR , solo uno de las condiciones tiene que ser v

num = int(input())

if num>50 or num%2==0:
    print('algo')

''' Ejercicio de operadores'''
#Identificar si un numero es o no primo

div = 1
cont= 0
num = int(input('Ingrese el nro deseado '))

while div <= num:
    if num % div ==  0:
        cont = cont +1
    div= div+1
    
if cont > 2 :
    print('No es un nro primo')
else:
    print('Es un nro primo')

''' Bucle For '''

''' Syntax

for variable in range (vi, vf, i):
          acción
'''

cont= 0

for cont in range (5):
    print(cont)

for cont in range (1,5):
    print(cont)


#Ejercicios
''' arrojar um dado 10 veces e informar que valores salieron '''

import random

cont, impar=0, 0

while cont < 10:
    nro = random.randint(1,6)
    if nro %2 == 1:
        print(nro, end = ' ')
        impar=impar + 1
    cont= cont+1

print()
print('Salieron ', impar, 'valores')


    
''' arrojar um dado 10 veces e informar ctas veces salio un valor impar y cuales fueron '''


"""Arrojar 100 bolas de ruleta
informar cuantas veces salió un valor de la segunda docena (13-24)"""

cont, valor = 0,0

while cont < 100:
    nro= random.randint (1, 24)
    if nro >= 13:
        valor = valor + 1
    cont = cont +1

print()
print('La cantidad es de', valor)

#Tarea
"""Arrojar 100 bolas de ruleta
informar cuantas veces salió un valor de la segunda docena (13-24)"""

#FIBONACCI
''' Generar 20 valores de la sucesion de Fibonacci comenzando con a=0 y b=1'''

vA, vB = 0, 1
cont= 0
print(vA,' ',vB,end=' ')

while cont<20:
    vC = vA + vB
    print(vC, end=' ')
    vA=vB
    vB=vC
    cont=cont+1
    
