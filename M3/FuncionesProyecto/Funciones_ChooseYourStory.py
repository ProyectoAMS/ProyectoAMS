# //////////////// Imports ////////////////

import time
import pymysql

# /////////////////////////////////////////


# ///////////// Conexión a la BBDD //////////////


# Establecer la conexión
conn = pymysql.connect(
    host="20.126.15.242",
    user="azure-admin",
    password="mypass123",
    db="AMS"
)
cursor = conn.cursor()


# ///////////////////////////////////////////////


# //////////////////////////////////////////////////////////////////////// Menú ////////////////////////////////////////////////////////////////////////

#Menú del juego antes de iniciar sesión
def menu_before():
    textOpts = "\n" + " " * 60 + "1.- Iniciar sessió" + "\n" + " " * 60 + "2.- Crear usuari" + "\n" + " " * 60 + "3.- Rejugar Aventuras" + "\n" + " " * 60 + "4.- Reportes" + "\n" + " " * 60 + "5.- Sortir"
    inputOptText = "\n" + " " * 60 + "Escull una opció: "

    lista = [1, 2, 3, 4, 5]
    exceptions = ["w", "e", -1, 0]

    while True:
        titulo = """
        /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                                                 ██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗███████╗
                                                 ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
                                                 ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░█████╗░░
                                                 ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░██╔══╝░░
                                                 ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░███████╗
                                                 ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝
                                 ███████╗░██████╗░█████╗░██╗░░░██╗██╗░░░░░██╗░░░░░  ██╗░░░░░░█████╗░  ████████╗███████╗██╗░░░██╗░█████╗░
                                 ██╔════╝██╔════╝██╔══██╗██║░░░██║██║░░░░░██║░░░░░  ██║░░░░░██╔══██╗  ╚══██╔══╝██╔════╝██║░░░██║██╔══██╗
                                 █████╗░░╚█████╗░██║░░╚═╝██║░░░██║██║░░░░░██║░░░░░  ██║░░░░░███████║  ░░░██║░░░█████╗░░╚██╗░██╔╝███████║
                                 ██╔══╝░░░╚═══██╗██║░░██╗██║░░░██║██║░░░░░██║░░░░░  ██║░░░░░██╔══██║  ░░░██║░░░██╔══╝░░░╚████╔╝░██╔══██║
                                 ███████╗██████╔╝╚█████╔╝╚██████╔╝███████╗███████╗  ███████╗██║░░██║  ░░░██║░░░███████╗░░╚██╔╝░░██║░░██║
                                 ╚══════╝╚═════╝░░╚════╝░░╚═════╝░╚══════╝╚══════╝  ╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝
                                 ██████╗░██████╗░░█████╗░██████╗░██╗░█████╗░  ██╗░░██╗██╗░██████╗████████╗░█████╗░██████╗░██╗░█████╗░
                                 ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗  ██║░░██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗
                                 ██████╔╝██████╔╝██║░░██║██████╔╝██║███████║  ███████║██║╚█████╗░░░░██║░░░██║░░██║██████╔╝██║███████║
                                 ██╔═══╝░██╔══██╗██║░░██║██╔═══╝░██║██╔══██║  ██╔══██║██║░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██║██╔══██║
                                 ██║░░░░░██║░░██║╚█████╔╝██║░░░░░██║██║░░██║  ██║░░██║██║██████╔╝░░░██║░░░╚█████╔╝██║░░██║██║██║░░██║
                                 ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝


          ███████╗░██████╗████████╗███████╗██╗░░░██╗███████╗  ████████╗███████╗██████╗░██████╗░░█████╗░██████╗░░█████╗░░██████╗  ██╗  ██╗██╗░░░░░██╗░░░░░░█████╗░
          ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║░░░██║██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██║  ██║██║░░░░░██║░░░░░██╔══██╗
          █████╗░░╚█████╗░░░░██║░░░█████╗░░╚██╗░██╔╝█████╗░░  ░░░██║░░░█████╗░░██████╔╝██████╔╝███████║██║░░██║███████║╚█████╗░  ██║  ██║██║░░░░░██║░░░░░███████
          ██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░░╚████╔╝░██╔══╝░░  ░░░██║░░░██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║░░██║██╔══██║░╚═══██╗  ██║  ██║██║░░░░░██║░░░░░██╔══██║
          ███████╗██████╔╝░░░██║░░░███████╗░░╚██╔╝░░███████╗  ░░░██║░░░███████╗██║░░██║██║░░██║██║░░██║██████╔╝██║░░██║██████╔╝  ██║  ██║███████╗███████╗██║░░██║
          ╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝░░╚═╝

        ******************************************************************************************************************************************************                               
"""

        print(titulo)
        print("\n")

        opcion = getOpt(textOpts, inputOptText, lista, exceptions)
        print("\n")
        opc = int(opcion)

        if opc == 1:  # Iniciar sessió

            access = login()

            valid = access[0]
            user = access[1]

            if valid == 0:
                menu_before()

            elif valid == -1:
                menu_before()

            elif valid == 1:
                jugar(user)

        elif opc == 2:  # Crear usuario

            createUser()

        elif opc == 3:  # Rejugar aventura

            replayAdventureMenu()

        elif opc == 4:
            reports()

        else:
            quit()

