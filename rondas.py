def rondas(color):
    print("Ingrese los números ganadores de la primera ronda, tablas", color)
    winner=[]
    #esta variable me ayudara continuar el juego
    estadoAmarillo=1;
    for i in range(8):
        print("Ingrese el numero", i+1 ,": ")
        numero=int(input())
        winner.append(numero)
    #convierto la lista en un conjunto
    setWinner = set(winner)
    #abro el fichero
    if(color=="amarilla"):
        fichero = open ("TabllasYelllow.csv","r",)
    if (color == "azul"):
        fichero = open("TablasBlue.csv.csv", "r", )
    if (color == "rojo"):
        fichero = open("TablasRed.csv.csv", "r", )
    #creamos la lista que tendra toddos los conjuntos de tablas amarillas
    tablasAmarillas = []
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
        tablasAmarillas.append(settabla)

    fichero.close()
    #empiezo a recorrer la lista de tablas amarillas
    contador = 0
    ##creamos una lista de semifinalista
    semifinalista = []
    semifinalistaId=[]
    for i in tablasAmarillas:
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
        print("Naide gano, jugaremos un numero mas")
        print("Ingrese el ultimo numero")
        numeroextra= int(input())
        setextra= {numeroextra}
        for i in semifinalista:
            verficadroextra= []
            verficadroextra = i.difference(setextra)
            if len(verficadroextra)==0:
                indiceWinner= semifinalista.index(numeroextra)
                contadorWinner = semifinalistaId[indiceWinner]
                print("Ha ganadp cpm el numero extra con la tabla ", contadorWinner)
                estadoAmarillo=0
                break

    if estadoAmarillo==1:
        print("Se acabo la ronda", color ," nadie gano, siga con la siguiente ronda")