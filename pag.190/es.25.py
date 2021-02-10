voti_studenti={}
voti_classe=[]
numero_studenti=5
for i in range(numero_studenti):
    print("Inserisci la matricola dello studente numero", i+1)
    studente=input()
    studente=studente.capitalize()
    while True:
            print("Inserire il voto di", studente)
            voto_studente=float(input())
            break
    voti_studenti[studente]=voto_studente

elenco_finale=(sorted(voti_studenti.items(), key=lambda voto_studente:voto_studente[1]))

for e in elenco_finale:
    voto_studente=e[1]
    if not voto_studente in voti_classe:
        voti_classe.append(voto_studente)

for studenti in elenco_finale:
    print(studenti[0], "ha preso", studenti[1])

print("\n\nIn classe ci sono stati i seguenti voti")
for l in voti_classe:
    print(e, end=", ")
