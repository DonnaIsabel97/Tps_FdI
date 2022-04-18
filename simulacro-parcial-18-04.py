''' teniendo en cuenta como valores iniciales a los valores 0 y 1, y cuyas
posiciones son 0 y 1, respectivamente, generar la sucesion de fibonacci
hasta la posicion 25.
Informar:
1. Apartir de la posicion 5 que valor son primos y que ademas, estan en
posicion pares. ¿Cuantos hay en total?
2. Cuantos valores deficiente se encontraron en posiciones impares
Numero deficiente: numero cuya suma de divisores sin el propio numero
es menor al numero. Ej: 15 > 1 + 3 + 5 '''

vA, vB = 0, 1
cont= 0
divisores= 0
divi= 1
contD= 0

for i in range (1,25):
#Fibonacci
    vC= vA + vB
    print(vC)
    vA=vB
    vB=vC
    cont = cont + 1
    
#Primos

    div, primos= 1, 0
    contP= 0
    if i>= 5 and i%2 == 0:
        while div <= vC:
            if vC % div == 0:
                contP = contP + 1
            div= div + 1
        if contP == 2:
            print('es un numero primo')
            
#Numero deficiente
    divisor, suma, deficiente= 1,0,0


    if i>=5 and i%2!=0:
        while divisor<vC:
            if c%divisor==0:
                suma= suma + divisor
            divisor = divisor + 1
        if suma<vC:
            deficiente = deficiente + 1

#poner bien las variables
        
        
print('Hay', contP, 'numeros primos en total y hay', contD, 'nros deficientes.')


    
