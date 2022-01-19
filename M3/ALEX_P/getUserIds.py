import mysql.connector
mydb=mysql.connector.connect(
    host= '40.68.208.129',
    user= 'azure-admin',
    password='mypass123',
    port='3306',
    database='AMS'
)

def getUserIds():
    mycursor=mydb.cursor()
    mycursor.execute('SELECT user_name FROM USER')
    user= mycursor.fetchall()
    lista1=[]
    lista2=[]
    listafinal=[]
    for i in user:
        users=i[0]
        lista1.append(users)
    mycursor=mydb.cursor()
    mycursor.execute('SELECT ID_USER FROM USER')
    id= mycursor.fetchall()
    for j in id:
        ids=j[0]
        lista2.append(ids)
    listafinal.append(lista1)
    listafinal.append(lista2)
    print(listafinal)

getUserIds()