import mysql.connector
mydb=mysql.connector.connect(
    host= '127.0.0.1',
    user= 'ALEX',
    password='5865bvxh',
    port='3306',
    database='ams'
)

def getUserIds():
    mycursor=mydb.cursor()
    mycursor.execute('SELECT user_name FROM user')
    user= mycursor.fetchall()
    lista1=[]
    lista2=[]
    listafinal=[]
    for i in user:
        users=i[0]
        lista1.append(users)
    mycursor=mydb.cursor()
    mycursor.execute('SELECT id_user FROM user')
    id= mycursor.fetchall()
    for j in id:
        ids=j[0]
        lista2.append(ids)
    listafinal.append(lista1)
    listafinal.append(lista2)
    print(listafinal)

getUserIds()