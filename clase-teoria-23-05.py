#Busqueda en listas

#Busqueda binaria
"""Sirve para buscar valores en una lista, estos tienen que estar en manera ordenada en forma ascendente. Se toma un minimo y un maximo con respecto a la posicion, se saca cuando es el medio((minimo+maximo) // 2) y respecto
a esto se compara si el valor ingresado es igual al valor del medio, si no es igual se compara si es mayor (corriendo la posicion del minimo a medio+1) o menor(corriendo la posicion del maximo a medio-1) a este y
se vuelve a hacer la comparación. Cuando tanto el maximo como el minimo se invierten, significa que el valor ingresado no se encuentra"""

datos= [2,8,13,15,26,35,48,90,122,123]

mini, maxi, posicion=0, len(datos)-1,-1
valor=50

while mini<=maxi and posicion==-1:

   medio=(mini+maxi)//2
#El valor es igual al del medio
   if valor==datos[medio]:
      posicion=medio
#El valor es mayor al medio
   if valor>datos[medio]:
      mini=medio+1
#El valor es menor al medio
   else:
      maxi=medio-1
#Cuando un while tiene dos condiciones, para poner una de referencia            
if posicion !=-1:
    print("El valor se en encontró en la posición", posicion)
else:
    print("El dato no esta.. besito x")
    
    