#Menú del juego después de iniciar sesión
def menu_after():
    textOpts = "\n" + " " * 60 + "1.- Tancar sessió" + "\n" + " " * 60 + "2.- Jugar" + "\n" + " " * 60 + "3.- Rejugar Aventuras" + "\n" + " " * 60 + "4.- Reportes" + "\n" + " " * 60 + "5.- Sortir"
    inputOptText = "\n" + " " * 60 + "Escull una opció: "

    lista = [1, 2, 3, 4, 5]

    while True:
        titulo = """
        /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                                                 ██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗███████╗
                                                 ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝
                                                 ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░█████╗░░
                                                 ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░██╔══╝░░
                                                 ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░███████╗
                                                 ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝
                                 ███████╗░██████╗░█████╗░██╗░░░██╗██╗░░░░░██╗░░░░░  ██╗░░░░░░█████╗░  ████████╗███████╗██╗░░░██╗░█████╗░
                                 ██╔════╝██╔════╝██╔══██╗██║░░░██║██║░░░░░██║░░░░░  ██║░░░░░██╔══██╗  ╚══██╔══╝██╔════╝██║░░░██║██╔══██╗
                                 █████╗░░╚█████╗░██║░░╚═╝██║░░░██║██║░░░░░██║░░░░░  ██║░░░░░███████║  ░░░██║░░░█████╗░░╚██╗░██╔╝███████║
                                 ██╔══╝░░░╚═══██╗██║░░██╗██║░░░██║██║░░░░░██║░░░░░  ██║░░░░░██╔══██║  ░░░██║░░░██╔══╝░░░╚████╔╝░██╔══██║
                                 ███████╗██████╔╝╚█████╔╝╚██████╔╝███████╗███████╗  ███████╗██║░░██║  ░░░██║░░░███████╗░░╚██╔╝░░██║░░██║
                                 ╚══════╝╚═════╝░░╚════╝░░╚═════╝░╚══════╝╚══════╝  ╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝
                                 ██████╗░██████╗░░█████╗░██████╗░██╗░█████╗░  ██╗░░██╗██╗░██████╗████████╗░█████╗░██████╗░██╗░█████╗░
                                 ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗  ██║░░██║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗
                                 ██████╔╝██████╔╝██║░░██║██████╔╝██║███████║  ███████║██║╚█████╗░░░░██║░░░██║░░██║██████╔╝██║███████║
                                 ██╔═══╝░██╔══██╗██║░░██║██╔═══╝░██║██╔══██║  ██╔══██║██║░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██║██╔══██║
                                 ██║░░░░░██║░░██║╚█████╔╝██║░░░░░██║██║░░██║  ██║░░██║██║██████╔╝░░░██║░░░╚█████╔╝██║░░██║██║██║░░██║
                                 ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝


          ███████╗░██████╗████████╗███████╗██╗░░░██╗███████╗  ████████╗███████╗██████╗░██████╗░░█████╗░██████╗░░█████╗░░██████╗  ██╗  ██╗██╗░░░░░██╗░░░░░░█████╗░
          ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║░░░██║██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██║  ██║██║░░░░░██║░░░░░██╔══██╗
          █████╗░░╚█████╗░░░░██║░░░█████╗░░╚██╗░██╔╝█████╗░░  ░░░██║░░░█████╗░░██████╔╝██████╔╝███████║██║░░██║███████║╚█████╗░  ██║  ██║██║░░░░░██║░░░░░███████
          ██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░░╚████╔╝░██╔══╝░░  ░░░██║░░░██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║░░██║██╔══██║░╚═══██╗  ██║  ██║██║░░░░░██║░░░░░██╔══██║
          ███████╗██████╔╝░░░██║░░░███████╗░░╚██╔╝░░███████╗  ░░░██║░░░███████╗██║░░██║██║░░██║██║░░██║██████╔╝██║░░██║██████╔╝  ██║  ██║███████╗███████╗██║░░██║
          ╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝░░╚═╝

        ******************************************************************************************************************************************************                               
"""

        print(titulo)
        print("\n")

        opcion = getOpt(textOpts, inputOptText, lista)
        print("\n")
        opc = int(opcion)

        if opc == 1:  # Tancar sessió

            print("Chao, esperem que tornis!!")

            input("Prém ENTER per continuar")

            menu_before()

        elif opc == 2:  # Jugar

            access = login()

            user = access[1]

            jugar(user)

        elif opc == 3:  # Rejugar aventura

            replayAdventureMenu()

        elif opc == 4:

            reports()

        else:
            quit()

#Función para poder comenzar a jugar
def jugar(user):
    valid = False
    lista = [0]

    adventures = get_adventure_with_chars()

    for i in adventures.keys():
        lista.append(i)

    inputOptText = "Quina aventura vols jugar? (0 to Go Back): "

    aventuras = getFormatedAdventures(adventures)

    opc = getOpt(aventuras, inputOptText, lista)

    # Opciones de las aventuras
    if int(opc) == 0:
        menu_after()

    elif int(opc) == 10:

        menu_aventuras(10, user)

    elif int(opc) == 11:

        menu_aventuras(11, user)

    elif int(opc) == 12:

        menu_aventuras(12, user)

