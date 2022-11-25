import unittest
from app.RejestrKont import RejestrKont
from ..KontoOsobiste import KontoOsobiste

class TestRejestrKont(unittest.TestCase):
    imie = "Jan"
    nazwisko = "Kowalski"
    pesel = "90082285987"
    @classmethod
    def setUpClass(cls):
        konto = KontoOsobiste(cls.imie,cls.nazwisko,cls.pesel)
        RejestrKont.dodaj_konto(konto)

    def test_1_dodawanie_pierwszego_konta(self):
        konto1 = KontoOsobiste(self.imie,self.nazwisko,self.pesel)
        konto2 = KontoOsobiste(self.imie + "qweq",self.nazwisko,self.pesel)
        RejestrKont.dodaj_konto(konto1)
        RejestrKont.dodaj_konto(konto2)
        self.assertEqual(RejestrKont.ile_kont(),3)
    def test_2_dodawanie_drugiego_konta(self):
        konto = KontoOsobiste(self.imie,self.nazwisko,self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(),4)
    @classmethod
    def tearDownClass(cls):
        RejestrKont.list = []