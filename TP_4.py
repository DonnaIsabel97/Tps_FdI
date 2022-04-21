#TP N°4 : Estructura iterativa (bucles)

#Ejercicio 1

""" Escribir un algoritmo que muestre los primeros 25 números naturales."""

cont= 0

while cont < 25:
    cont = cont + 1
    print(cont, end=' ')

#Ejercicio 2

""" Calcular e imprimir la suma de los números comprendidos entre 42 y 176. """

cont, suma= 0, 0

while cont<176:
    cont= cont + 1
    if cont> 42:
        suma= cont + suma
        print(suma, end=' ')

#Ejercicio 3

""" Mostrar las tablas de multiplicar (entre 1 y 10) del número 4.
¿Cómo cambiaría el algoritmo para que el usuario pueda decidir la tabla de
multiplicar a mostrar?"""

tabla, num, cont= 0, 4, 0

while cont<= 10:
    tabla = num * cont
    cont = cont + 1
    print(tabla, end=' ')

print()    
#Para que el usuario pueda decidir en vez de poner una variable fija,
#pongo un input

num = int(input("Ingresa el numero deseado: "))
tabla, cont= 0,0

while cont<=10:
    tabla=num * cont
    cont=cont+1
    print(tabla, end=' ')

#Ejercicio 4

""" Leer 10 números enteros e imprimir el promedio, el mayor y en qué orden
fue ingresado el mayor valor,si se ingresó más de una vez debe informar el
primer ingreso. """

