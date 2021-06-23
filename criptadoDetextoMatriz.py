#El metodo bifido es un cifrado fraccionario,el metodo comienza con una matriz 5x5
#palabra clave de cifrado "qwerty"
#  1 2 3 4 5
#1 q w e r t
#2 y a b c d
#3 f g h ij k
#4 l m n o p
#5 s u v x z
#matriz de 5x5 i yj comparten lugares
#las primeras posiciones son ocupadas por los valores de la clave
#cifrar palabra "informatica"
#34 43 31 44 14 42 22 15 34 24 22 ( fila, columna)
#el equivalente numerico se divide en dos de la siguiente forma:
#34433144144
#22215342422
#se combina nuevamente intercalando un digito de la primera mitad con la segunda mitad
#32 42 42 31 35 13 44 42 14 42 42
# volviendo a consultar la matriz de cifrado
#gmmfkeomrmm ( palabra cifrada)
import string
def crearMatriz(palabra):

    listaAbc = list(string.ascii_lowercase) #lista con el abc
    listaClave = list(palabra) #lista con la clave

    for caracClave in listaClave: # remueve los caracteres dados por el parametro
        if caracClave in listaAbc:
            listaAbc.remove(caracClave)

    total = listaClave + listaAbc

    posi = total.index('i') # busca la "i" y se remplaza por "ij" se remueve la j
    total[posi] = 'ij'
    total.remove('j')

    matriz = [] #se crea la matriz 
    ini = 0
    fin = 5
    for f in range (0,5): # se recorre para que en un rango de 5 se creen sub listas en la matriz
        fila = total[ini:fin]
        matriz.append(fila)
        ini+=5
        fin+=5
    return matriz

def letraCoordenada(letra,matriz):
    if letra == "i" or letra == "j":
        letra = 'ij' # se comprueba que i-j tengan el mismo indice
    posColumna = 0
    posFila = 0
    #for fila in matriz:
    for f in range(len(matriz)):# se recorre la matrix por indices
        fila = matriz[f] # se ubican las filas
        if letra in fila:
            posColumna = fila.index(letra)+1 # si la letra esta en la fila se indexa la  posicion columna
            posFila = f +1
    return str(posFila) + str(posColumna) 

def coordenadaletra(coorF,CoordC, matriz):
    fila = matriz[coorF-1]
    letra = fila [CoordC-1]
    return letra

def cifrar (matriz,palabra): 
    eqNumerico = ""
    for letra in palabra:
        coordenada = letraCoordenada(letra,matriz) #se ejeuta una funcion para hallar la coordenada de la letra
        eqNumerico += coordenada
    #print(eqNumerico)
    mitad = len(eqNumerico)//2 
    mitadIzq = eqNumerico[:mitad]
    mitadDere = eqNumerico[mitad:]
    
    eqNumericoIntercalado = []
    for i in range(len(mitadIzq)):#recorrido paralelo de las dos mitades
        digitoIzq = mitadIzq[i]
        digitoDer = mitadDere[i]
        coordenadaInter = digitoIzq + digitoDer
        eqNumericoIntercalado.append(coordenadaInter)
    #print(eqNumericoIntercalado)

    palabraCifrada = ""
    for coordenadaInter in eqNumericoIntercalado:
        f = int(coordenadaInter[0])
        c = int(coordenadaInter[1])
        
        letra = coordenadaletra(f,c,matriz)
        palabraCifrada += letra
    return palabraCifrada

matriz = crearMatriz('qwerty')
palabraCifrada = cifrar(matriz, 'informatica')
print(palabraCifrada)

#[ 1   2  3  4  5
#1 [q, w ,e ,r, t]
#2 [y, a, b, c, d]
#3 [f, g, h ,ij, k]
#4 [l, m, n, o, p]
#5 [s, u, v, x, z ]
#]