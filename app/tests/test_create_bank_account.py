import unittest

from ..KontoOsobiste import KontoOsobiste

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = KontoOsobiste("Dariusz", "Januszewski","123456789098")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
    #tutaj proszę dodawać nowe testy
    def test_pesel(self):
        konto_pesel_poprawny = KontoOsobiste("Jan","Kowalski","12345678900")
        konto_pesel_bledny = KontoOsobiste("Jan","Kowalski","132123123123123123132")
        self.assertEqual(konto_pesel_poprawny.pesel,"12345678900","pesel nie został zapisany")
        self.assertEqual(len(konto_pesel_poprawny.pesel),11,"niepoprawna dlugosc numeru  pesel")
        self.assertEqual(konto_pesel_poprawny.pesel,"12345678900","niepoprawny pesel")
        self.assertEqual(konto_pesel_bledny.pesel,"Niepoprawny pesel!","nie dziala sprawdzanie peselu")
    def test_kod_promocyjny(self):
        konto_poprawny_kod = KontoOsobiste("Jan","Kowalski","90082285987","PROMO_123") # urodzony w 1990 roku
        konto_bledny_kod1 = KontoOsobiste("Jan","Kowalski","50010342933","PROM_1234")# urodzony w 1950 roku
        konto_bledny_kod2 = KontoOsobiste("Jan","Kowalski","12345678900","PROM_123") #
        konto_bledny_pesel = KontoOsobiste("Jan","Kowalski","50010342933","PROMO_123")
        konto_poprawny_pesel = KontoOsobiste("Jan","Kowalski","08321967998","PROMO_123")
        self.assertEqual(konto_poprawny_kod.kod[0:5],"PROMO","blednie zapisany kod")
        self.assertEqual(konto_poprawny_kod.kod[5:9],"_123","blednie zapisany kod")
        self.assertEqual(len(konto_poprawny_kod.kod),9,"bledna dlugosc kodu")
        self.assertEqual(konto_bledny_kod1.kod,None,"zły kod jest możliwy do wprowadzenia")
        self.assertEqual(konto_bledny_kod2.kod,None,"zły kod jest możliwy do wprowadzenia")
        self.assertEqual(konto_poprawny_kod.kod,"PROMO_123","kod_check nie działa poprawnie")
        self.assertEqual(konto_bledny_pesel.kod,None,"kod_check nie działa poprawnie")
        self.assertEqual(konto_poprawny_kod.saldo,50,"nie działa dodawanie 50zł")
        self.assertEqual(konto_bledny_pesel.saldo,0,"niepoprawna kwota")
        self.assertEqual(konto_poprawny_pesel.kod,"PROMO_123","kod_check nie działa poprawnie")
        self.assertEqual(konto_poprawny_pesel.saldo,50,"kod_check nie działa poprawnie")



    

        