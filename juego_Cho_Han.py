from random import*

billetera = 10
contadorWin = 0
continuar = "si"
print("----Bienvenido a Cho - Han---")
print("Usted tiene ${} en la billetera".format(billetera))
while billetera >0 and continuar == "si" :
    apuesta = int(input("Ingrese apuesta: "))
    if apuesta <= billetera:
        dado1 = randint(1,6)
        dado2 = randint(1,6)
        total = dado1 + dado2
        resto = total % 2
        parimpar = input("adivine Cho o Han? ").title()
        print("Salió: {} + {} = {}".format(dado1,dado2,total))
        if resto == 0 and parimpar == "Cho":
            print("usted gano")
            billetera += apuesta
            contadorWin+=1
        elif resto !=0 and parimpar == "Han":
            print("usted gano")
            billetera += apuesta
            contadorWin+=1
        else:
            print("perdio ")
            billetera-= apuesta
        print("Billetera actual :", billetera)
        if billetera != 0:
            continuar = input("Desea seguir  jugando <Si / No > ").lower()
            print("-------------")
    else:
        print("la apuesta es mayor al dinero que tiene en la billetera")
print("Usted gano {} partidas ".format(contadorWin))