#Menú del Rejugar Aventuras
def replayAdventureMenu():
    keys = ("idGame","idUser", "username", "adventure", "characterName", "date")

    columns = (10, 10, 20, 30, 10, 10)

    titulo = """
                                             ██████╗░███████╗██╗░░░██╗██╗██╗░░░██╗  ██╗░░░░░░█████╗░  ████████╗███████╗██╗░░░██╗░█████╗░
                                             ██╔══██╗██╔════╝██║░░░██║██║██║░░░██║  ██║░░░░░██╔══██╗  ╚══██╔══╝██╔════╝██║░░░██║██╔══██╗
                                             ██████╔╝█████╗░░╚██╗░██╔╝██║██║░░░██║  ██║░░░░░███████║  ░░░██║░░░█████╗░░╚██╗░██╔╝███████║
                                             ██╔══██╗██╔══╝░░░╚████╔╝░██║██║░░░██║  ██║░░░░░██╔══██║  ░░░██║░░░██╔══╝░░░╚████╔╝░██╔══██║
                                             ██║░░██║███████╗░░╚██╔╝░░██║╚██████╔╝  ███████╗██║░░██║  ░░░██║░░░███████╗░░╚██╔╝░░██║░░██║
                                             ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░╚═════╝░  ╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝

                                             ░█████╗░██╗░░░██╗███████╗███╗░░██╗████████╗██╗░░░██╗██████╗░░█████╗░
                                             ██╔══██╗██║░░░██║██╔════╝████╗░██║╚══██╔══╝██║░░░██║██╔══██╗██╔══██╗
                                             ███████║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░░██║██████╔╝███████║
                                             ██╔══██║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░░██║██╔══██╗██╔══██║
                                             ██║░░██║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚██████╔╝██║░░██║██║░░██║
                                             ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
"""

    print(" " * 7 + "//" * 90)
    print("\n" * 3)
    print(titulo)
    print("\n" * 3)
    print(" " * 7 + "//" * 90)

    input("\nPrém ENTER per continuar")
    print()

    diccionari = getReplayAdventures()
    
    print(getHeadeForTableFromTuples(("IdGame","idUser", "Username", "Name", "CharacterName", "date"), (10, 10, 20, 30, 10, 10)))

    text = getTableFromDict(keys, diccionari, columns)
    inputText = "Escull una aventura: "
    rangeList = []

    for i, j in diccionari.items():
        rangeList.append(i)

    opcion = int(getOpt(text, inputText, rangeList))

    replay(opcion)

#Menú de reportes
def reports():
    textOpts = "\n" + " " * 50 + "1.- Resposta més utilitzada" + "\n" + " " * 50 + "2.- Jugador amb més partides jugades" + "\n" + " " * 50 + "3.- Jocs jugats per l'usuari" + "\n" + " " * 50 + "4.- Enrere"
    inputOptText = "\n" + " " * 50 + "Escull una opció: "

    lista = [1, 2, 3, 4]
    exceptions = ["w", "e", -1, 0]

    while True:
        titulo = """
                                        ██████╗░███████╗██████╗░░█████╗░██████╗░████████╗░██████╗
                                        ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                                        ██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░
                                        ██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗
                                        ██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝
                                        ╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
"""

        print(" " * 3 + "//" * 60)
        print("\n" + titulo + "\n")
        print(" " * 3 + "//" * 60)

        print("\n")
        opcion = getOpt(textOpts, inputOptText, lista, exceptions)
        opc = int(opcion)
        print("\n")

        # Menú Respostes més jugades
        if opc == 1:
            tupla = (20, 30, 30)
            tupla_texts = []

            query = """

            SELECT CONCAT(A.ID_ADVENTURE," - ",A.adventure_name) as "ID AVENTURA - NOMBRE", 
		    concat(S.ID_STEP, S.step_description) as "ID PASO - DESCRIPCION", 
		    concat(O.answer," - ",O.option_description) as "ID RESPUESTA - DESCRIPCION", 
		    count(D.FK_OPTION_ID_OPTION) as "NÚMERO VECES SELECCIONADA" 
            from AMS.ADVENTURE A 
            INNER JOIN AMS.STEP S ON S.FK_ADVENTURE_ID_ADVENTURE = A.ID_ADVENTURE 
            INNER JOIN AMS.OPTION O ON O.FK_STEP_ID_STEP = S.ID_STEP
            INNER JOIN AMS.DECISION D ON D.FK_OPTION_ID_OPTION = O.ID_OPTION
            group by O.ID_OPTION
            order by count(D.FK_OPTION_ID_OPTION)
            desc limit 1000;"""

            res = list(get_table(query))

            for i in res:
                tupla_texts.append(list(i))

            print()
            print(getFormatedTable(tupla_texts))
            print()

        # Menú Más partidas jugadas
        elif opc == 2:

            query = """ SELECT U.user_name, count(G.FK_USER_ID_USER) from AMS.GAME G 
            INNER JOIN AMS.USER U ON U.ID_USER = G.FK_USER_ID_USER
            group by U.user_name
            order by count(G.FK_USER_ID_USER)
            desc limit 1; """

            # print(getFormatedTable(get_table(query)), title="Player with more games played")

            print(" " * 33 + "Player with most games played")

            print(getHeadeForTableFromTuples(("USUARIO", "PARTIDAS JUGADAS"), (40, 20)))

            cursor.execute(query)

            res = cursor.fetchall()

            for i in res:
                j = list(i)
                cont = 0
                for k in j:

                    cont += 1

                    print(str(k).ljust(40), end=" ")

                    if cont == 2:
                        print("\n")
                        break
                break

            print("\n")

        # Menú Aventuras jugadas por el usuario
        elif opc == 3:

            listBody = []

            query = "SELECT MAX(FK_USER_ID_USER) FROM GAME;"

            cursor.execute(query)

            res = cursor.fetchall()

            for i in res:
                for j in i:
                    idUser = j

            query = f"SELECT A.ID_ADVENTURE, A.adventure_name, G.current_date from AMS.ADVENTURE A INNER JOIN AMS.GAME G ON G.FK_ADVENTURE_ID_ADVENTURE = A.ID_ADVENTURE INNER JOIN AMS.USER U ON G.FK_USER_ID_USER = U.ID_USER where ID_USER = {idUser};"

            diccionari = list(get_table(query))

            getHeadeForTableFromTuples(("ID AVENTURA", "NOMBRE", "FECHA"), (20, 30, 40))

            for i in diccionari:
                listBody.append(list(i))

            listBody.pop(0)

            for k in listBody:
                print("\n")
                for j in k:
                    print(str(j).ljust(10), end=" " * 5)

            print("\n")
            input("Prém ENTER per continuar")
            print("\n")

        else:
            break

