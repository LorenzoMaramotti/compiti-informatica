while True:
    print("inserisci due parametri a e b e verrà calcolata l'equazione ax+b=0")
    a=int(input("inserisci il valore del parametro a: "))
    b=int(input("Inserisci il valore del parametro b: "))
    if a==0 and b==0:
        print("L'equazione è indeterminata")
    elif a==0 and b!=0:
        print("L'equazione è impossibile")
    elif a!=0 and b==0:
        print("L'equazione risulta x=0")
    elif a!=0 and b!=0:
        print("L'equazione risulta" , -b/a)
    esc=input("Per uscire premi q per continuare premi qualsiasi altra lettera")
    if esc=="q":
        print("Grazie e arrivederci")
        break