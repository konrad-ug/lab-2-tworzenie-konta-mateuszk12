class RejestrKont():
    lista = []
    @classmethod
    def dodaj_konto(cls,konto):
        cls.lista.append(konto)
    @classmethod
    def ile_kont(cls):
        return len(cls.lista)
    @classmethod
    def wyszukaj_konto(cls,pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                return konto
        return None    
    @classmethod
    def usun_konto(cls,pesel):
        for i in range(len(cls.lista)):
            if cls.lista[i].pesel == pesel:
                del cls.lista[i]
                return 1
        return None

