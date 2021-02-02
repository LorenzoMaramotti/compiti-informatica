while True:
    scelta=input("Premi q per calcolare l'area del quadrato, premi r per calcolare l'area del rettangolo, premi c pre calcolare l'area de cerchio, premi t per calcolare l'area del triangolo. Per uscire scrivi esc ")
    if scelta=="q":
        lato=int(input("Inserisci la lunghezza del lato: "))
        areaq=lato**2
        print("L'area del quadrato è" , areaq , "m*2")
    elif scelta=="r":
        base=int(input("Inserisci la lunghezza della base: "))
        altezza=int(input("Inserisci la lunghezza dell'altezza: "))
        arear=base*altezza
        print("L'area del quadrato è" , arear , "m*2")
    elif scelta=="c":
        raggio=int(input("Inserisci la lunghezza del raggio: "))
        areac=raggio**2*3.14
        print("L'area del raggio e di" , areac , "m*2")
    elif scelta=="t":
        baset=int(input("Inserisci la lunghezza della base: "))
        altezzat=int(input("Inserisci la lunghezza dell'altezza: "))
        areat=baset*altezzat/2
        print("L'area del raggio e di" , areat , "m*2")
    elif scelta=="esc":
        print("Arrivederci grazie")
        break
    else:
        print("Non hai selezionato una lettera valida")