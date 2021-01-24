def rondas(color):
    winner=[]
    contador = 1
    # esta variable me ayudara continuar el juego
    estadoAmarillo = 1;
    if (color == "amarilla"):
        print("Ingrese los 14 números ganadores de la primera ronda, las tablas de color ", color)
        while(len(winner) < 14):
            print("Ingrese el número: ", contador, ": ")
            try:
                numero = int(input())
                if(numero <= 20):
                    winner.append(numero)
                    contador = contador+ 1
                else:
                    print("Numero Inválido")
            except:
                print("Numero Inválido")

        fichero = open("TablasAmarillas.csv", "r", )
    if (color == "azul"):
        print("Ingrese los 14 números ganadores de la primera ronda, las tablas de color ", color)
        while(len(winner) < 14):
            print("Ingrese el número: ", contador, ": ")
            try:
                numero = int(input())
                if(numero <= 20):
                    winner.append(numero)
                    contador = contador+ 1
                else:
                    print("Numero Inválido")
            except:
                print("Numero Inválido")
        fichero = open("TablasAzules.csv", "r", )
    if (color == "rojo"):
        print("Ingrese los 11 números ganadores de la primera ronda, las tablas de color ", color)
        while(len(winner) < 11):
            print("Ingrese el número: ", contador, ": ")
            try:
                numero = int(input())
                if(numero <= 20):
                    winner.append(numero)
                    contador = contador+ 1
                else:
                    print("Numero Inválido")
            except:
                print("Numero Inválido")
        fichero = open("TablasRojas.csv", "r", )

    #convierto la lista en un conjunto
    setWinner = set(winner)

    #creamos la lista que tendra toddos los conjuntos de tablas
    tablas = []
    while(True):
        linea = fichero.readline()
        if not linea:
            break

        #quitamos el salto de liena
        lienaNuena= linea.rstrip()
        listatabla = lienaNuena.split(" ")
        #convertimos la lista str en una lista con int
        for i in range(len(listatabla)):
            listatabla[i] = int(listatabla[i])

        #creamos los conjuntos
        settabla = set(listatabla)
        #los agregaamos a lista de tablas amarillas
        tablas.append(settabla)

    fichero.close()

    #empiezo a recorrer la lista de tablas amarillas
    contador = 0

    ##cream1os una lista de semifinalista
    semifinalista = []
    semifinalistaId=[]

    for i in tablas:
        contador= contador + 1
        #conjutno digerencia entre la tabla particpante y el jugo ganador
        verificador = setWinner.difference(i)
        #si no hay diferencia entre las tablas hubo un ganador
        if len(verificador)==0:
            print("Ha ganado!!!!!!!, con el id: ", contador)
            estadoAmarillo=0
            break
        #si solo hay 1 elemento en la difernecia se ingresa en las listas de seminfinal
        elif len(verificador)==1:
            semifinalistaId.append(contador)
            semifinalista.append(verificador)

    if estadoAmarillo==1:
        print("Nadie ganó, jugaremos un número mas!!")
        print("Ingrese el último numero:")
        numeroextra= int(input())
        setextra= {numeroextra}
        for i in semifinalista:
            verficadroextra= []
            verficadroextra = i.difference(setextra)
            if len(verficadroextra)==0:
                indiceWinner= semifinalista.index(numeroextra)
                contadorWinner = semifinalistaId[indiceWinner]
                print("Ha ganado com el número extra con la tabla ", contadorWinner)
                estadoAmarillo=0
                break

    if estadoAmarillo==1:
        print("Se acabó la ronda ", color ," Nadie gano, siga con la siguiente ronda!")

print("*****Bingo 2,0*****")
ronda1= "amarilla"
ronda2= "azul"
ronda3= "rojo"

rondas(ronda1)
rondas(ronda2)
rondas(ronda3)