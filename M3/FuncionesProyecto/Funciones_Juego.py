#///////////// Conexión a la BBDD //////////////

import pymysql

#Establecer la conexión
conn = pymysql.connect(
    host="localhost",
    user="jismael",
    password = "Admin123-",
    db = "Prueba"
)

cursor = conn.cursor()

#///////////////////////////////////////////////



#//////////////////////////// Variables globales ////////////////////////////

#getOpt()
textOpts="\n1.- Jugar\n2.- Iniciar sessió\n3.- Crear usuari\n4.- Mostrar aventures\n5.- Sortir"
inputOptText="\nEscull una opció: "

lista = [1,2,3,4,5]
exceptions = ["w","e",-1]

#---------------------------------------------------------------------------

#getTableFromDict()

import datetime

tuple_of_keys = ('Username','Name','CharacterName','date')

weigth_of_columns = (20,30,20,20)

diccionari={
    4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure':1, 
        'Name': 'Este muerto esta muy vivo',
        'CharacterName':'Beowulf',
        'date': datetime.datetime(2021, 11, 28, 18, 17, 20),
        'idCharacter': 1, 
        },
     
    5: {'idUser': 2, 'Username': 'Jordi','idAdventure': 1, 
        'Name': 'Este muerto esta muy vivo',
        'CharacterName': 'Beowulf', 
        'date': datetime.datetime(2021, 11, 26,13, 28, 36), 
        'idCharacter': 1,
        }}

#---------------------------------------------------------------------------

#getFormatedTable

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

#////////////////////////////////////////////////////////////////////////////




#////////////////////// Funciones no funcionales //////////////////////

def menu():

    textOpts="\n1.- Jugar\n2.- Iniciar sessió\n3.- Crear usuari\n4.- Mostrar aventures\n5.- Sortir"
    inputOptText="\nEscull una opció: "
    lista = [1,2,3,4,5]
    
    while True:
        titulo = """

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


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

***********************************************************************************************************************************************************************************************                                             

"""
    
        print(titulo)
        print()
        
        opcion = getOpt(textOpts,inputOptText,lista, exceptions)
        opc = int(opcion)
        
        if opc == 1:
            userExists()
            print("Jugar") 
            
        elif opc == 2:
            print("Iniciar sessió") 
            
        elif opc == 3:
            createUser()
            
        elif opc == 4:
            reports()
            print("Mostra Aventures")
        else:
            break

def reports():
    
    textOpts="\n1.- Resposta més utilitzada\n2.- Jugador amb més partides jugades\n3.- Jocs jugats per l'usuari\n4.- Enrere"
    inputOptText="\nEscull una opció: "
    lista = [1,2,3,4]
    
    while True:
        titulo = """
                                                                    ██████╗░███████╗██████╗░░█████╗░██████╗░████████╗░██████╗
                                                                    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
                                                                    ██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░
                                                                    ██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗
                                                                    ██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝
                                                                    ╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
"""
        
        
        print("//"*104)
        print(titulo)
        print()
        
        print("//"*104)
        
        opcion = getOpt(textOpts,inputOptText,lista, exceptions)
        
        
        opc = int(opcion)
        
        if opc == 1:
            print("Resposta més utilitzada") 
            
        elif opc == 2:
            print("Jugador amb més partides jugades") 
            
        elif opc == 3:
            print("Jocs jugats per l'usuari")
        
        else:
            break
    
    
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
            print("Opció invàida")
        else:
            break
        
    return opcion


""" def getTableFromDict(tuple_of_keys, diccionari, weigth_of_columns):
    
    weigth_of_columns = list(weigth_of_columns)
    
    for i,j in diccionari.items():
        pos = 0
        print(str(i).ljust(weigth_of_columns[pos]), end="")
        for k,l in j.items():
            
            if pos == len(tuple_of_keys):
                print("\n")
                
            if k in tuple_of_keys:
                print(str(l).ljust(weigth_of_columns[pos]), end=" ")
                pos+=1
                
    return " "
"""


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
        
        
print(getFormatedTable(getTable))


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


def get_table(query):
    
    cursor.execute(query)
    res = list(cursor.fetchall())
    
    nums_fields = len(cursor.description)
    
    fields_names = tuple([i[0] for i in cursor.description])
    res.insert(0, fields_names)
    
    return tuple(res)


def userExists(user):
    
    cursor.execute("select username from User")
    
    res = cursor.fetchall()
    
    if user in res:
        return True
    else:
        return False


""" def replay(*choices):
    pass
"""


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
    
    query = f"INSERT INTO user (user_name,password) values ({user},{password})"
    cursor.execute(query)
    
    conn.commit()
    

def getChoices():
    query = "SELECT * FROM "
    cursor.execute(query)
    
#//////////////////////////////////////////////////////