'''nazioni=['Belgio' , 'Francia' , 'Germania' , 'Grecia' , 'Italia' , 'Paesi Bassi' , 'Polonia' ,  'Portogallo' , 'Regno Unito']
capitali=['Bruxelles' , 'Parigi' , 'Berlino' , 'Atene' , 'Roma' , 'Amsterdam' , 'Varsavia' , 'Lisbona' , 'Londra']

while True:
    scelta_stato=input("Scegli uno stato per saperne la capitale.\nRicordati di inserire la maiuscola: ")
    if scelta_stato in nazioni:
        i = nazioni.index(scelta_stato)
        print("La capitale dello stato" , scelta_stato , "è" , capitali[i])
    else:
        scelta=int(input("Questa capitale non è nel nostro database \nPer inserirne una nuova premi 1 \nPer uscire premi 0: "))
        while True:
            if scelta==1:
                break
            elif scelta==0:
                print("Grazie e arriverderci")
                break
            else:
                print("Per favore seleziona un carattere tra 1 e 0")
                break'''






b_maggiore=int(input("inserire la basa maggiore"))
b_minore=int(input("inserire la base minore"))
h=int(input("inserire l'altezza"))
while True:
    lato_1=int(input("inserire lato 1 (non può essere  negativo)"))
    if lato_1<0:
        print("errore: lato negativo")
    else:
        break
while True:
    lato_2=int(input("inserire lato 2  (non può essere  negativo)"))
    if lato_2<0:
        print("errore: lato negativo")
    else:
        break
def trapezio():
    area = (b_maggiore+b_minore)*h/2
    perimetro = b_maggiore+b_minore+lato_1+lato_2
    print("l'area è di", area)
    print("il perimetro è di", perimetro)
trapezio()