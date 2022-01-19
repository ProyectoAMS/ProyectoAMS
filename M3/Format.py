

'''--FUNCIONES--'''


import pymysql
#--ESTABLECER CONEXION--
conn=pymysql.connect(host="localhost", user="root", password="Qwert12345", db="ams")
import os


text = "Nada es la primera novela de la escritora barcelonesa Carmen Laforet y una de las obras literarias más importantes de la España del siglo XX. Se trata de una obra existencialista1​ que representa el estancamiento y la pobreza que se vivieron en la posguerra española, durante los primeros años del franquismo. Dotada de un estilo literario que supuso una renovación en la prosa de la época, Nada refleja también la lenta desaparición de la pequeña burguesía tras la Guerra Civil."
def formatText(text, lenLine = 50, split = "\n"):
    l = text.split(" ")
    lista_Frases = []
    #print(l)

    for i in range(len(l)):
        if not l[i] == l[-1]:
            l[i] += " "
    #print(l)
    contador = 0
    for i in range(len(l)):
        contador += len(l[i])
        if contador <= lenLine or contador == lenLine + 1:
            lista_Frases.append(l[i])
        else:
            lista_Frases.append(split + l[i])

            contador = len(l[i])
    #print(lista_Frases)
    for j in range(len(lista_Frases)):

        print(lista_Frases[j], end= "")

#formatText(text)



adventures={1:{"Adventure":"Este muerto esta myu vivo", "Description":"Beowlf, se embarca en la busqueda de la espada llamada la Ira de Los Cielos"},2:{"Adventure":"La Matanza de Texas", "Description":"Mario Vaquerizo, se enfrenta al horror"}}

def getFormatedAdventures(adventures):
    l = 50
    r = 50
    medio = len("Adventures")
    num = medio / 2
    l = l - num
    r = r - num

    print("="*int(l)+"Adventures"+"="*int(r))
    print("Id Adventure".ljust(12), "Adventure".ljust(40), "Description")
    print("*" * 100)

    for i in adventures:

        print(str(i).ljust(12), adventures[i]["Adventure"].ljust(40), adventures[i]["Description"])
        #formatText(adventures[i]["Description"])

#getFormatedAdventures(adventures)


def getHeader(text):
    l=50
    r=50
    medio=len(text)
    num=medio/2
    l=l-num
    r=r-num

    print("*" * 100)
    print("="*int(l)+text+"="*int(r))
    print("*" * 100)

'''text=input("introduce un texto:")
getHeader(text)'''

def getHeadeForTableFromTuples(t_name_columns,t_size_columns,title=""):
    cont1=0
    cont2=0
    dic1=[]
    dic2=[]

    print("="*100)
    '''print("column1".ljust(10)+"column2".ljust(20)+"column3".ljust(30))
    print(t_name_columns[0])
    print(t_size_columns[0])'''

    while cont1 != len(t_name_columns):
        #print(t_name_columns[cont1])
        dic1.append(t_name_columns[cont1])
        cont1+=1
    while cont2 != len(t_size_columns):
        #print(t_size_columns[cont2])
        dic2.append(t_size_columns[cont2])
        cont2+=1

    cont1 = 0
    cont2 = 0
    #print(dic1, dic2,"\n")

    column=[]
    while cont1 != len(dic1):
        column.append(dic1[cont1].ljust(dic2[cont2]))
        cont1 += 1
        cont2 += 1
    #print(column)
    print("".join(column))
    print("*"*100)

#getHeadeForTableFromTuples(("column1","column2","column3"),(10,20,30))










import datetime
def getTableFromDict(tuple_of_keys, diccionari, weigth_of_columns):
    weigth_of_columns = list(weigth_of_columns)

    for i, j in diccionari.items():
        pos = 0
        print(str(i).ljust(weigth_of_columns[pos]), end="")
        for k, l in j.items():

            if pos == len(tuple_of_keys):
                print("\n")

            if k in tuple_of_keys:
                print(str(l).ljust(weigth_of_columns[pos]), end=" ")
                pos += 1

    return " "



def getFormatedAnswers(idAnswer, text, lenLine, leftMargin):
    cur = conn.cursor()

    query = f'''select * from ams.option where FK_STEP_ID_STEP={idAnswer}'''
    cur.execute(query)

    answer = cur.fetchall()

    for i in answer:
        formatText(str(i[0])+") "+str(i[text]),lenLine)
        print()

"101<--poner el id de la pregunta"
#getFormatedAnswers(101,1,100,50)



def replay(choice):
    # --CONSULTA--
    cur = conn.cursor()
    query1 = f"""select adventure_name, description, id_adventure from adventure 
    where id_adventure=(select FK_ADVENTURE_ID_ADVENTURE from game where id_game={choice})"""
    cur.execute(query1)
    title = cur.fetchall()

    print()
    getHeader(str(title[0][0]))
    formatText(str(title[0][1]),100)
    cur.close()
    print()
    input("\n\nEnter para Continuar")

    #--CONSULTA--
    cur = conn.cursor()
    query2 = f"""select d.ID_DECEISION ,s.id_step, s.step_description, o.id_option, o.option_description, o.go_step, 
    (select s.step_description from step s where o.go_step=s.ID_STEP)
    from ams.option o inner join ams.step s on o.fk_step_id_step=s.id_step
    inner join decision d on o.id_option=d.fk_option_id_option
    where FK_GAME_ID_GAME={choice}"""
    cur.execute(query2)
    history = cur.fetchall()

    #while history[] repetir hasta acabar el replay
    for i in history:
        formatText(str(i[2]), 100)
        print("\n")
    input("Enter to contiune\n")

    for i in history:
        print("opcion: ")
        formatText(str(i[3]), 100)
        print()
        formatText(str(i[4]), 100)
        print("\n")
    input("Enter to continue")
    for i in history:
        formatText(str(i[6]), 100)
        print("\n")
    getHeader("FIN")
    cur.close()
    conn.close()

#choice = int(input("elige id game: "))
#replay(choice)




def getChoices():
    '''Una vegada hem triat l'aventura que volem reviure, get choices ens retorna una tupla
    on els components són les tuples (idByStep_Adventure, idAnswers_ByStep_Adventure),
    que ens permetran reviure una aventura donada'''

    cur = conn.cursor()
    query3 = '''select FK_GAME_ID_GAME, d.fk_option_id_option, o.answer from ams.decision d 
    inner join ams.option o on d.fk_option_id_option = o.id_option'''
    cur.execute(query3)
    choices = cur.fetchall()
    print(choices)
    input("\npulsar")

#getChoices()

def insertCurrentChoice(idGame,actual_id_step,id_answer):
    '''Aquesta funció actualitza la taula choices.'''

    cur = conn.cursor()
    query4 = f'''inser into decision (FK_GAME_ID_GAME, id_step) value ({idGame}, )'''
    cur.execute(query4)
    choices = cur.fetchall()
    getChoices()
    input("\npulsar")


idGame = int(input("Introduce el id del juego: "))
actual_id_step = int(input("introduce el id_step actual: "))
id_answer = int(input("Introduce el id_answer (answer) en la db: "))
#insertCurrentChoice(idGame, actual_id_step, id_answer)
os.system("tree")
