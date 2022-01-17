import mysql.connector
diccionario={}

mydb=mysql.connector.connect(
    host= '127.0.0.1',
    user= 'ALEX',
    password='5865bvxh',
    port='3306',
    database='ams'
)

mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM ams.character')
user= mycursor.fetchall()
for i in user:
    id=i[0]
    name=i[1]
    diccionario1 = {id: name}
    diccionario.update(diccionario1)
print(diccionario)