#Menú de las aventuras
def menu_aventuras(idAdventure, user):
    fin = """
                            ░░░░░░░░░░░░  ███████╗██╗███╗░░██╗  ░░░░░░░░░░░░
                            ░░░░░░░░░░░░  ██╔════╝██║████╗░██║  ░░░░░░░░░░░░
                            █████╗█████╗  █████╗░░██║██╔██╗██║  █████╗█████╗
                            ╚════╝╚════╝  ██╔══╝░░██║██║╚████║  ╚════╝╚════╝
                            ░░░░░░░░░░░░  ██║░░░░░██║██║░╚███║  ░░░░░░░░░░░░
                            ░░░░░░░░░░░░  ╚═╝░░░░░╚═╝╚═╝░░╚══╝  ░░░░░░░░░░░░
"""

    inputOptText = "Select your Character (0 to Go back): "
    adventure = get_adventure_with_chars()
    characters = get_characters()

    decisiones = ()

    text = " "

    for i, j in adventure.items():

        for k, l in j.items():
            if i == idAdventure:
                if k == "Name":
                    titulo = str(l)

                if k == "Description":
                    descripcion = str(l)

    getHeader(titulo)
    print("Adventure:".ljust(20), titulo, "\n")
    print("Description:".ljust(20), descripcion, "\n\n")

    print("=" * 20 + "Characters" + "=" * 20)

    for j, k in characters.items():

        if idAdventure == 10:

            if j == 1:
                print(f"{j}) {k}")
            elif j == 2:
                print(f"{j}) {k}")

        elif idAdventure == 11:

            if j == 3:
                print(f"{j}) {k}")

        elif idAdventure == 12:

            if j == 4:
                print(f"{j}) {k}")

    opc = getOpt(text, inputOptText, rangeList=[0, 1, 2, 3, 4])

    if int(opc) == 0:
        menu_after()

    elif int(opc) == 1 or int(opc) == 2 or int(opc) == 3 or int(opc) == 4:

        char = get_characters()

        userInfo = getUserIds()

        idUser = userInfo[0].index(user) + 1

        for i, j in char.items():
            if int(opc) == i:
                print(f"Has seleccionat a {j}")
                charac = i

                insertCurrentGame(idUser, charac, idAdventure)

        input("\nPrém ENTER per continuar\n")

        text = titulo
        getHeader(text)
        print()

        # print(get_id_bystep_adventure(idAdventure))
        sql5 = f"SELECT * FROM AMS.STEP where ID_STEP = {get_first_step_adventure(idAdventure)}"  # printa el primer paso
        cursor.execute(sql5)
        step = cursor.fetchall()

        for i in step:
            opt = i[1]
            print(opt)
        print('Opcions:\n')

        sql1 = f"SELECT * FROM AMS.OPTION where FK_STEP_ID_STEP = {get_first_step_adventure(idAdventure)}"  # printa las opciones el primer paso
        cursor.execute(sql1)
        option = cursor.fetchall()
        for i in option:
            ids = i[0]
            opts = i[1]
            print(" " * 2 + str(ids), ')', opts)
            print()

    while True:
        while True:

            resFinal = 0

            sql6 = f"SELECT * FROM GAME"
            cursor.execute(sql6)
            option = cursor.fetchall()
            for i in option:
                id = i[0]
            game = id

            if resFinal == 1:
                print(fin)
                print("\n")
                input("Prém ENTER per continuar")
                menu_after()
            else:
                option = int(input('\nSelect Option: \n'))

            insertCurrentChoice(game, idUser, idAdventure, charac, option)

            sql3 = f"SELECT * FROM AMS.OPTION where ID_OPTION = {option}"  # mira la opcion
            cursor.execute(sql3)
            option = cursor.fetchall()

            for i in option:
                go = i[3]
            go_step = go

            sql2 = f"SELECT * FROM AMS.STEP where ID_STEP = {go_step}"
            cursor.execute(sql2)
            step = cursor.fetchall()

            text = titulo
            getHeader(text)
            print()

            for i in step:
                final = i[2]
                resFinal = int.from_bytes(final, byteorder="little")
                opt = i[1]
                print(opt)
                print()

            sql4 = f"SELECT * FROM AMS.OPTION where FK_STEP_ID_STEP = {go_step}"
            cursor.execute(sql4)
            option = cursor.fetchall()

            for i in option:
                id = i[0]
                opt = i[1]
                print(id, ')', opt)
                print()

            if resFinal == 1:
                print(fin)
                print("\n")
                input("Prém ENTER per continuar")
                menu_after()

            break


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# /////////////////////////////////////////////////////////////// Funciones de formato ///////////////////////////////////////////////////////////////

#Función para obtener opciones
def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[], **dictionary):
    while True:
        print(textOpts + "\n")

        opcion = input(f"{inputOptText}")

        print()

        if not opcion.isdigit():
            print("Opció invàlida")
        elif int(opcion) < rangeList[0] or int(opcion) > rangeList[-1]:
            print("Opció invàlida")
        elif opcion in exceptions == False or opcion in rangeList == False:
            print("Opció invàlida")
        else:
            break

    return opcion

