import mysql.connector
mydb=mysql.connector.connect(
    host= '127.0.0.1',
    user= 'ALEX',
    password='5865bvxh',
    port='3306',
    database='ams'
)

def get_id_game():
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM GAME')
    game = mycursor.fetchall()
    for i in game:
        id = i[0]
        print(id)

get_id_game()
