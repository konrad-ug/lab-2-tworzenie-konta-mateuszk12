import unittest

from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe
class TestTransferHistory(unittest.TestCase):
    def test_transfer_history(self):
        konto1 = KontoFirmowe("polBud","1234567890")
        konto2 = KontoOsobiste("Jan","Kowalski","90082285987")
        konto1.przelewP(40)
        self.assertEqual(konto1.history,[40])
        konto1.przelewW(10)
        self.assertEqual(konto1.history,[40,-10])
        konto2.przelewP(200)
        self.assertEqual(konto2.history,[200])
        konto2.przelewW(15)
        self.assertEqual(konto2.history,[200,-15])
        konto1.przelewEks(10)
        self.assertEqual(konto1.history,[40,-10,-15])
        konto2.przelewEks(10)
        self.assertEqual(konto2.history,[200,-15,-11])
