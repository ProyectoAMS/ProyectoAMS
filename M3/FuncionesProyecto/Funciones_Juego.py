#//////////////// Imports ////////////////

import datetime
import time
import pymysql

#/////////////////////////////////////////



#///////////// Conexión a la BBDD //////////////

#Establecer la conexión
conn = pymysql.connect(
    host="40.68.208.129",
    user="azure-admin",
    password = "mypass123",
    db = "AMS"
)

cursor = conn.cursor()

#///////////////////////////////////////////////



#//////////////////////////////////////////////////////////////////////// Variables globales ////////////////////////////////////////////////////////////////////////

diccionari={
    4: {'idUser': 2, 'username': 'Jordi', 'idAdventure':1, 
        'adventure': 'Este muerto esta muy vivo',
        'characterName':'Beowulf',
        'date': datetime.datetime(2021, 11, 28, 18, 17, 20),
        'idCharacter': 1, 
        },
     
    5: {'idUser': 2, 'username': 'Jordi','idAdventure': 1, 
        'adventure': 'Este muerto esta muy vivo',
        'characterName': 'Beowulf', 
        'date': datetime.datetime(2021, 11, 26,13, 28, 36), 
        'idCharacter': 1,
        }}

#---------------------------------------------------------------------------

getTable = (
    ('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA - DESCRIPCION', 'NUMERO VECES SELECCIONADA'),
     
    ('10 - Todos los héroes ','necesitan su princesa', 
    '101 - Son las 6 de la mañana, personajes  est├í profundamente dormido. Le suena la alarma!', 
    '101 - Apaga la alarma porque quiere dormir, han sido días muy duros y personajes necesita un descanso.', 7), 

    ('10 - Todos los héroes necesitan su princesa', '103 - Nuestro héroe personaje se viste rápidamente y van dirección al ciber, hay mucho jaleo en la calle, también mucha policía.', '108 - Entra en el ciber a revisar si la princesa Wyoming sigue dentro.', 5)
)

#---------------------------------------------------------------------------

#get_table()

query = "select username as NOMBRE, descripcion as DESCRIPCION from User"


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




#//////////////////////////////////////////////////////////////////////// Menú ////////////////////////////////////////////////////////////////////////

def menu_before():
    
    textOpts= "\n" + " "*60 +  "1.- Iniciar sessió" + "\n" + " "*60 + "2.- Crear usuari" + "\n" + " "*60 + "3.- Rejugar Aventuras" + "\n" + " "*60 + "4.- Reportes" + "\n" + " "*60 + "5.- Sortir"
    inputOptText="\n" + " "*60 + "Escull una opció: "
    
    lista = [1,2,3,4,5]
    exceptions = ["w","e",-1,0]
    
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
                                 
                                 
                                 ███████╗░██████╗████████╗███████╗██╗░░░██╗███████╗  ████████╗███████╗██████╗░██████╗░░█████╗░██████╗░░█████╗░░██████╗
                                 ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║░░░██║██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
                                 █████╗░░╚█████╗░░░░██║░░░█████╗░░╚██╗░██╔╝█████╗░░  ░░░██║░░░█████╗░░██████╔╝██████╔╝███████║██║░░██║███████║╚█████╗░
                                 ██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░░╚████╔╝░██╔══╝░░  ░░░██║░░░██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║░░██║██╔══██║░╚═══██╗
                                 ███████╗██████╔╝░░░██║░░░███████╗░░╚██╔╝░░███████╗  ░░░██║░░░███████╗██║░░██║██║░░██║██║░░██║██████╔╝██║░░██║██████╔╝
                                 ╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░
                                 
                                 ██╗  ██╗██╗░░░░░██╗░░░░░░█████╗░
                                 ██║  ██║██║░░░░░██║░░░░░██╔══██╗
                                 ██║  ██║██║░░░░░██║░░░░░███████║
                                 ██║  ██║██║░░░░░██║░░░░░██╔══██║
                                 ██║  ██║███████╗███████╗██║░░██║
                                 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝░░╚═╝

        ******************************************************************************************************************************************************                               

