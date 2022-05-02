""" Inicializar la lista mes con 30 valores cero
Se ingresa por teclado el dia y un gasto para ese dia.
Los valores y los dias noson ingresados en orden y puede haber varios
gastos para un mismo dia.
El ingreso de datos finaliza cuando se ingresa -1 en la variable dia.
Por fin de proceso, informar cual fue el dia de mayor gasto y cuanto
fue ese gatos. """

mes = []
mayor,menor=0,0
diaMayor, diaMenor = 0,0

for i in range (30):
    mes.append(0)

dia= int(input("Ingrese el nro del día: "))

while dia != -1:
    gasto= int(input("Ingrese el gasto del día: "))
    mes[dia-1] = mes [dia-1]+ gasto
    dia= int(input("Ingrese el nro del día: "))

for gasto in mes:
    
    if gasto>mayor:
        mayor= gasto
        diaMayor= mes[dia]
    if gasto<mayor:
        menor= gasto
        diaMenor = mes[dia]



print(mes,)
print(mayor, menor)
print(diaMayor, diaMenor)

    

