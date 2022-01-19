import mysql.connector
mydb=mysql.connector.connect(
    host= '127.0.0.1',
    user= 'ALEX',
    password='5865bvxh',
    port='3306',
    database='ams'
)
def checkUserbdd (user,password):
    correct=False
    mycursor=mydb.cursor()
    mycursor.execute('SELECT user_name FROM user')
    user= mycursor.fetchall()
    lista1=[]
    lista2=[]
    for i in user:
        users=i[0]
        lista1.append(users)
    mycursor=mydb.cursor()
    mycursor.execute('SELECT password FROM user')
    contrasenya1= mycursor.fetchall()
    for j in contrasenya1:
        password=j[0]
        lista2.append(password)
    while correct==False:
        usuari = input('usuari a trobar')
        contrasenya = input('contraseña')
        if usuari in lista1:
            print('Usuari trobat')
            if contrasenya in lista2:
                print(1)
                correct=True
            else:
                print(-1)
        else:
            print(0)
            tr=False

usuari=0
contrasenya=0
checkUserbdd(usuari,contrasenya)