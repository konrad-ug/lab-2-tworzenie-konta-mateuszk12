class Konto:
    def __init__(self,saldo):
        self.saldo = saldo
    def przelewW(self,kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
    def przelewP(self,kwota):
        self.saldo += kwota
    def przelewEks(self,kwota,oplata):
        if self.saldo+oplata-kwota >= 0:
            self.saldo -= (kwota+oplata)
            