"""
    
        print(titulo)
        print("\n")
        
        opcion = getOpt(textOpts,inputOptText,lista, exceptions)
        print("\n")
        opc = int(opcion)
        
        if opc == 1: # Iniciar sessió
            
            access = login()
            
            if access == 0:
                menu_before()
            elif access == -1:
                menu_before
            elif access == 1:
                jugar()
            
        elif opc == 2: # Crear usuario
            
            createUser()
            
        elif opc == 3: # Rejugar aventura
            pass
            
        elif opc == 4:
            reports()
            
        else:
            quit()


def menu_after():
    
    textOpts= "\n" + " "*60 +  "1.- Tancar sessió" + "\n" + " "*60 + "2.- Jugar" + "\n" + " "*60 + "3.- Rejugar Aventuras" + "\n" + " "*60 + "4.- Reportes" + "\n" + " "*60 + "5.- Sortir"
    inputOptText="\n" + " "*60 + "Escull una opció: "
    
    lista = [1,2,3,4,5]
    
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
                                 
                                 
                                 ███████╗░██████╗████████╗███████╗██╗░░░██╗███████╗  ████████╗███████╗██████╗░██████╗░░█████╗░██████╗░░█████╗░░██████╗
                                 ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║░░░██║██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
                                 █████╗░░╚█████╗░░░░██║░░░█████╗░░╚██╗░██╔╝█████╗░░  ░░░██║░░░█████╗░░██████╔╝██████╔╝███████║██║░░██║███████║╚█████╗░
                                 ██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░░╚████╔╝░██╔══╝░░  ░░░██║░░░██╔══╝░░██╔══██╗██╔══██╗██╔══██║██║░░██║██╔══██║░╚═══██╗
                                 ███████╗██████╔╝░░░██║░░░███████╗░░╚██╔╝░░███████╗  ░░░██║░░░███████╗██║░░██║██║░░██║██║░░██║██████╔╝██║░░██║██████╔╝
                                 ╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚══════╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░
                                 
                                 ██╗  ██╗██╗░░░░░██╗░░░░░░█████╗░
                                 ██║  ██║██║░░░░░██║░░░░░██╔══██╗
                                 ██║  ██║██║░░░░░██║░░░░░███████║
                                 ██║  ██║██║░░░░░██║░░░░░██╔══██║
                                 ██║  ██║███████╗███████╗██║░░██║
                                 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝░░╚═╝

        ******************************************************************************************************************************************************                               

"""
    
        print(titulo)
        print("\n")
        
        opcion = getOpt(textOpts,inputOptText,lista)
        print("\n")
        opc = int(opcion)
        
        if opc == 1: # Tancar sessió

            menu_before()
            
        elif opc == 2: # Jugar
            
            jugar()
            
        elif opc == 3: # Rejugar aventura
            
            query = " "
            
            choices = get_table(query)
            
            replay(choices)
            
        elif opc == 4:
            
            reports()
            
        else:
            quit()


def jugar():
    
    valid = False
    lista = [0]
    
    adventures = get_adventure_with_chars()
    
    for i in adventures.keys():
        lista.append(i)
    
    inputOptText= "Quina aventura vols jugar? (0 to Go Back): "
                
    aventuras = getFormatedAdventures(adventures)
    
    opc = getOpt(aventuras, inputOptText, lista)
    
    
    
   
    
    #Opciones de las aventuras
    if int(opc) == 0:
        menu_after()
        
        
    elif int(opc) == 10:
     
        menu_aventuras(10)
        
    elif int(opc) == 11:
        
        menu_aventuras(11)
    
    elif int(opc) == 12:
        
        menu_aventuras(12)



