''' Ejercicio 2 '''
# a)

calculo = (12*4)+(4*5)
print(calculo)

# b)

calculo = 12 * (4+4) * 5
print(calculo)

#c)

calculo = (5*4)/2
print(calculo)

#d)

calculo = 5 * (4/2)
print(calculo)

#e)

calculo = 24 / (2 ** 2)
print(calculo)

#f)

calculo = (24/2) ** 2
print(calculo)

#g)

calculo = -(9 ** 2)
print(calculo)

#h)

calculo = (-9) ** 2
print(calculo)

#i)

calculo = 10 / 3
print(calculo)

#j) 

calculo = 10 // 3
print(calculo)

#k)

calculo = 12 % 5
print(calculo)

''' Ejercicio 3 '''

nota1 = int(input('Ingresa el valor de tu primera nota: '))
nota2= int(input('Ingresa el valor de la segunda nota: '))

promedio = (nota1 + nota2) / 2

print('El promedio de tus dos parciales es ', promedio)

''' Ejercicio 4 '''

''' Ejercicio 5 '''

capital = int(input('Ingrese su capital invertido: '))

capitalGanado = (capital * 0.2) * 6

capitalFinal = capitalGanado + capital

print ('El dinero ganado en seis mese será de ', capitalGanado, 'siendo su capital final de ', capitalFinal)

''' Ejercicio 6 '''

medidas = int(input('Ingresa la medida en metros que desea convertir: '))

cm = medidas * 100
pulgadas = cm / 2.54
pie = pulgadas / 12
yarda = pie / 3

print('La medida deseada equivale a ', cm, 'centimetros, ', pulgadas, 'pulgadas, ', pie, 'pies y ', yarda, 'yardas.')

''' Ejercicio 7 '''
#salario basico = 2000 , comisionfija = 20%, comisionextra = 5%

vendedor = int(input('Ingresa el numero identificatorio del vendedor: '))
ventas = int(input('Ingrese la cantidad de las ventas: '))
comision = int(input('Ingrese el valor total de las ventas realizadas: '))
salario = int(input('Ingrese su salario basico: '))

comisionfija= ventas * 0.2 #Preguntar si es sobre la cantidad de ventas o sobre el monto total de las ventas
comisionvalor = comision * 0.5

salariototal = salario + comisionfija + comisionvalor

print('Al vendedor numero ', vendedor, 'le corresponde un salario total de', salariototal)

''' Ejercicio 8 '''



