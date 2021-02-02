lista_caratteri=[]
while True:
    ripetizioni=0
    parola=input("Inserisci le parole che vuoi per sapere quanto sono lunghe. Per vedere la lunghezza delle parole scrivi p per vedere la lunghezza delle parole e uscire scrivi q ")
    if parola=="p":
        print(lista_caratteri)
    if parola=="q":
        break
    else:
        for str in parola:
            ripetizioni+=1
        lista_caratteri.append(ripetizioni)
print("Sei uscito. La lunghezza delle parole che hai inserito è:" , lista_caratteri)


            