def reports():
    
    textOpts= "\n" + " "*80 +  "1.- Resposta més utilitzada" + "\n" + " "*80 + "2.- Jugador amb més partides jugades" + "\n" + " "*80 + "3.- Jocs jugats per l'usuari" + "\n" + " "*80 + "4.- Enrere"
    inputOptText="\n" + " "*80 + "Escull una opció: "
    lista = [1,2,3,4]
    exceptions = ["w","e",-1,0]
    
    keys = ('idAventure','adventure', 'date')
    columns = (20,20,20)
    
    while True:
        titulo = """
                                                                        ██████╗░███████╗██████╗░░█████╗░██████╗░████████╗░██████╗
                                                                        ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                                                                        ██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░
                                                                        ██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗
                                                                        ██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝
                                                                        ╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
"""
                
        print(" "*14+"//"*90)
        print("\n"*3)
        print(titulo)
        print("\n"*3)
        print(" "*14+"//"*90)
        
        print("\n")
        opcion = getOpt(textOpts,inputOptText,lista, exceptions)
        opc = int(opcion)
        print("\n")
        
        if opc == 1:
            print("Resposta més utilitzada") 
            
        elif opc == 2:
            print(" "*40 + "Jugador amb més partides jugades")
            
            query = """
            select count(G.FK_USER_ID_USER) into @partidas from GAME G;
            
            select U.user_name as NOMBRE USUARIO, @partidas as NÚMERO PARTIDAS JUGADAS from AMS.GAME G INNER JOIN AMS.USER U ON U.ID_USER = G.FK_USER_ID_USER;
            """
            
            cursor.execute(query)
            
            res = cursor.fetchall()
            
            print(res)
            
            getHeadeForTableFromTuples(("NOMBRE","USUARIO","PARTIDAS JUGADAS"),(10,20,30)) 
            print("\n")
            
        elif opc == 3:
            print(" "*40 + "Jocs jugats per l'usuari")
            getHeadeForTableFromTuples(("ID AVENTURA","NOMBRE","FECHA"),(20,20,40)) 
            getTableFromDict(keys, diccionari, columns)
            print("\n")
            
        else:
            break
    
   
def menu_aventuras(idAdventure):
    
    inputOptText = "Select your Character (0 to Go back): "
    adventure = get_adventure_with_chars()
    characters = get_characters()
    
    text = " "
    
    for i,j in adventure.items():
        
        for k,l in j.items():
            if i == idAdventure:
                if k == "Name":
                    titulo = str(l)
                    
                if k == "Description":
                    descripcion = str(l)
            
    getHeader(titulo)
    print("Adventure:".ljust(20),titulo,"\n")
    print("Description:".ljust(20),descripcion,"\n\n")

    print("="*20+"Characters"+"="*20)
    
    
    for j,k in characters.items():
        
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
    
    
    opc = getOpt(text,inputOptText, rangeList=[0,1,2])
    
    if int(opc) == 0:
        menu_after()
        
    elif int(opc) == 0:
        
        SetIdGame()


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






#/////////////////////////////////////////////////////////////// Funciones de formato ///////////////////////////////////////////////////////////////

def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[],**dictionary):
    
    while True:
        print(textOpts + "\n")
        
        opcion = input( f"{inputOptText}" )
        
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


def getTableFromDict(tuple_of_keys, diccionari, weigth_of_columns):
    
    weigth_of_columns = list(weigth_of_columns)
    
    for i,j in diccionari.items():
        pos = 0
        print(str(i).ljust(weigth_of_columns[pos]), end="")
        for k,l in j.items():
            
            if pos == len(tuple_of_keys) - 1:
                print("\n")
                
            if k in tuple_of_keys:
                print(str(l).ljust(weigth_of_columns[pos]), end=" ")
                pos+=1
                
    return " "


def formatText(text, lenLine = 25, split = "\n"):
    
    l = text.split(" ")
    lista_Frases = []
    
    for i in range(len(l)):
        if not l[i] == l[-1]:
            l[i] += " "
    
    contador = 0
    for i in range(len(l)):
        contador += len(l[i])
        if contador <= lenLine or contador == lenLine + 1:
            lista_Frases.append(l[i])
        else:
            lista_Frases.append(split + l[i])

            contador = len(l[i])
    
    for j in range(len(lista_Frases)):
        print(lista_Frases[j], end= " ")
        
    return " "


