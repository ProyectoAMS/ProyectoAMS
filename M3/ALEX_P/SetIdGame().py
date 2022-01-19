import mysql.connector
import time
mydb=mysql.connector.connect(
    host= '127.0.0.1',
    user= 'ALEX',
    password='5865bvxh',
    port='3306',
    database='ams'
)
idGame=0
idUser=1
idAdventure=11
idChar=1
def SetIdGame():
    times=time.strftime('%Y-%m-%d %H:%M:%S')
    sql=f"INSERT INTO ams.game(current_data,FK_USER_ID_USER,FK_ADVENTURE_ID_ADVENTURE,FK_CHARACTER_ID_CHARACTER) VALUES('{times}','{idUser}','{idAdventure}','{idChar}')"
    mycursor=mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()

SetIdGame()