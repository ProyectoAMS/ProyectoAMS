import mysql.connector
mydb=mysql.connector.connect(
    host= '127.0.0.1',
    user= 'ALEX',
    password='5865bvxh',
    port='3306',
    database='ams'
)

# LAS VARIABLES SE IRAN RELLENANDO DURANTE EL JUEGO
idGame=4
idUser=6
idAdventure=10
idChar=7
idoption=101
idstep=101
idadventure=10

def insertCurrentChoise(idGame,idstep,idoption):
    sql=f"INSERT INTO ams.decision(FK_GAME_ID_GAME,FK_GAME_USER_ID_USER,FK_GAME_ADVENTURE_ID_ADVENTURE,FK_GAME_CHARACTER_ID_CHARACTER,FK_OPTION_ID_OPTION,FK_STEP_ID_STEP,FK_STEP_ADVENTURE_ID_ADVENTURE) VALUES('{idGame}','{idUser}','{idAdventure}','{idChar}','{idoption}','{idstep}','{idadventure}')"
    mycursor=mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()

insertCurrentChoise(idGame,idstep,idoption)