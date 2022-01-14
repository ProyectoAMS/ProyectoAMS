#///////////// Conexión a la BBDD //////////////

import pymysql

#Establecer la conexión
conn = pymysql.connect(
    host="40.68.208.129",
    user="azure-admin",
    password = "mypass123",
    db = "ams"
)

cursor = conn.cursor()

#///////////////////////////////////////////////



#//////////////////////////// Variables globales ////////////////////////////

#getOpt()
textOpts="\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit"
inputOptText="\nChoose an option: "

lista = [1,2,3,4,5]

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

#////////////////////////////////////////////////////////////////////////////




#////////////////////// Funciones no funcionales //////////////////////

def menu():
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
        
        opc = getOpt(textOpts,inputOptText,lista)
        
        if opc == 1:
            print("Login")
        elif opc == 2:
            print("Create User")
        elif opc == 3:
            print("Show Adventures")
        else:
            quit()
        
def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[],**dictionary):
    valid = False
    
    while valid != True:
        print(textOpts + "\n")
        
        opcion = input( f"{inputOptText}" )
        
        print()
        
        if not opcion.isdigit():
            print("Opció invàlida")
        elif (int(opcion) < rangeList[0] or int(opcion) > rangeList[-1]):  
            print("Opció invàlida")
        else:
            valid = True
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

def formatText(text, lenLine = 21, split = "\n"):
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
        length = 0
        
        if cont == 0:
            print("="*60+title+"="*60+"\n")
            for j in i:
                print(j, end=" "*14)
            print("\n\n"+"*"*136)
            
        for i in range(len(queryTable)):
            for j in i:
                print(formatText(str(j)))
                
                    
                
        cont+=1
        
    return " "

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

""" def userExists(user):
    if user in dict:
        return True
    else:
        False
"""

""" def replay(*choices):
    pass
"""

""" def createUser():
    
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
        
    print()
    return input("Prém per continuar")
"""

def getTable(query):
    pass
#//////////////////////////////////////////////////////