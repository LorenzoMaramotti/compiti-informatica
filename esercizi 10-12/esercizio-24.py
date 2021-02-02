voti_primo_candidato = int(input("Inserire i voti del primo candidato"))
voti_secondo_candidato = int(input("Inserire i voti del primo candidato"))
voti_totali = voti_primo_candidato + voti_secondo_candidato
percentuale_primo_candidato = (voti_primo_candidato*100)/voti_totali
percentuale_secondo_candidato= 100-voti_secondo_candidato
if percentuale_primo_candidato > percentuale_secondo_candidato:
    print("Ha vinto il primo candidato con " , voti_primo_candidato , "con una percentuale del" , percentuale_primo_candidato , "%")
else:
    print("Ha vinto il secondo candidato con " , voti_secondo_candidato , "con una percentuale del" , percentuale_secondo_candidato , "%" )