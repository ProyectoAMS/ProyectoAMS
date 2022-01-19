import mysql.connector

mydb=mysql.connector.connect(
    host= '40.68.208.129',
    user= 'azure-admin',
    password='mypass123',
    port='3306',
    database='AMS'
)

def get_first_step_adventure():
    while True:
        aventura = input('Aventura')
        if aventura=='10' or aventura=='11' or aventura=='12':
            mycursor=mydb.cursor()
            sql1=f"SELECT * FROM STEP WHERE FK_ADVENTURE_ID_ADVENTURE= {aventura} "
            mycursor.execute(sql1)
            user= mycursor.fetchall()
            lista=[]
            for i in user[0]:
                lista.append(i)
            id=lista[0]
            description=lista[1]
            lista2=[]
            lista2.append(id)
            lista2.append(description)
            print(lista2)
            break
        else:
            print('No es possible aquesta opció')

get_first_step_adventure()


