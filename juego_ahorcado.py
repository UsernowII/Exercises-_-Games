#cree un programa que simule el juego del ahorcado
#debe seleccionar una palabra aleatoria de una lista de palabras
#muestre una pista de la palabra aleatoria ( "MOUSE" ) pisa ( M_ _ _ E)
#El usuario debe ingresas una palabra y si es igual a la palabra aleatoria
#entonces el programa mostrara True , caso contrario False

from random import*
again = 0
i = 1
palabras = ["mouse", "raton", "monitor", "teclado"]
indice = randint(0,len(palabras)-1)
pal = palabras[indice].upper()
pista1 = pal[0]
pista2 = pal[-1]
nGuion = len(pal)-2
subGuion = nGuion * " _ "
print("**Adivine la palabra**")
pista = pista1 + subGuion + pista2
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
