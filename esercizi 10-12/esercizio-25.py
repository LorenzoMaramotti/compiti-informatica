print("Inserire i voti e il nome del primo candidato")
voti_primo_candidato = int(input("Inserire i voti del primo candidato"))
nome1 = input("Inserire il nome del candidato")
voti_secondo_candidato = int(input("Inserire i voti del primo candidato"))
nome2 = input("Inserire il nome del candidato")
lista_nomi = [nome1, nome2]
lista_voti = [voti_primo_candidato, voti_secondo_candidato]
lista_nomi.sort()
lista_voti.sort(reverse=True)
print(lista_nomi)
print(lista_voti)