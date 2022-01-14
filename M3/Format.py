

'''--FUNCIONES--'''


def formatText(text, lenLine=50, split="\n"):
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
        if contador <= lenLine or contador == lenLine:
            lista_Frases.append(l[i])
        else:
            contador = len(l[i])
            lista_Frases.append(split + l[i])
    #print(lista_Frases)
    for j in range(len(lista_Frases)):
        print(lista_Frases[j], end="")
'''text="A aquesta funció li passem el diccionari adventures i retorna una cadena que una vegada impresa ens mostra:"
formatText(text)'''



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

def getFormatedAnswers(idAnswer,text,lenLine,leftMargin):
    print()