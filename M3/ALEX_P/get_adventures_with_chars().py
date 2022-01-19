import mysql.connector

mydb=mysql.connector.connect(
    host= '40.68.208.129',
    user= 'azure-admin',
    password='mypass123',
    port='3306',
    database='AMS'
)

def get_adventure_with_chars():
    lista=[]
    diccionario={}
    mycursor=mydb.cursor()
    char=mydb.cursor()
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
    print(diccionario)

get_adventure_with_chars()


