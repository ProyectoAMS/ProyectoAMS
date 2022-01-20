import mysql.connector


mydb=mysql.connector.connect(
    host= '40.68.208.129',
    user= 'azure-admin',
    password='mypass123',
    port='3306',
    database='AMS'
)
def get_characters():
    diccionario = {}
    mycursor=mydb.cursor()
    mycursor.execute('SELECT * FROM AMS.CHARACTER')
    user= mycursor.fetchall()
    for i in user:
        id=i[0]
        name=i[1]
        diccionario1 = {id: name}
        diccionario.update(diccionario1)
    print(diccionario)

get_characters()