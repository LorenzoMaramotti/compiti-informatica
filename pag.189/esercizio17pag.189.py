def capovolgi(nazioni,capitali):
    capitali_nazioni={}
    for i in range(len(capitali)):
        capitali_nazioni[capitali[i]]=nazioni[i]
    return capitali_nazioni

def main():
    nazioni=["Italia","Francia","Germania","Regno unito","Portogallo","Grecia","Polonia"]
    capitali=["Roma","Parigi","Berlino","Londra","Lisbona","Atene","Varsavia"]
    while True:
        scelta=input("Vuoi aggiungere un'altra capitale e un altro stato? ")
        scelta=scelta.capitalize()
        if scelta=="Si":
            numero_scelta=int(input("Quante capitali voi aggiungere? "))
            for i in range(numero_scelta):
                print("Inserisci il nome della capitale e dello stato")
                aggiunta_capitale=input()
                aggiunta_nazione=input()
                nazioni.append(aggiunta_nazione)
                capitali.append(aggiunta_capitale)
            print("Ecco a te la lista aggiornata delle capitali seguite dallo stato")
            break
        else:
            print("Va bene eccoti la lista delle capitali seguite dagli stati presenti nel sistema")
            break
    print(capovolgi(nazioni,capitali))
main()
        
