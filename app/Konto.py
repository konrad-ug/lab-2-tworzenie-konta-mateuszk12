class Konto:
    def __init__(self,saldo,history):
        self.saldo = saldo
        self.history = history
    def przelewW(self,kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            self.history.append(kwota*-1)
    def przelewP(self,kwota):
        self.saldo += kwota
        self.history.append(kwota)
    def przelewEks(self,kwota,oplata):
        if self.saldo+oplata-kwota >= 0:
            self.saldo -= (kwota+oplata)
            self.history.append((kwota+oplata)*-1)
          



