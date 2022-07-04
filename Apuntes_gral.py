#PRIMERA PARTE DEL CUATRIMESTRE

"""Hacer una sucesion de Fibonacci e informar a partir de la posicion 5:
• Numeros primos
• Numeros deficientes"""

a,b,primos, deficientes= 0,1,0,0

for i in range(2,26):
    c= a + b
    a=b
    b=c
    print(c)

divisor, cont, suma= 1,0,0

if i>= 5 and i%2==0:
    while divisor<= c:
        if c%divisor==0:
            cont=cont+1
        divisor= divisor+1
    if cont ==2:
        primos=primos+1

if i>=5 and i%2!=0:
    while divisor<c:
        if c%divisor==0:
            suma=suma+divisor
        divisor= divisor + 1
    if suma <c:
        deficientes= deficientes + 1


print("Hay", primos, "numeros primos en posicion par.")
print("Hay", deficientes, "numeros deficientes.")

"""resar un nro entre 2 y 10, validar qque se encuentre en este rango e informar su factorial"""

import random

nro=int(input("Ingrese un nro: "))
factorial=1

while nro>2 and nro<10:
    print("ERROR: Ingrese un numero valido entre el 2 y el 10: ")

while nro>1:
    factorial= factorial*nro
    nro=nro-1

print("El factorial es", factorial)

"""Dada la siguiente frecuencia, halla el numero siguiente: 53781-37851-78153-?"""

nro, cont= 53781, 0

while cont<=2:
    x=(nro%10000)*10
    suma= x + (nro//10000)
    nro=sumacont=cont+1
    print(suma)

#SEGUNDA PARTE DEL CUATRIMESTRE

""" Fibonacci en lista y raiz exacta"""
"""Dada la lista fibo, con valores iniciales entre
1 y 0. Generar la cuscesion y cargarla a la lista
fibo hasta la posicion 20 o hasta que aparezca
un valor con raiz cuadrada exacta, a partir de la
posicion 5."""

fibo= [0,1]
i=2
stop=0 #Señal para que el bucle while pare

while i<20 and stop==0:
#Fibo en lista
    fibo.append(fibo[i-2]+fibo[i-1])
#Raiz exacta
    if i>5:
        resto=1
        aux=fibo[i]
        while aux>0:
            aux= aux-resto
            resto=resto+2
        
        #Para abortar el bucle
        if aux==0:
            stop=1
    i = i+1

print(fibo)

""" De dos listas ordenadas (sin importar su len)
sacar lista c  uniendo a y b, comparando los primeros
indices de ambas listas, sacando asi el
mayor y el menor. 
Dadas las lista A y B AMBAS ORDENADASNDE MANERA
ASCENDENTE, obtener la lista c tambien ordenada
ascendentemente por la union de ambas."""

a= [2,6,9,12]
b=[1,3,5]
c=[]
i,j=0,0

while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i= i + 1
    else:
        c.append(b[j])
        j=j+1

#Al terminar el while, se controla que lista
#se termino y se pasa a la siguiente lista.

if i<=len(a):
    while j<len(b):
        c.append(b[j])
        j=j+1
else:
    while i<len(a):
        c.append(a[i])
        i=i+1
print(c)

#Metodos para ordenar listas

#ORDENAMIENTO POR BURBUJEO

"""Se toma los valores en pareja, siendo uno i
y el otro i+1. Para lograr la rotacion se
utiliza un valor extra auxiliar donde se almacena
alguna de las variables principales."""

#Con for
a=[8,7,6,5,4,1]
i=0

print(a)

for j in range(len(a)-1):
    for i in range (len(a)-1):
        if a[i]>a[i+1]:
            aux=a[i+1]
            a[i+1]=a[i]
            a[i]= aux

print(a)

#Con while, bucle mejorado
señal=1
b=[1,4,5,9,7]

while señal==1:
    señal=0
    for i in range (len(b)-1):
        if b[i]>b[i+1]:
            aux=b[i+1]
            b[i+1]=b[i]
            b[i]=aux
            señal=1
print(b)

#ORDENAMIENTO POR SELECCIÓN
"""Tomo la variable en la posicion 0 y la llamamos
i, y la tomo la variable en la posicion 1 y la
llamamos j."""

a=[8,7,6,5,4,3]
i=0

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]>a[j]:
            aux=a[j]
            a[j]=a[i]
            a[i]=aux
print(a)

#Metodos para buscar en listas

#BUSQUEDA BINARIA
"""Sirve para buscar valores en una lista, estos
tienen que estar en manera ordenada en forma 
ascendente. Se toma un min y un max con respecto
a la posicion, y se saca cuando es el medio:
(min+max)//2
Respecto a esto, se compara si el valor ingresado
es igual al valor del medio, si no es igual se
compara si es mayor (corriendo la posicion del
min a medio+1) o menor (corriendo la posicon
del max a medio-1) al valor del medio y se
vuelve hacer la comparacion. Cuando tanto el 
max como el min se invierten significa que el 
valor no se encuentra en la lista."""

datos=[2,8,13,15,26,35,48,90,122,123]
min, max, posicion=0,len(datos)-1,-1
valor=50

while min<=max and posicion==-1:
    medio=(min+max)//2
    #Si el valor es igual al del medio
    if valor==datos[medio]:
        posicion=medio
    #Si el valor es mayor al del medio
    if valor > datos[medio]:
        min=medio+1
    #Si el valor es manor al del medio
    else:
        max=medio-1
#Cuando un while tiene dos condiciones, se pone 
#una de referencia

if posicion!=-1:
    print("El valor se encontro en la posición0, posicion")
else:
    print("El valor no se encuentra.")

#Funciones

def bienvenida(nom):
    print("Bienvenidos a la clase de funciones")
    print("Hola", nom)

def superficie(x,y):
    sup=x*y
    print("La superficie es", sup)

print("Hoy es lunes 23/05")
nombre=input("Ingrese su nombre: ")
bienvenida(nombre)

a=int(input("Ingrese el lado A: "))
b=int(input("Ingrese el lado B: "))

superf= superficie(a,b)
print("La superficie es ", superf)
print("Fin.")


    
