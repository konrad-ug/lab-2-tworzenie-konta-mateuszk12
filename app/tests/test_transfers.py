import unittest

from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe
class TestPrzelewy(unittest.TestCase):
    def test_przelew_przychodzący(self):
        konto1 = KontoOsobiste("Jan","Kowalski","90082285987","PROMO_123")
        konto1.przelewP(20)
        self.assertEqual(konto1.saldo,70)
    def test_przelew_wychodzący(self):
        konto1 = KontoOsobiste("Jan","Kowalski","90082285987","PROMO_123")
        konto2 = KontoOsobiste("Jan","Kowalski","90082285987")
        konto1.przelewW(20)
        self.assertEqual(konto1.saldo,30)
        konto2.przelewW(40)
        self.assertEqual(konto2.saldo,0)
    def test_przelew_ekspresowy(self):
        konto1 = KontoOsobiste("Jan","Kowalski","90082285987","PROMO_123")
        konto2 = KontoFirmowe("KowalPol","1234567890")
        konto1.przelewEks(50)
        self.assertEqual(konto1.saldo,-1)
        konto2.przelewEks(40)
        self.assertEqual(konto2.saldo,0)
        konto1.przelewP(10)
        konto1.przelewEks(5)
        self.assertEqual(konto1.saldo,3)
        konto2.przelewP(20)
        konto2.przelewEks(10)
        self.assertEqual(konto2.saldo,5)
        konto2.przelewEks(5)
        self.assertEqual(konto2.saldo,-5)
        konto2.przelewEks(30)
        self.assertEqual(konto2.saldo,-5)
