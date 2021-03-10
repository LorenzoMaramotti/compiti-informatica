
class atleta:
    def __init__(self , nome , altezza , sport , anni , squadra = 0 , visita_medica = False):
        self.nome = nome
        self.sport = sport
        self.altezza = altezza
        self.anni = anni
        self.visitaMedica = visita_medica
    def squadra (self , nome_squadra):
        self.squadra = nome_squadra
    def visualizza_dati(self):
        print("Ciao, mi chiamo", self.nome, "sono alto", self.altezza, "metri, pratico", self.sport, "la mia squadra è", self.squadra, "e ho effettuato la visita medica")
    def effettua_visita(self):
        self.visita_medica = True
a1 = atleta("Nome", altezza, "sport", anni)
a1.squadra ("squadra")
a1.visualizza_dati()
a1.effettua_visita()

