"""Ejercicio 1: Crear 3 listas de 20 elementos cada una
Legajo: aleatorio entre 100 y 1000
Parcial1: Aleatorio entre 1 y 10
Parcial2: Aleatorio entre 1 y 10
Una vez creadas, recorrerlas e informar:
1) Cuantos alumnos promocionana la materia (ambos parciales >=7)
2) Cuantos alumnos recursan (ambos parciales <4)
3) Legajo del primer alumno con mayor promedio
4) Porcentaje de alumnos que rinden final  """

import random

legajo, parcial1, parcial2= [], [], []
contPromo, contRecu, contFinal =0, 0 , 0
mayorP, legajoMayor = 0, 0

for i in range(20):

    nroLegajo = random.randint(100, 1000)
    legajo.append(nroLegajo)
    
    notaP1 = random.randint(1, 10)
    parcial1.append(notaP1)

    notaP2 = random.randint(1, 10)
    parcial2.append(notaP2)

    #Punto 1
    if notaP1 >= 7 and notaP2 >= 7:
        contPromo = contPromo + 1

    #Punto 2    
    elif notaP1<4 and notaP2< 4:
        contRecu= contRecu + 1

    #Punto 3
    promedio = (notaP1 + notaP2) / 2
   
    if promedio>mayorP :
        mayorP = promedio
        legajoMayor = legajo[i]

    #Punto 4

    contFinal = ((20 - contPromo - contRecu) * 100) / 20


print(legajo)    
print(parcial1)    
print(parcial2)
print("La cantidad de alumnos que promocionan son: ", contPromo)
print("La cantidad de alumnos que recursan son: ", contRecu)
print("El legajo del alumno con mayor promedio es: ", legajoMayor)
print("El porcentaje de alumnos que van a final es de ",contFinal,"%.")

"""Ejercicio 2: Crear 3 listas, de 20 valores cada una
codrep: aleatorio entre 100 y 1000
stock: aleatorio entre 0 y 100
reponer: aleatorio entre 5 y 15
Emitir un listado (codrep) con aquellos productos cuyo stock
sea menor o igual al valor en reponer"""

import random

codrep, stock, reponer = [],[],[]

for i in range (20):

    codigorep= random.randint(100, 1000)
    print(codigorep, end=' ')

    codigostock= random.randint(0,100)
    stock.append(codigostock)

    codigoreponer= random.randint(5, 15)
    reponer.append(codigoreponer)

    if codigostock <= codigoreponer:
        codrep.append(codigorep)

    
print()
print(stock)
print(reponer)
print(codrep)
    


""" Ejercicio 3 : Dada la lista fibo, con valores iniciales 1 y 0.
Generar la sucesion y cargarla a la lista fibo,
hasta la posicion 20 o, hasta que aparezca un valor con raiz cuadrada exacta,
a partir de la posicion 5 """

fibo=[0, 1]
i= 2
stop= 0 #señal para que el bucle while pare

while i < 20 and stop==0:

#Fibonacci en lista
    
    fibo.append(fibo[i - 2] + fibo [i - 1])

#Raiz exacta

    if i>5:
        resto= 1
        aux= fibo [i]
        while aux>0:
            aux=aux-resto
            resto=resto+2
            
#Para abortar el bucle
        if aux== 0: 
            stop = 1            
    i= i + 1

print(fibo)

""" Ejercicio tarea del 2/05 (Ejercicio de parcial/final)"""

a=[2,6,9,12]
b=[1,3,5]
c=[]
i,j=0,0


while i<len(a) and j<len(b):

    if a[i] < b[j]:
        c.append(a[i])
        i= i + 1

    else:
        c.append(b[j])
        j= j + 1

#Termino el while, se controla que lista termino y se pasa a la otra

if i>=len(a):
    while j<len(b):
        c.append(b[j])
        j=j+1

else:
    while i<len(a):
        c.append(a[i])
        i= i + 1

print(c)    
