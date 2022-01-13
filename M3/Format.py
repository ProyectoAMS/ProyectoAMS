def format():
    hola = "ice oiwnwe in iconw e oien oiwncweoi iociowen ei ociwne ew c"
    l = []
    ll = []
    lenLine = 10
    contador = 0

    for i in range(len(hola)):
        l.append(hola[i])
    print(l)
    print(l[lenLine - 1])
    for i in range(len(l)):
        if (i + 1) == lenLine * (i + 1):
            if l[lenLine - 1] == " ":
                ll.append(l[0: lenLine - 2])
                del l[0: lenLine - 1]
            else:
                while l[(lenLine - 1) - contador] != " ":
                    contador += 1
                ll.append(l[0: (lenLine - 2) - contador])
                del l[0: (lenLine - 1) - contador]

    print(ll)
#format()

def formatText(text, lenLine, split):
    l=[]
    for i in range(len(text)):
        l.append(text[i])
    print(l)


text="Doing so will treat the number as an integer value and thus remove the error"
formatText(text, 10, " ")


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