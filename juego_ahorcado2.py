#cree un programa que simule el juego del ahorcado
#debe seleccionar una palabra aleatoria de una lista de palabras y luego una letra aleatoria
#muestre una pista de la palabra aleatoria ( "MOUSE" ) pisa a leatoria( _ _ U _ _ )
#El usuario debe ingresas una palabra y si es igual a la palabra aleatoria
#entonces el programa mostrara True , caso contrario False

import random as rd
i = 1
again = 0
palabras = ["mouse", "raton", "monitor", "teclado"]
pal = rd.choice(palabras).upper()
#print(pal)
index = rd.randint(0,len(pal)-1)
pista = pal[index]
nGuion1 = len(pal[:index])
nGuion2 = len(pal[index +1:])
pista = nGuion1* " _ " + " " + pista + " "+ nGuion2 * " _ "
print(pista)
palabra = input("Ingrese la palabra ").upper()
condicion = palabra == pal
if condicion :
    print(condicion,"***Gano!!!!***")
else:
    print(condicion)
    again = input("Error, quiere probar de nuevo < Fin para terminar> ").lower()
    while again != "fin":
        palabra = input("Ingrese la palabra ").upper()
        condicion = palabra == pal
        print("Adivino ?", condicion)
        i +=1
        again = input("Error, quiere probar de nuevo < Fin para terminar> ").lower()
print("Su numero de intentos fue: ", i)        
print("--------Fin del juego--------")   