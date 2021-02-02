lista_città=[]
lista_città_valore_alto=[]
lista_citta_valore_basso=[]
while True:
    nome_città=input("Insersci il nome della città desiderata o se desideri uscire premi q: ")
    if nome_città=="q":
        break
    else:
        pass
    lista_città.append(nome_città)
    valore_minimo=int(input("Inserire il valore minimo della temperatura: "))
    valore_massimo=int(input("Inserire il valore massimo della temperatura: "))
    escursione_termica=valore_massimo-valore_minimo
    print("L'escursione termica nella città di " , nome_città , "è di" , escursione_termica , "gradi")
    if escursione_termica>=20:
        lista_città_valore_alto.append(nome_città)
    else:
        lista_citta_valore_basso.append(nome_città)

print("Queste sono le città con escursione termica maggiore di 20:" , lista_città_valore_alto)

