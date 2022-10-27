from typing import List


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
            if (int(self.pesel[0:2]) > 60 and self.pesel[2] in ['0','1']) or (self.pesel[2] in ['2','3']): 
                self.kod = kod
                self.saldo += 50
            else:
                self.kod = None
        else:
            self.kod = None




