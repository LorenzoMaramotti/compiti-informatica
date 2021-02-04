stati_capitali={"Italia":"Roma" , "Francia":"Parigi" , "Germania":"Berlino" , "Regno unito":"Londra" , "Portogallo":"Lisbona" , "Grecia":"Atene" , "Polonia":"Varsavia"}

while True:
    scelta_nazione=input("Inserisci il nome di uno stato per saperne la capitale \nRicordati la maiuscola: ")
    if scelta_nazione in stati_capitali:
        print("La capitale dello stato" , scelta_nazione , "è" , stati_capitali[scelta_nazione])
    else:
        capitale=input("Lo stato selezionato non è presente se aggiungi la capitale verrà aggiunto al database \nRicordati di mettere la maiuscola: ")
        stati_capitali[scelta_nazione]=capitale
    while True:
        scelta=int(input("Per continuare premi 1 per uscire premi 0: "))
        if scelta==1:
            print("Buona continuazione")
            break
        elif scelta!=1 and scelta!=0:
            print("Per favore utilizza un valore che sia 1 o 0")
            
        elif scelta==0:
            print("Grazie ed arrivederci")
            break
    if scelta==0:
        break