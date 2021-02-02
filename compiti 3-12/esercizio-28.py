while True:
    numero_studenti=int(input("Quanti studenti partecipano a questa gara? "))
    if numero_studenti>1:
        break
    else:
        print("Hai inserito solo un partecipante per favore inseriscine almeno due")
        pass


lista_nomi=[]
lista_lanci=[]

numero_lanci=0
while True:
    numero_lanci+=1
    nome_studente=input("Inserire il nome dello studente: ")
    lista_nomi.append(nome_studente)

    lancio_studente=int(input("Inserire la lunghezza del lancio: "))
    lista_lanci.append(lancio_studente)

    if numero_lanci==numero_studenti:
        break

lancio_max=max(lista_lanci)
index_lancio=lista_lanci.index(lancio_max)
index_nome=lista_nomi[index_lancio]
print("Questa è la lista dei partecipanti:" , lista_nomi)
print("Questa è la lista dei lanci:" , lista_lanci)
print("Ha vinto", index_nome, "con un lancio di", lancio_max, "metri")
