voti_studenti={}
numero_studenti=5
somma_voti=0
for i in range(numero_studenti):
    print("Inseririsci la matricola dello studente numero", i+1)
    studente=input()
    studente=studente.capitalize()
    while True:
            print("Inserire il voto di", studente)
            voto=float(input())
            break
    somma_voti+=voto
    voti_studenti[studente]=voto

media=somma_voti/numero_studenti

for s in voti_studenti:
    if voti_studenti[s]>media:
        print("Lo studente" , s , "ha superato la media voti della classe")