#Función para printar información de un diccionario en forma de tabla
def getTableFromDict(tuple_of_keys, diccionari, weigth_of_columns):
    weigth_of_columns = list(weigth_of_columns)

    for i, j in diccionari.items():
        pos = 0
        print(str(i).ljust(10), end=" ")
        for k, l in j.items():
            if pos == 5:
                print("\n")

            if k in tuple_of_keys:
                print(str(l).ljust(weigth_of_columns[pos]), end=" ")
                pos += 1

    return " "

#Función para formatear texto
def formatText(texts, lenLine, split="\n"):
    
    textoGeneral = ""
    
    for i in texts:
        textoGeneral += i + " "
        
    texts = textoGeneral.split("\n")
    
    cuerpo = ""

    for i in texts:
        listBody = []
        body(listBody, str(i), lenLine)

        if len(str(i)) > lenLine:
            for i in listBody:
                if listBody != listBody[len(listBody) - 1]:
                    cuerpo += i + str(split)
        else:
            cuerpo+=i
    return cuerpo

def body(listBody, texto, tuple_sizes, i = 0):

    if i + tuple_sizes >= len(texto):
        listBody.append(texto[i:])
        return listBody
    else:
        k = spaces(texto[i:i+tuple_sizes])
        listBody.append(k[:len(k) - 1])
        body(listBody , texto, tuple_sizes,i + len(k))

def spaces(texto):
    if texto[len(texto) - 1] != " ":
        return spaces(texto[:len(texto) - 1])
    else:
        return texto


listaFinalColumnas = []
#Función para obtener columnas de texto ordenadas
def getFormatedBodyColumns(tupla_texts, tupla_sizes, margin=2):
    tupla_texts = list(tupla_texts)
    tupla_sizes = list(tupla_sizes)
    for t in range(len(tupla_texts)):
        l = tupla_texts[t].split(" ")
        lista_Frases = []
        for i in range(len(l)):
            if not l[i] == l[-1]:
                l[i] += " "
        contador = 0
        for i in range(len(l)):
            contador += len(l[i])
            if contador <= tupla_sizes[t] or contador == tupla_sizes[t] + 1:
                lista_Frases.append(l[i])
            else:
                lista_Frases.append("\n" + l[i])

                contador = len(l[i])
        frase = ""
        for i in range(len(lista_Frases)):
            frase += lista_Frases[i]
        ListaFinal = frase.split("\n")
        listaFinalColumnas.append(ListaFinal)

    # PARA PRINTARLO
    linea = ""
    textLinea = []
    textsLinees = []
    for j in range(len(listaFinalColumnas)):
        textLinea.append(linea + " " * (tupla_sizes[j - 1] + margin - len(linea)))
        linea = ""
        textLinea = []
        c = 0
        for i in listaFinalColumnas[j]:
            c += 1
            if len(tupla_texts[j]) < tupla_sizes[j]:
                if c == len(listaFinalColumnas[j]):
                    linea += i + " " * ((tupla_sizes[j] + margin) - len(linea))
                    textLinea.append(linea)
                    linea = ""
                else:
                    linea += i + " "
            elif len(linea) + len(i) + 1 + margin > tupla_sizes[j]:
                linea += " " * (tupla_sizes[j] + margin - len(linea))
                textLinea.append(linea)
                linea = ""
                linea += i + " "
            else:
                linea += i + " "
        textsLinees.append(textLinea)
    textLinea.append(linea + " " * (tupla_sizes[j] + margin - len(linea)))

    if len(textsLinees[0]) > len(textsLinees[1]) and len(textsLinees[0]) > len(textsLinees[2]):
        c = 0
    elif len(textsLinees[1]) > len(textsLinees[0]) and len(textsLinees[1]) > len(textsLinees[2]):
        c = 1
    else:
        c = 2
    for j in range(len(textsLinees)):
        if len(textsLinees[j]) <= len(textsLinees[c]):
            for i in range(len(textsLinees[c]) - len(textsLinees[j])):
                textsLinees[j].append(" " * tupla_sizes[j])
    for i in range(len(textsLinees[c])):
        print(textsLinees[0][i], end="")
        print(textsLinees[1][i], end="")
        print(textsLinees[2][i])
        
    return " "

#Función para obtener una tabla formateada de la query que desees
def getFormatedTable(queryTable, title="Most used answer"):
    listQuery = list(queryTable)
    listTitle = []
    listBody = []

    for i in listQuery[0]:
        listTitle.append(i)

    for i in listQuery[len(listQuery) - 1]:
        listBody.append(str(i))

    sizes = (20, 30, 30, 20, 20)

    print("=" * 52 + title + "=" * 52 + "\n")
    for i in listTitle:
        print(str(i).ljust(30), end=" ")
    print("\n" + "*" * 120)
    
    for i in listBody:
        print(getFormatedBodyColumns(tuple(listBody), sizes, margin=3))

    return " "

#Función para obtener el header para una tabla
def getHeadeForTableFromTuples(t_name_columns, t_size_columns, title=""):
    cont1 = 0
    cont2 = 0
    dic1 = []
    dic2 = []

    print("=" * 100)
    '''print("column1".ljust(10)+"column2".ljust(20)+"column3".ljust(30))
    print(t_name_columns[0])
    print(t_size_columns[0])'''

    while cont1 != len(t_name_columns):
        # print(t_name_columns[cont1])
        dic1.append(t_name_columns[cont1])
        cont1 += 1
    while cont2 != len(t_size_columns):
        # print(t_size_columns[cont2])
        dic2.append(t_size_columns[cont2])
        cont2 += 1

    cont1 = 0
    cont2 = 0
    # print(dic1, dic2,"\n")

    column = []
    while cont1 != len(dic1):
        column.append(dic1[cont1].ljust(dic2[cont2]))
        cont1 += 1
        cont2 += 1
    # print(column)
    print("".join(column))
    print("*" * 100)

    return " "

