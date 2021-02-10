nomi_numeri={}
while True:
    nome_contatto=input("Inserire il nome della persona della quale si vuole cercare il numero; \nPer fermare il programma premi q  ")
    nome_contatto=nome_contatto.capitalize()
    if nome_contatto=="Q":
        break
    if nome_contatto in nomi_numeri:
        print("Il numero di", nome_contatto, "è già presente nella rubrica ed è", nomi_numeri[nome_contatto])
    else:
        print("Il contatto inserito non è stato trovato")
        aggiungi_contatto=input("Vuoi aggiungere questo contatto alla rubrica? ")
        aggiungi_contatto=aggiungi_contatto.capitalize()
        if aggiungi_contatto=="Si":
            print("Inseririsci il numero di", nome_contatto)
            numero_contatto=input()
            nomi_numeri[nome_contatto]=numero_contatto
            print("Il numero è stato aggiunto correttamente")
        else:
            print("Va bene passiamo al prossimo contatto")
            pass