""" Dada la secuencia 53781 - 37815 - 78153 - ...., que num sigue? """

nro,cont= 53781,0

while cont <= 2:
    x = (nro%10000)*10
    suma = x + (nro // 10000)
    nro = suma
    cont = cont + 1
    print(suma)

""" Ingresar un nro entre 2 y 10, validar que este en el rango indicado.
Informar el factorial del nro ingresado """

nro = int (input("Ingrese un numero: "))
factorial= 1

#Para validar

while nro < 2 or nro > 10 :
    nro = int (input("Ingrese un numero valido: "))

while nro >1:
    factorial= factorial * nro
    nro=nro-1

print('El factorial es de',factorial)



    


        
        
         
