import mysql.connector


mydb=mysql.connector.connect(
    host= '127.0.0.1',
    user= 'ALEX',
    password='5865bvxh',
    port='3306',
    database='ams'
)
def getUser():
    diccionario={}
    mycursor=mydb.cursor()
    mycursor.execute('SELECT * FROM user')
    user= mycursor.fetchall()
    for i in user:
        id=i[0]
        users=i[1]
        password=i[2]
        diccionario1={users:{'Password':password,'IdUser':id}}
        diccionario.update(diccionario1)
    print(diccionario)
getUser()