#Función para printar la tabla de aventuras
def getFormatedAdventures(adventures):
    l = 60
    r = 60
    medio = len("Adventures")
    num = medio / 2
    l = l - num
    r = r - num

    print("=" * int(l) + "Adventures" + "=" * int(r))
    print("Id Adventure".ljust(12), "Adventure".ljust(40), "Description")
    print("*" * 110)

    for i in adventures:
        print(str(i).ljust(12), adventures[i]["Name"].ljust(40), adventures[i]["Description"])

    return " "

#Función para obtener un header con el título que quieras
def getHeader(text):
    l = 50
    r = 50
    medio = len(text)
    num = medio / 2
    l = l - num
    r = r - num

    print("*" * 100)
    print("=" * int(l) + text + "=" * int(r))
    print("*" * 100)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# //////////////////////////////////////////////////////////// Funciones de usuario /////////////////////////////////////////////////////////////////

#Función de logeo
def login():
    user = " "
    password = " "

    chequeo = checkUserbdd(user, password)

    valid = chequeo[0]
    user = chequeo[1]

    userInfo = getUser()

    if valid == 0:
        print("Usuari no existeix")
        return 0, user

    elif valid == -1:
        print("Contrasenya incorrecta")
        return -1, user

    elif valid == 1:

        for i in userInfo:
            print(f"Hola {user}, anem a jugar!!\nQuina aventura vols jugar?\n\n")
            return 1, user

#Función que revisa si el usuario que inicia sesión
#se encuentra en la BBDD
def checkUserbdd(user, password):
    correct = False
    mycursor = conn.cursor()
    mycursor.execute('SELECT user_name FROM AMS.USER')
    user = mycursor.fetchall()
    lista1 = []
    lista2 = []

    for i in user:
        users = i[0]
        lista1.append(users)
    mycursor = conn.cursor()
    mycursor.execute('SELECT password FROM AMS.USER')
    contrasenya1 = mycursor.fetchall()
    for j in contrasenya1:
        password = j[0]
        lista2.append(password)

    while correct == False:

        usuari = input("Usuari a trobar: ")
        contrasenya = input("Contrasenya: ")

        if usuari in lista1:
            print('Usuari trobat')
            if contrasenya in lista2:
                correct = True
                return 1, usuari
            else:
                return -1, usuari
        else:
            return 0, usuari

#Función que revisa los requisitos de la contraseña
def checkPassword(password):
    valid = False

    while valid == False:

        if len(password) < 8 or len(password) > 12:
            print("La contrasenya ha de tenir més de 8 caracters")
            return False
        else:

            minuscula = False
            for minus in password:
                if minus.islower() == True:
                    minuscula = True
            if not minuscula:
                print("Ha de tenir minúscules")
                return False

            mayusculas = False
            for mayus in password:
                if mayus.isupper() == True:
                    mayusculas = True
            if not mayusculas:
                print("Ha de portar majúscules")
                return False

            num = False
            for digit in password:
                if digit.isdigit() == True:
                    num = True
            if not num:
                print("La contrasenya ha de tenir números")
                return False

            if password.count(" ") > 0:
                print("No pot tenir espais en blanc")
                return False

            else:
                return True

#Función que revisa los requisitos del usuario
def checkUser(user):
    i = False

    while i == False:
        if len(user) < 6:
            print("El nom d'usuari ha de contenir almenys 6 carácters")
            return False

        elif len(user) > 12:
            print("El nom d'usuari no pot contenir més de 12 carácters")
            return False

        elif user.isalnum() != True:
            print("El nom d'usuari pot contenir només lletres i números")
            return False

        elif user.isalpha() == True:
            print("El nom d'usuari ha de contenir almenys un dígit")
            return False

        elif user.count(" ") > 0:
            print("El nom d'usuari no pot tenir espais en blanc")
            return False
        else:
            i = True
            return True

#Función que revisa si el usuario existe
def userExists(user):
    cursor.execute("SELECT user_name FROM USER")

    res = cursor.fetchall()

    if user in res:
        return True
    else:
        return False

#Función para crear un usuario
def createUser():
    userOK = False
    passOK = False

    while userOK != True:
        user = input("Introdueixi un nom d'usuari (Té que ser alfanúmeric): ")
        print()

        if checkUser(user) == True:
            userOK = True

    while passOK != True:
        password = input("Introdueix la contrasenya: ")
        print()

        if checkPassword(password) == True:
            passOK = True

    insertUser(user, password)

    print("Usuari creat satisfactoriament")
    print()
    return input("Prém per continuar")

#Función para insertar el usuario creado en la BBDD
def insertUser(user, password):
    query = f"INSERT INTO AMS.USER (user_name, password) values ('{user}','{password}')"

    cursor.execute(query)

    res = cursor.fetchall()

    print(res)

    conn.commit()

#Función para obtener a los usuarios en la BBDD
def getUser():
    diccionario = {}
    cursor.execute('SELECT * FROM USER')

    user = cursor.fetchall()
    for i in user:
        id = i[0]
        users = i[1]
        password = i[2]
        diccionario1 = {users: {'Password': password, 'IdUser': id}}
        diccionario.update(diccionario1)

    return diccionario

