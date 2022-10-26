class Konto:
    def __init__(self, imie, nazwisko,pesel,kod=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel_check(pesel)
        if kod != None:
            self.kod_check(kod)
    def pesel_check(self,pesel):
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel =  "Niepoprawny pesel!"
    def kod_check(self,kod):
        if kod[0:6] == "PROMO_" and len(kod[6:]) == 3:
            self.kod = kod
        else:
            self.kod = None


        

