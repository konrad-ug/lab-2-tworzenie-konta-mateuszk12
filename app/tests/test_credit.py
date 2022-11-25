import unittest
from parameterized import parameterized, parameterized_class

from ..KontoOsobiste import KontoOsobiste

class TestCredit(unittest.TestCase):
    imie = "Jan"
    nazwisko = "Kowalski"
    pesel = "90082285987"

    def setUp(self):
        self.konto = KontoOsobiste(self.imie,self.nazwisko,self.pesel)

    @parameterized.expand([
        ([-100,100,100,100,600],500,True,500),
        ([],500,False,0),
        ([-100,100,100,-100,600],500,False,0),
        ([-100,100,100,100,100],500,False,0),
        ([-100,100,100,-100,600],500,False,0),
    
    ])
    def test_getting_credit(self,historia,kwota,oczekiwany_wynik,oczekiwane_saldo):
        self.konto.history = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEquals(czy_przyznany,oczekiwany_wynik)
        self.assertEqual(self.konto.saldo,oczekiwane_saldo)

        
