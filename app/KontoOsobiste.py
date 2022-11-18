from app.Konto import Konto
class KontoOsobiste(Konto):
    def __init__(self, imie, nazwisko,pesel,kod=None):
        super().__init__(0,[])
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.czy_pesel_poprawny(pesel)
        if kod != None:
            self.czy_mozna_dodac_kod(kod)
    def czy_pesel_poprawny(self,pesel):
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel =  "Niepoprawny pesel!"
    def czy_mozna_dodac_kod(self,kod):
        if kod[0:6] == "PROMO_" and len(kod[6:]) == 3:
            if (int(self.pesel[0:2]) > 60 and self.pesel[2] in ['0','1']) or (self.pesel[2] in ['2','3']): 
                self.kod = kod
                self.saldo += 50
            else:
                self.kod = None
        else:
            self.kod = None
    def przelewEks(self, kwota):
        return super().przelewEks(kwota, oplata=1)
    def zaciagnij_kredyt(self,kwota):
        suma = 0
        for i in self.history[-5:]:
            suma += i
        czy_wpłaty = True
        for i in self.history[-3:]:
            if (i < 0):
                czy_wpłaty = False
        if czy_wpłaty and suma > kwota:
            self.saldo += kwota
            return True