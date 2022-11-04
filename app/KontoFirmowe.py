from app.Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self,nazwa,nip):
        super().__init__(0)
        self.nazwa = nazwa
        self.czy_poprawny_nip(nip)
    def czy_poprawny_nip(self,nip):
        if len(nip) != 10 or False in [x.isdigit() for x in nip] :
            self.nip = "Niepoprawny NIP!"
        else:
            self.nip = nip      
    def przelewEks(self, kwota):
        return super().przelewEks(kwota,oplata=5)
    def testCoverage:
        print("cos")
    
