numero_binario=[]
lunghezza=int(input("Da quante cifre è composto il numero? "))
ripetizione=0
for i in range (lunghezza):
    ripetizione+=1
    print("Inserisci la cifra numero" , ripetizione , ", ricordati di inserire solo cifre uguali a 1 e 0: ")
    cifra_numero=int(input())
    numero_binario.append(cifra_numero)
numero_binario.reverse()
numero_decimale=0
elevazione_potenza=0
for i in range(lunghezza):
    numero_finale=numero_binario[lunghezza-1]
    if numero_finale==0:
        numero_decimale+=0
    elif numero_finale==1:
        numero_decimale+=2**elevazione_potenza
    lunghezza-=1
    elevazione_potenza+=1
print ("Il numero decimale corrispondente è" , numero_decimale)