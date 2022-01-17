

'''--FUNCIONES--'''


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
opciones={
    1:{"answer":"A aquesta funció li passem un id de resposta, el text de la resposta, "
                "longitud de la línia i marge a la dreta, i ens retorna la resposta amb "
                "els paràmetres passats. "},
    2:{"answer":"Aquesta funció ens serà útil per a presentar les respostes possibles en "
                "cadascun dels passos. "},
    3:{"answer":"Observem que en formatar les línies, no tallem cap paraula per la meitat. "}
}
opciones2={
    1:{"answer":"A aquesta funció li passem el diccionari adventures i retorna una "
                "cadena que una vegada impresa ens mostra:"},
    2:{"answer":"La capçalera de la selecció d'aventures i les aventures amb id, títol"
                " i descripció de les aventures formatades en columnes."}
}
def getFormatedAnswers(idAnswer,text,lenLine,leftMargin):
    cont=1
    id=cont,")"

    #print(len(idAnswer))
    while cont !=len(idAnswer)+1:
        formatText(idAnswer[cont][text], lenLine)
        print()
        cont+=1



getFormatedAnswers(opciones2,"answer",80,"leftMargin")

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

diccionari={
    4: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': 'Este muerto esta muy vivo',
        'date': datetime.datetime(2021, 11, 28, 18, 17, 20), 'idCharacter': 1, 'CharacterName':
'Beowulf'},
    5: {'idUser': 2, 'Username': 'Jordi', 'idAdventure': 1, 'Name': "Este muerto esta muy vivo",
        "date": datetime.datetime(2021, 11, 26, 13, 28, 36), 'idCharacter': 1,
'CharacterName': 'Beowulf'}}
tuple_of_keys = ("Username","Name","CharacterName","date")
weigth_of_columns = (20, 30, 20, 20)

#getTableFromDict(tuple_of_keys, diccionari,weigth_of_columns)


def replay(choices):
    print()
