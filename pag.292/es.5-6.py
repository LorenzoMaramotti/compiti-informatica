class Prodotto:
    def __init__(self , nome,  numero , provenienza, prezzo):
        self.nome = nome
        self.numero = numero
        self.prezzo = prezzo
        self.provenienza = provenienza

    def assegna_prezzo(self):
        self.prezzo = self.prezzo*self.numero

    def informazioni(self):
        print("Il prodotto" , self.nome , "proviene da" , self.provenienza , "e costa" , self.prezzo , "€")

p1 = Prodotto("nome prodotto" , quantità ,"stato di provenienza" , prezzo)
p1.assegna_prezzo()
p1.informazioni()
