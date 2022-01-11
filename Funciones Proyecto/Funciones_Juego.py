import datetime

"""
getOpt()
getFormatedTable()
checkPassword()
checkUser()
userExists()
replay()
"""

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
    length = 0
    
    for i,j in diccionari.items():
        for k,l in diccionari[i].items():
            if k in tuple_of_keys:
                print(l, end=" ")
                length+=1
            
            if length == 4:
                print("\n")
            
    return " "

print(getTableFromDict(tuple_of_keys, diccionari, weigth_of_columns))