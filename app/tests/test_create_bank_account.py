import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski","123456789098")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
    #tutaj proszę dodawać nowe testy
    def test_pesel(self):
        konto_pesel_poprawny = Konto("Jan","Kowalski","12345678900")
        konto_pesel_bledny = Konto("Jan","Kowalski","132123123123123123132")
        self.assertEqual(konto_pesel_poprawny.pesel,"12345678900","pesel nie został zapisany")
        self.assertEqual(len(konto_pesel_poprawny.pesel),11,"niepoprawna dlugosc numeru  pesel")
        self.assertEqual(konto_pesel_poprawny.pesel,"12345678900","niepoprawny pesel")
        self.assertEqual(konto_pesel_bledny.pesel,"Niepoprawny pesel!","nie dziala sprawdzanie peselu")
    def test_kod_promocyjny(self):
        konto_poprawny_kod = Konto("Jan","Kowalski","12345678900","PROMO_123")
        konto_bledny_kod1 = Konto("Jan","Kowalski","12345678900","PROM_1234")
        konto_bledny_kod2 = Konto("Jan","Kowalski","12345678900","PROM_123")
        self.assertEqual(konto_poprawny_kod.kod,"PROMO_123","blednie zapiany kod")
        self.assertEqual(konto_poprawny_kod.kod[0:5],"PROMO","blednie zapiany kod")
        self.assertEqual(konto_poprawny_kod.kod[5:9],"_123","blednie zapiany kod")
        self.assertEqual(konto_poprawny_kod.kod,"PROMO_123","blednie zapiany kod")
        self.assertEqual(len(konto_poprawny_kod.kod),9,"bledna dlugosc kodu")
        self.assertEqual(konto_bledny_kod1.kod,None,"zły kod jest możliwy do wprowadzenia")
        self.assertEqual(konto_bledny_kod2.kod,None,"zły kod jest możliwy do wprowadzenia")