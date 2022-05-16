#Metodos para ordenar listas

#Ordenamiento por burbujeo

"""Se toma los valores en pareja, siendo uno i y el otro i+1. Para lograr la
rotacion se utiliza un valor extra auxiliar donde se almacena alguna de las
variables principales(cualquiera de las dos). """

a=[8,7,6,5,4,1]
i=0

print(a)

for j in range(len(a)-1):
    for i in range (len(a)-1):
        if a[i]>a[i+1]:
            aux= a[i+1]
            a[i+1]= a[i]
            a[i]= aux

print(a)

""" Con while

cont= 0

while cont<= len(a):
    for i in range (len(a)-1):
        if a[i]>a[i+1]:
            aux= a[i+1]
            a[i+1]= a[i]
            a[i]= aux
    cont= cont+1

print(a) """

""" Para poder parar el ciclo cambiamos el for principal por un while
con una señal(optimizado. USAR ESTE. ++ practico.)"""

señal= 1
b=[1,4,5,9,7]

while señal==1:    
    señal=0
    for i in range (len(b)-1):
        if b[i]>b[i+1]:
            aux= b[i+1]
            b[i+1]= b[i]
            b[i]= aux
            señal= 1           

print(b)

# Ordenamiento por selección

""" Tomo la variable en la posicion 0 y la llamamos i, y la tomo la
variable en la posicion 1 y la llamamos j. """

a=[8,7,6,5,4,3]
i= 0

for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            aux=a[j]
            a[j]=a[i]
            a[i]= aux

print(a)
