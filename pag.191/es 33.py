lista_pazienti=[]
while True:
    nome_paziente=input("Inserisci il nome del paziente, per smettere di aggiungere pazienti premi q ")
    nome_paziente=nome_paziente.capitalize()
    if nome_paziente=="Q":
        break
    else: 
        lista_pazienti.append(nome_paziente)
for i in range (len(lista_pazienti)):
    while True:
        if lista_pazienti==[]:
            break
        print("Il prossimo paziente della lista è", lista_pazienti[0])
        lista_pazienti.pop(0)

print("Grazie di aver usato il nostro programma")