#Función para obtener los IDs de los usuarios en la BBDD
def getUserIds():
    mycursor = conn.cursor()
    mycursor.execute('SELECT user_name FROM USER')
    user = mycursor.fetchall()
    lista1 = []
    lista2 = []
    listafinal = []

    for i in user:
        users = i[0]
        lista1.append(users)

    mycursor = conn.cursor()
    mycursor.execute('SELECT ID_USER FROM USER')
    id = mycursor.fetchall()

    for j in id:
        ids = j[0]
        lista2.append(ids)
    listafinal.append(lista1)
    listafinal.append(lista2)

    return listafinal


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# ///////////////////////////////////////////////////////////////// Funcions d'accés a BBDD ////////////////////////////////////////////////////////////////

#Función para insertar el juego actual en la BBDD
def insertCurrentGame(idUser, idChar, idAdventure):
    tiempo = time.strftime('%Y-%m-%d %H:%M:%S')

    sql = f"INSERT INTO AMS.GAME (`current_date`,FK_USER_ID_USER,FK_ADVENTURE_ID_ADVENTURE,FK_CHARACTER_ID_CHARACTER) VALUES ('{tiempo}','{idUser}','{idAdventure}','{idChar}')"
    mycursor = conn.cursor()
    mycursor.execute(sql)
    conn.commit()

#Función para insertar las opciones de la aventura actual en la BBDD
def insertCurrentChoice(game, idUser, idAdventure, idChar, idOption):
    sql = f"INSERT INTO AMS.DECISION (FK_GAME_ID_GAME,FK_GAME_USER_ID_USER,FK_GAME_ADVENTURE_ID_ADVENTURE,FK_GAME_CHARACTER_ID_CHARACTER,FK_OPTION_ID_OPTION) VALUES ('{game}','{idUser}','{idAdventure}','{idChar}','{idOption}')"
    mycursor = conn.cursor()
    mycursor.execute(sql)
    conn.commit()

#Función para obtener el primer paso de una aventura
def get_first_step_adventure():
    while True:
        aventura = input('Aventura')
        if aventura == '10' or aventura == '11' or aventura == '12':
            mycursor = conn.cursor()
            sql1 = f"SELECT * FROM STEP WHERE FK_ADVENTURE_ID_ADVENTURE= {aventura} "
            mycursor.execute(sql1)
            user = mycursor.fetchall()
            lista = []
            for i in user[0]:
                lista.append(i)
            id = lista[0]
            description = lista[1]
            lista2 = []
            lista2.append(id)
            lista2.append(description)
            print(lista2)
            break
        else:
            print('No es possible aquesta opció')

#Función para obtener las aventuras con los personajes que pueden jugarla
def get_adventure_with_chars():
    lista = []
    diccionario = {}

    mycursor = conn.cursor()
    char = conn.cursor()

    sql = 'SELECT * FROM CHARACTER_HAS_ADVENTURE'
    sql1 = 'SELECT * FROM ADVENTURE'
    mycursor.execute(sql)

    charac = mycursor.fetchall()

    for j in charac:
        id_char = j[0]
        lista.append(id_char)

    mycursor.execute(sql1)
    adventures = mycursor.fetchall()

    for i in adventures:
        id_adventure = i[0]
        name_adventure = i[1]
        description_adventure = i[2]
        diccionario1 = {
            id_adventure: {'Name': name_adventure, 'Description': description_adventure, 'Characters': lista}}
        diccionario.update(diccionario1)

    return diccionario

#Función para setear el id del juego en la BBDD
def SetIdGame():
    times = time.strftime('%Y-%m-%d %H:%M:%S')
    idUser = " "  # getUserId()
    idAdventure = " "
    idChar = " "

    sql = f"INSERT INTO AMS.GAME (current_data,FK_USER_ID_USER,FK_ADVENTURE_ID_ADVENTURE,FK_CHARACTER_ID_CHARACTER) VALUES('{times}','{idUser}','{idAdventure}','{idChar}')"

    mycursor = conn.cursor()
    mycursor.execute(sql)

    conn.commit()

#Función para obtener una tupla de la query introducida
def get_table(query):
    cursor.execute(query)
    res = list(cursor.fetchall())

    nums_fields = len(cursor.description)

    fields_names = tuple([i[0] for i in cursor.description])
    res.insert(0, fields_names)

    return tuple(res)

#Función para obtener las aventuras ya jugadas
def getReplayAdventures():
    dictGame = {}
    dictUser = {}

    query1 = """SELECT G.ID_GAME, U.ID_USER, U.user_name, A.ID_ADVENTURE, A.adventure_name, G.current_date, C.ID_CHARACTER, C.character_name FROM AMS.USER U
        INNER JOIN AMS.GAME G ON U.ID_USER = G.FK_USER_ID_USER
        INNER JOIN ADVENTURE A ON A.ID_ADVENTURE = G.FK_ADVENTURE_ID_ADVENTURE
        INNER JOIN AMS.CHARACTER C ON C.ID_CHARACTER = G.FK_CHARACTER_ID_CHARACTER;"""

    cursor.execute(query1)

    game = cursor.fetchall()

    for i in game:
        idGame = i[0]
        idUser = i[1]
        user_name = i[2]
        idAdventure = i[3]
        adventure_name = i[4]
        date = i[5]
        idCharacter = i[6]
        characterName = i[7]

        dictUser = {
            idGame: {'idUser': idUser, 'username': user_name, 'idAdventure': idAdventure, 'adventure': adventure_name,
                     'characterName': characterName, 'date': date, 'idCharacter': idCharacter}}
        dictGame.update(dictUser)

    return dictGame

