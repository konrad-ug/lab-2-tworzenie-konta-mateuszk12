import unittest
import requests
class TestObslugaKont(unittest.TestCase):
    body = {
        'imie':'Jan',
        'nazwisko':'Kowalski',
        'pesel':'08321967998'
    }
    body2 = {
        'imie':'Krzysztof',
        'nazwisko':'Krawczyk',
        'pesel':'09324967988',
        'saldo':100
    }

    url = 'http://localhost:5000'

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto",json = self.body)
        self.assertEqual(create_resp.status_code,201)
    def test_2_get_na_peselu(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code,200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"],self.body["nazwisko"])
        self.assertEqual(resp_body['imie'],self.body["imie"])
        self.assertEqual(resp_body['saldo'],0)
    def test_3_put(self):
        create_resp = requests.put(self.url + f"/konta/konto/{self.body['pesel']}",json=self.body2)
        self.assertEqual(create_resp.status_code,200)
    def test_4_zmiana(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body2['pesel']}")
        self.assertEqual(get_resp.status_code,200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"],self.body2["nazwisko"])
        self.assertEqual(resp_body['imie'],self.body2["imie"])
        self.assertEqual(resp_body['saldo'],100)
    def test_5_usuwanie(self):
        create_resp = requests.delete(self.url + f"/konta/konto/{self.body2['pesel']}",json=self.body2)
        self.assertEqual(create_resp.status_code,200)