import unittest

from ..KontoFirmowe import KontoFirmowe
class TestKontaFirmowe(unittest.TestCase):
    def test_tworzenie_konta_firmowego(self):
        konto1 = KontoFirmowe("Januszex","1234567890")
        konto2 = KontoFirmowe("PolBudTrans","123456")
        konto3 = KontoFirmowe("TransPol","123456g890")
        self.assertEqual(konto1.saldo,0)
        self.assertEqual(len(konto1.nip),10)
        self.assertEqual(konto1.nazwa,"Januszex")
        self.assertEqual(konto2.nip,"Niepoprawny NIP!")
        self.assertEqual(konto3.nip,"Niepoprawny NIP!")

