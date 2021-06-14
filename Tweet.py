#usted cuenta con  una cadena de caracteres (tweet)
#se mencionan ayudantes de una materia en especifico
#mostrar ayudante 1
#mostarr ayudante 2
#mostrar ayudante ultimo


tweet= ("El dia de ayer hubo ayudantias con #Joel de FP y #kevin de Cuv ya se divirtieron los pollos, ahora le toca a los gallos con  #alexB ")
pos1 = tweet.index("#")
subtweet1 = tweet[pos1 +1: ] #hago un subtweet desde la posicion #+1 hasta el final
pos2 = subtweet1.index(" ") #index (desde #+1 hasta el espacio)
ayudante1 = subtweet1[:pos2]
print(ayudante1)


pos3 = subtweet1.index("#")
subtweet2 = subtweet1[pos3+1:] #hago un subtweet desde la posicion #+1 del subtweet1 hasta el final
pos4 = subtweet2.index(" ") #index (desde #+1 hasta el espacio)
ayudante2 = subtweet2[:pos4]
print(ayudante2)


#metodo2 para allar el tercer ayudante

pos5 = subtweet1.index("#", pos3+1) #metodo dos de index , buscar "x" a partir de un rango
pos6 = subtweet1.index(" ", pos5) # index (desde #+1 hasta el espacio)
ayudante3 = subtweet1[pos5+1:pos6]
print(ayudante3)

#ultimo ayudante
tweetinv= tweet[::-1]
pos7 = tweetinv.index("#")
subtweetInv = tweetinv[:pos7]
subtweetUltInv = subtweetInv[::-1]
pos8 = subtweetUltInv.index(" ")
ayudanteUltimo = subtweetUltInv[:pos8]
print(ayudanteUltimo)



