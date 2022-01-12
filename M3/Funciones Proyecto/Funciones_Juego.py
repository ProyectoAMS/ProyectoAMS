"""
import datetime

tuple_of_keys = ('Username','Name','CharacterName','date')

weigth_of_columns = (20,30,20,20)

diccionari={
    4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure':1, 
        'Name': 'Este muerto esta muy vivo',
        'date': datetime.datetime(2021, 11, 28, 18, 17, 20),
        'idCharacter': 1, 
        'CharacterName':'Beowulf'},
     
    5: {'idUser': 2, 'Username': 'Jordi','idAdventure': 1, 
        'Name': 'Este muerto esta muy vivo', 
        'date': datetime.datetime(2021, 11, 26,13, 28, 36), 
        'idCharacter': 1,
        'CharacterName': 'Beowulf'}}

def getTableFromDict(tuple_of_keys, diccionari, weigth_of_columns):
    
    weigth_of_columns = list(weigth_of_columns)
    pos = 0
    
    for i in diccionari.keys():
        print(str(i).ljust(weigth_of_columns[0]), end="")
        for k,l in diccionari[i].items(): 
            print(str(l).ljust(weigth_of_columns[pos]), end="")
            pos+=1

            
    return " "

print(getTableFromDict(tuple_of_keys, diccionari, weigth_of_columns))
"""

"""
textOpts="\n1)Login\n2)Create user\n3)Show Adventures\n4)Exit"
inputOptText="\nElige tu opción: "
lista = [1,2,3,4]
dict = {1,2,3,4}
exceptions = ["w","e",-1]

def getOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[],**dictionary):
    valid = False
    
    while valid != True:
        print(textOpts)
        
        opcion = input(f"{inputOptText}")
        print()
        
        if not opcion.isdigit():
            print("Opció invàlida")
        elif (int(opcion) < rangeList[0] or int(opcion) > rangeList[-1]):  
            print("Opció invàlida")
        else:
            valid = True
    
    
    if opcion == 4:
        quit()
    
    return opcion


opc = getOpt(textOpts,inputOptText,lista,exceptions)
print(opc)
"""
"""
getTable = (
    ('ID AVENTURA - NOMBRE', 'ID PASO - DESCRIPCION', 'ID RESPUESTA - DESCRIPCION', 'NUMERO VECES SELECCIONADA'), 
    ('10 - Todos los héroes necesitan su princesa', '101 - Son las 6 \nde la mañana, personajes\n est├í profundamente\n dormido. Le suena la\n alarma!', '101 - Apaga la alarma\n porque quiere dormir,\n han sido d├¡as muy duros\n y personajes necesita\n un descanso.', 7), 
    ('10 - Todos los héroes necesitan su princesa', '103 - Nuestro héroe\n personaje se viste\n rápidamente y va an\n direcci├│n al ciber, hay\n mucho jaleo en la calle,\n tambi├®n mucha policía.', '108 - Entra en el ciber\n a revisar si la princesa\n Wyoming sigue dentro.', 5)
)

def getFormatedTable(queryTable, title="Most used answer"):
    listQuery = list(queryTable)
    cont = 0

    
    for i in listQuery:
        if cont == 0:
            print("="*60+title+"="*60+"\n")
            for j in i:
                print(j, end=" "*14)
            print("\n\n"+"*"*136)
        
        elif cont == 1:
            for j in i:
                print(j, end = " ")
                
        elif cont == 2:
            for j in i:
                print(j)
                
        elif cont == 3:
            for j in i:
                print(j)  
                
        elif cont == 4:
            for j in i:
                print(j)
        cont+=1
            
        
        
    return " "

print(getFormatedTable(getTable))
"""

"""
def checkPassword(password=input("Introdueix la contrasenya: ")):
    
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
                print("La password ha de tenir números")
                return False
            
            if password.count(" ") > 0:
                print("No pot tenir espais en blanc")
                return False
            
            else:
                return True
                
print(checkPassword())
"""

"""
def checkUser(user = input("Introdueixi un nom d'usuari (Té que ser alfanúmeric): ")):
    
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

print(checkUser())
"""

"""
def userExists(user):
    if user in dict:
        return True
    else:
        False
"""

"""
def replay(*choices):
    pass
"""