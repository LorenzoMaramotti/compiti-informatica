while True:
    numero=int(input("Inserisci il numero che vuoi controllare se è pari o dispari: "))
    if numero%2==0:
        print("Il numero è pari")
    else:
        print("Il numero è dispari")
    esc=input("Per uscire premi q per continuare premi qualsiasi altra lettera ")
    if esc=="q":
        print("Grazie e arrivederci")
        break