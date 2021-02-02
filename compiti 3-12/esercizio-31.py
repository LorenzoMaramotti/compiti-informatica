def convertitore(num):
    if num > 1:
        convertitore(num // 2)
    print(num % 2, end='')
numero_binario=int(input("Inserisci qualsiasi numero decimale: "))
convertitore(numero_binario)