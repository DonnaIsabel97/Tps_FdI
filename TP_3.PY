#TP N° 3 : Condicional

#Ejercicio 1

""" Ingresar dos numeros enteros e indicar si son o no iguales """

num1= int(input("Ingresar su primer numero: "))
num2=int(input("Ingresar su segundo numero: "))

if num1 == num2:
    print("Los dos numeros ingresados son iguales.")
else:
    print("Los dos numeros ingresados son distintos.")

#Ejercicio 2

""" Leer un numero entero e imprimir un mensaje indicando si es par o
impar"""

num= int(input("Ingresar un numero entero: "))

if num %2==0:
    print("El",num,"es un numero par.")
else:
    print("El",num,"es un numero impar.")

#Ejercicio 3

""" Crear un programa que pida un número de mes (ejemplo 4) y escriba el
nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar
en caso que no lo sea."""

nroMes = int(input("Ingresar un numero de mes: "))

if nroMes < 1 or nroMes> 12:
    print("ERROR: Ingresa un numero de mes valido entre el 1 y el 12")

if nroMes == 1:
    print("El mes correspondiente al nro ingresado es: Enero")
elif nroMes== 2:
    print("El mes correspondiente al nro ingresado es: Febrero")
elif nroMes== 3:
    print("El mes correspondiente al nro ingresado es: Marzo")
elif nroMes== 4:
    print("El mes correspondiente al nro ingresado es: Abril")
elif nroMes== 5:
    print("El mes correspondiente al nro ingresado es: Mayo")
elif nroMes== 6:
    print("El mes correspondiente al nro ingresado es: Junio")
elif nroMes== 7:
    print("El mes correspondiente al nro ingresado es: Julio")
elif nroMes== 8:
    print("El mes correspondiente al nro ingresado es: Agosto")
elif nroMes== 9:
    print("El mes correspondiente al nro ingresado es: Septiembre")
elif nroMes== 10:
    print("El mes correspondiente al nro ingresado es: Octubre")
elif nroMes== 11:
    print("El mes correspondiente al nro ingresado es: Noviembre")
elif nroMes ==12:
    print("El mes correspondiente al nro ingresado es: Diciembre")


#Ejercicio 4

""" Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.
• Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
• Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
• Se debe recuperar cuando al menos una de las dos notas es menor a 4."""


nota1= int(input("Ingresa la nota del primer parcial: "))
nota2= int(input("Ingresa la nota del segundo parcial: "))

if nota1>= 7 and nota2>=7 :
    print("¡Felicitaciones! Promocionaste la materia.")
elif nota1>=4 and nota2>=4 :
    print("¡Aprobaste!")
elif nota1<4 and nota2>=4:
    print("Debes recuperar recuperar el primer parcial.")
elif nota1>=4 and nota2<4:
    print("Debes recuperar recuperar el segundo parcial.")
else:
    print("Desaprobaste la materia :(")

#Ejercicio 5

""" Una editorial determina el precio de un libro según la cantidad de
páginas que contiene. El costo básico del libro es de $500, más $20,20
por página con encuadernación rústica. Si el número de páginas supera las
300 la encuadernación debe ser en tela, lo que incrementa el costo en $200.
Además, si el número de páginas sobrepasa las 600 se hace necesario un
procedimiento especial de encuadernación que incrementa el costo en $336.
Desarrollar un programa que calcule el costo de un libro dado el número de
páginas. """

nroPag= float(input("Ingrese la cantidad de páginas que contiene el libro: "))
costo= 0

if nroPag<300:
    costo= 500 + (20.20 * nroPag)
    print("El costo sera de $", costo)
elif nroPag>300:
    costo = 500 + (20.20 * nroPag) + 200
    print("El costo será de $", costo)
elif nroPag>600:
    costo = costo = 500 + (20.20 * nroPag) + 336
    print("El costo será de $", costo)

#Ejercicio 6

""" Una remisería requiere un sistema que calcule el precio de un viaje a
partir de la cantidad de km que desea recorrer el usuario. Tiene la siguiente
tarifa:
▪ Viaje mínimo $50
▪ Si recorre entre 0 y 10km: $20/km
▪ Si recorre 10km o más: $15/km """

km = float(input("Ingresa los km que el cliente desea recorrer: "))
monto= 0

if km > 0 and km < 10:
    monto= km * 20
    if monto < 50:
        print("El viaje costará $50")
    else:
        print("El viaje costará", monto)
elif km>10:
    monto= km * 15
    print("El viaje costará", monto)

#Ejercicio 7

""" Leer un número correspondiente a un año e imprimir un mensaje indicando si
es bisiesto o no. Se recuerda que un año es bisiesto cuando es divisible por 4.
Sin embargo, aquellos años que sean divisibles por 4 y también por 100 no son
bisiestos, a menos que también sean divisibles por 400.
Por ejemplo, 1900 no fue bisiesto, pero sí el 2000. """

año = int(input("Ingresa elmaño deseado: "))

if año%4!=0:
    print("El",año,"no es bisiesto.")
elif año%4== 0 and año%100!= 0 :
    print("El",año,"es bisiesto.")
elif año%4 == 0 and año%100== 0 and año%400!=0:
    print("El",año,"no es bisiesto.")
elif año%4==0 and año%100==0 and año%400==0:
    print("El",año,"es bisiesto.")

#Ejercicio 8

""" Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si
es casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social:
3%, Sindicato: 3%.
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y
estado civil (‘s’ o ‘c’). Se debe informar: (reemplazar los 9 por los valores
que correspondan) """

sueldoB= float(input("Ingresar el sueldo básico: "))
añosA = int(input("Ingresar los años de antigúedad: "))
eCivil = input("Ingresar 'c' si es casado o 's' si es soltero: ")

incre, sueldoSD, jub, oB, sind, sueldoCD = 0,0,0,0,0,0

if eCivil == "c" or eCivil == "C":
    incre = (sueldoB * 0.7) * añosA
    sueldoSD = incre + sueldoB
    jub= sueldoB * 0.11
    oB = sueldoB * 0.3
    sind = sueldoB * 0.3
    sueldoCD = sueldoSD - jub - oB -sind

    print("El sueldo basico es de", sueldoB, ", sus años de antigúedad son",añosA, "dandole un incremento a su sueldo de", incre, "quedando su sueldo en", sueldoSD)
    print("El importe de la jubilacion es de", jub, ", el de la obra social es de",oB,"y el del sindicato es de",sind)
    print("Su sueldo neto es de", sueldoCD)
    
elif eCivil == "s" or eCivil == "S":
    incre = (sueldoB * 0.5) * añosA
    sueldoSD = incre + sueldoB
    jub= sueldoB * 0.11
    oB = sueldoB * 0.3
    sind = sueldoB * 0.3
    sueldoCD = sueldoSD - jub - oB -sind

    print("El sueldo basico es de", sueldoB, ", sus años de antigúedad son",añosA, "dandole un incremento a su sueldo de", incre, "quedando su sueldo en", sueldoSD)
    print("El importe de la jubilacion es de", jub, ", el de la obra social es de",oB,"y el del sindicato es de",sind)
    print("Su sueldo neto es de", sueldoCD)