def getFormatedTable(queryTable, title="Most used answer"):
 
    cont = 0
    
    for i in queryTable:
        
        if cont == 0:
            print("="*60+title+"="*60+"\n")
            for j in i:
                print(j, end=" "*14)
            print("\n\n"+"*"*136)        
            
        
        if cont == 1:
            for j in i:
                print(formatText(str(j)))
        
        cont+=1

    
def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    cont1=0
    cont2=0
    dic1=[]
    dic2=[]

    print("="*100)
    '''print("column1".ljust(10)+"column2".ljust(20)+"column3".ljust(30))
    print(t_name_columns[0])
    print(t_size_columns[0])'''

    while cont1 != len(t_name_columns):
        #print(t_name_columns[cont1])
        dic1.append(t_name_columns[cont1])
        cont1+=1
    while cont2 != len(t_size_columns):
        #print(t_size_columns[cont2])
        dic2.append(t_size_columns[cont2])
        cont2+=1

    cont1 = 0
    cont2 = 0
    #print(dic1, dic2,"\n")

    column=[]
    while cont1 != len(dic1):
        column.append(dic1[cont1].ljust(dic2[cont2]))
        cont1 += 1
        cont2 += 1
    #print(column)
    print("".join(column))
    print("*"*100)


def getFormatedAdventures(adventures):
    l = 50
    r = 50
    medio = len("Adventures")
    num = medio / 2
    l = l - num
    r = r - num

    print("="*int(l)+"Adventures"+"="*int(r))
    print("Id Adventure".ljust(12), "Adventure".ljust(40), "Description")
    print("*" * 100)

    for i in adventures:

        print(str(i).ljust(12), adventures[i]["Name"].ljust(40), adventures[i]["Description"])
        
    return " "
        
        
def getHeader(text):
    l=50
    r=50
    medio=len(text)
    num=medio/2
    l=l-num
    r=r-num

    print("*" * 100)
    print("="*int(l)+text+"="*int(r))
    print("*" * 100)


def replay(*choices):
    pass

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////







#//////////////////////////////////////////////////////////// Funciones de usuario /////////////////////////////////////////////////////////////////


def login():
    
    user = " "
    password = " "

    chequeo = checkUserbdd(user, password)
    
    userInfo = getUser()
    

    if int(chequeo) == 0:
        print("Usuari no existeix")
        return 0
       
    elif int(chequeo) == -1:
        print("Contrasenya incorrecta")
        return -1
       
    elif int(chequeo) == 1:
        
        for i in userInfo:
            print(f"Hola {i}, anem a jugar!!\nQuina aventura vols jugar?\n\n")
            return 1
   

def checkUserbdd (user,password):
    
    correct=False
    mycursor=conn.cursor()
    mycursor.execute('SELECT user_name FROM AMS.USER')
    user= mycursor.fetchall()
    lista1=[]
    lista2=[]
    
    for i in user:
        users=i[0]
        lista1.append(users)
    mycursor=conn.cursor()
    mycursor.execute('SELECT password FROM AMS.USER')
    contrasenya1= mycursor.fetchall()
    for j in contrasenya1:
        password=j[0]
        lista2.append(password)
        
    while correct==False:
        
        usuari = input("Usuari a trobar: ")
        contrasenya = input("Contrasenya: ")
        
        if usuari in lista1:
            print('Usuari trobat')
            if contrasenya in lista2:
                correct=True
                return 1
            else:
                return -1
        else:
            return 0


