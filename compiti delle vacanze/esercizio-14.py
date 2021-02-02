while True:
    numero1=int(input("Inserisci il primo numero: "))
    numero2=int(input("Inserisci il secondo numero: "))
    if numero1+numero2>10:
        print("La differenza tra i due numeri è" , numero1-numero2)
    elif numero1*numero2<=10:
        print("La somma tra i due numeri è" , numero1+numero2)
    esc=input("Per uscire premi q. Per continuare premi qualsiasi altra lettera ")
    if esc=="q":
        print("Grazie e arrivederci")
        break