#Función para obtener los personajes
def get_characters():
    diccionario = {}
    mycursor = conn.cursor()
    mycursor.execute('SELECT * FROM AMS.CHARACTER')
    user = mycursor.fetchall()
    for i in user:
        id = i[0]
        name = i[1]
        diccionario1 = {id: name}
        diccionario.update(diccionario1)

    return diccionario

#Función para obtener la id del juego
def get_id_game():
    mycursor = conn.cursor()
    mycursor.execute('SELECT * FROM GAME')
    game = mycursor.fetchall()
    for i in game:
        id = i[0]
        return id

#Función para obtener las decisiones durante el juego
def getChoices():
    '''Una vegada hem triat l'aventura que volem reviure, get choices ens retorna una tupla
    on els components són les tuples (idByStep_Adventure, idAnswers_ByStep_Adventure),
    que ens permetran reviure una aventura donada'''

    cur = conn.cursor()
    query3 = ''' SELECT D.FK_GAME_ID_GAME, D.FK_OPTION_ID_OPTION, O.answer from AMS.DECISION D 
    inner join AMS.OPTION O on D.FK_OPTION_ID_OPTION = O.ID_OPTION '''

    cur.execute(query3)
    choices = cur.fetchall()

    # input("\nPulsar")
    return choices

#Función para obtener el diccionario de las respuestas de los pasos de las aventuras
def get_answers_bystep_adventure():
    dictGeneral = {}

    dict = {}

    query = """
    SELECT concat("(",O.answer,",",O.FK_STEP_ADVENTURE_ID_ADVENTURE,")") as "Tupla de decisiones", 
    (SELECT S.step_description from STEP S where ID_STEP = O.FK_STEP_ID_STEP) as "Descripción", 
    O.answer as "Respuesta",
    O.go_step as "Next Step" from AMS.OPTION O;"""

    cursor.execute(query)

    res = cursor.fetchall()

    for i in res:
        idTuplas = i[0]
        description = i[1]
        answer = i[2]
        next_step = i[3]

        dict = {idTuplas: {'Description': description, 'answer': answer, 'NextStep': next_step}}
        dictGeneral.update(dict)

    return dictGeneral

#Función para obtener el primer paso de una aventura
def get_first_step_adventure(idAdventure):
    sql1 = f"SELECT * FROM STEP WHERE FK_ADVENTURE_ID_ADVENTURE= {idAdventure} "
    cursor.execute(sql1)
    user = cursor.fetchall()
    lista = []
    for i in user[0]:
        lista.append(i)
    id = lista[0]
    description = lista[1]
    lista2 = []
    lista2.append(id)
    lista2.append(description)
    return id

#Función para obtener la id de los pasos de una aventura
def get_id_bystep_adventure(id_adventure):
    query = f"SELECT STEP.ID_STEP,step_description,STEP.end, AMS.OPTION.ID_OPTION from ADVENTURE  inner join STEP  on ADVENTURE.ID_ADVENTURE = STEP.FK_ADVENTURE_ID_ADVENTURE inner join AMS.OPTION  on  AMS.OPTION.FK_STEP_ID_STEP = STEP.ID_STEP where ID_ADVENTURE = '{id_adventure}' "
    cursor.execute(query)
    data = cursor.fetchall()
    dict = {}
    query1 = f"SELECT STEP.ID_STEP,step_description,STEP.end from ADVENTURE  inner join STEP  on ADVENTURE.ID_ADVENTURE= STEP.FK_ADVENTURE_ID_ADVENTURE where end= 1 and ADVENTURE.ID_ADVENTURE = '{id_adventure}'"
    cursor.execute(query1)
    data_end = cursor.fetchall()
    for i in data:
        if i[0] not in dict.keys():
            dict[i[0]] = {"Description": i[1], "Final_Step": 0}
            aux = []
            for j in data:
                if j[0] == i[0]:
                    aux.append(j[3])
            dict[i[0]]["asnwers_in_step"] = tuple(aux)
    for i in data_end:
        dict[i[0]] = {"Description": i[1], "Final_Step": 1, "asnwers_in_step": {}}
    return dict

#Función que nos permite rejugar una historia
def replay(choice):
    # --CONSULTA--
    cur = conn.cursor()
    query1 = f"""select adventure_name, description, ID_ADVENTURE from ADVENTURE 
    where id_adventure=(select FK_ADVENTURE_ID_ADVENTURE from GAME where ID_GAME= {choice});"""
    cur.execute(query1)
    title = cur.fetchall()

    print()
    getHeader(str(title[0][0]))
    formatText(str(title[0][1]), 100)
    cur.close()
    print()
    input("\n\nPrém ENTER per continuar")

    # --CONSULTA--
    cur = conn.cursor()
    query2 = f"""select d.ID_DECEISION ,s.ID_STEP, s.step_description, o.ID_OPTION, o.option_description, o.go_step, 
    (select s.step_description from STEP s where o.go_step = s.ID_STEP)
    from AMS.OPTION o inner join AMS.STEP s on o.FK_STEP_ID_STEP =s.ID_STEP
    inner join AMS.DECISION d on o.ID_OPTION = d.FK_OPTION_ID_OPTION
    where FK_GAME_ID_GAME= {choice};"""

    cur.execute(query2)
    history = cur.fetchall()
    
    cont = 0
    print(history)
    for i in history:
        if cont > 1:
            pass
        else:
            print(formatText(str(i[2]), 90))
            print("\n")
        cont+=1
        print(formatText(str(i[3]), 90))
        print("\n")
        print(formatText(str(i[4]), 90))
        print("\n")
        print(formatText(str(i[6]), 90))
        print("\n")
    
    print("\n")
    getHeader("FIN")
    input("Enter to go menu")
    
    cur.close()
    conn.close()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
