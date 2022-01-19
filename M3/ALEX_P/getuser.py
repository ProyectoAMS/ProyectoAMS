import mysql.connector


mydb=mysql.connector.connect(
    host= '40.68.208.129',
    user= 'azure-admin',
    password='mypass123',
    port='3306',
    database='AMS'
)
def getUser():
    diccionario={}
    mycursor=mydb.cursor()
    mycursor.execute('SELECT * FROM USER')
    user= mycursor.fetchall()
    for i in user:
        id=i[0]
        users=i[1]
        password=i[2]
        diccionario1={users:{'Password':password,'IdUser':id}}
        diccionario.update(diccionario1)
    print(diccionario)
getUser()









