import unittest
from parameterized import parameterized, parameterized_class

from ..KontoFirmowe import KontoFirmowe

class TestCredit(unittest.TestCase):
    nazwa = "Januszex"
    nip = "1234567890"

    def setUp(self):
        self.konto = KontoFirmowe(self.nazwa,self.nip)

    @parameterized.expand([
        ([1765,10],500,1775,False,1775),
        ([1775,10],2000,1785,False,1785),
        ([],500,0,False,0),
        ([1775,10],500,1785,True,2285),
    
    ])
    def test_getting_credit(self,historia,kwota,saldo,oczekiwany_wynik,oczekiwane_saldo):
        self.konto.saldo = saldo
        self.konto.history = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEquals(czy_przyznany,oczekiwany_wynik)
        self.assertEqual(self.konto.saldo,oczekiwane_saldo)