def checkPassword(password):
    
    valid=False
    
    while valid == False:
    
        if len(password) < 8 or len(password) > 12:
            print("La contrasenya ha de tenir més de 8 caracters")
            return False
        else:
            
            minuscula = False
            for minus in password:
                if minus.islower()==True:
                    minuscula = True
            if not minuscula:
                print("Ha de tenir minúscules")
                return False
            
            mayusculas = False
            for mayus in password:
                if mayus.isupper()==True:
                    mayusculas = True
            if not mayusculas:
                print("Ha de portar majúscules")
                return False
        
            num=False
            for digit in password:
                if digit.isdigit()== True:
                    num=True
            if not num:
                print("La contrasenya ha de tenir números")
                return False
            
            if password.count(" ") > 0:
                print("No pot tenir espais en blanc")
                return False
            
            else:
                return True
            
                
def checkUser(user):
    
    i = False

    while i == False:
        if len(user) < 6: 
            print("El nom d'usuari ha de contenir almenys 6 carácters")
            return False

        elif len(user)>12: 
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


def userExists(user):
    
    cursor.execute("SELECT user_name FROM USER")
    
    res = cursor.fetchall()
    
    if user in res:
        return True
    else:
        return False


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


def insertUser(user, password):
    
    query = f"INSERT INTO AMS.USER (user_name, password) values ('{user}','{password}')"
    
    cursor.execute(query)
    
    res = cursor.fetchall()
    
    print(res)
    
    conn.commit()
    
    
def getUser():
    
    diccionario={}
    cursor.execute('SELECT * FROM USER')
    
    user= cursor.fetchall()
    for i in user:
        id=i[0]
        users=i[1]
        password=i[2]
        diccionario1={users:{'Password':password,'IdUser':id}}
        diccionario.update(diccionario1)
        
    return diccionario

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////




#///////////////////////////////////////////////////////////////// Funcions d'accés a BBDD ////////////////////////////////////////////////////////////////

def SetIdGame():
    times=time.strftime('%Y-%m-%d %H:%M:%S')
    idUser = " " #getUserId()
    idAdventure = " "
    idChar = " "
    
    sql=f"INSERT INTO AMS.GAME (current_data,FK_USER_ID_USER,FK_ADVENTURE_ID_ADVENTURE,FK_CHARACTER_ID_CHARACTER) VALUES('{times}','{idUser}','{idAdventure}','{idChar}')"
    
    mycursor=conn.cursor()
    mycursor.execute(sql)
    
    conn.commit()


def get_table(query):
    
    cursor.execute(query)
    res = list(cursor.fetchall())
    
    nums_fields = len(cursor.description)
    
    fields_names = tuple([i[0] for i in cursor.description])
    res.insert(0, fields_names)
    
    return tuple(res)
 
    
def get_adventure_with_chars():
    lista=[]
    diccionario={}
    
    mycursor=conn.cursor()
    char = conn.cursor()
    
    sql='SELECT * FROM CHARACTER_HAS_ADVENTURE'
    sql1='SELECT * FROM ADVENTURE'
    mycursor.execute(sql)

    charac= mycursor.fetchall()

    for j in charac:
        id_char= j[0]
        lista.append(id_char)

    mycursor.execute(sql1)
    adventures= mycursor.fetchall()

    for i in adventures:
        id_adventure=i[0]
        name_adventure=i[1]
        description_adventure=i[2]
        diccionario1 = {id_adventure: {'Name': name_adventure, 'Description': description_adventure,'Characters':lista}}
        diccionario.update(diccionario1)
        
    return diccionario
    
    
def getReplayAdventures():
    
    diccionario = {}
    
    USER = " SELECT * FROM AMS.USER;"
    
    ADVENTURE = "SELECT * FROM AMS.ADVENTURE"

    
    CHARACTER = "SELECT * FROM AMS.CHARACTER"
    
    cursor.execute(CHARACTER)
    
    res = cursor.fetchall()
    
    return res


def get_characters():
    diccionario = {}
    mycursor=conn.cursor()
    mycursor.execute('SELECT * FROM AMS.CHARACTER')
    user= mycursor.fetchall()
    for i in user:
        id=i[0]
        name=i[1]
        diccionario1 = {id: name}
        diccionario.update(diccionario1)
        
    return diccionario

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////