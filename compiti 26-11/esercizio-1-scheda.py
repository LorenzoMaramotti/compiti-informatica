def controllo(nome):
    indice = (len(nome) -1)
    nuovo_nome = ""
    while indice >= 0:
        nuovo_nome += nome[indice]
        indice -= 1
    if nuovo_nome == nome:
        print("Il nome" , nome ,  "è palindromo")
    else:
        print("Il nome" , nome , "non è palindromo")


nome=input("Inserisci il nome che vuoi sapere se è palindromo ")
controllo(nome)


