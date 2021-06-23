import string
def crearMatriz(palabra):

    listaAbc = list(string.ascii_lowercase)
    listaClave = list(palabra)

    for caracClave in listaClave: # remueve los caracteres dados por el parametro
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
        coordenada = letraCoordenada(letra,matriz) #se ejeuta otra funcion dentro
        eqNumerico += coordenada# que recibe la letra y la matriz
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