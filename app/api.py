from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoOsobiste import KontoOsobiste

app = Flask(__name__)

@app.route("/konta/stworz_konto",methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    konto = RejestrKont.wyszukaj_konto(dane['pesel'])
    if konto != None:
        return jsonify("konto z podanym peselem istnieje"),400
    else:
        konto_nowe = KontoOsobiste(dane["imie"],dane["nazwisko"],dane["pesel"])
        RejestrKont.dodaj_konto(konto_nowe)
        return jsonify("konto stworzone"),201

@app.route("/konta/ile_kont",methods=['GET'])
def ile_kont():
    liczba_kont = RejestrKont.ile_kont()
    return jsonify(liczba_kont),200
@app.route("/konta/konto/<pesel>",methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    
    konto = RejestrKont.wyszukaj_konto(pesel)
    return jsonify(imie=konto.imie,nazwisko=konto.nazwisko,saldo=konto.saldo),200 
@app.route('/konta/konto/<pesel>',methods=['PUT'])
def aktualizuj_konto(pesel):

    dane = request.get_json()    
    konto = RejestrKont.wyszukaj_konto(pesel)
    konto.nazwisko = dane['nazwisko'] if 'nazwisko' in dane else dane.nazwisko
    konto.imie = dane['imie'] if 'imie' in dane else dane.imie
    konto.pesel = dane['pesel'] if 'pesel' in dane else dane.pesel
    konto.saldo = dane['saldo'] if 'saldo' in dane else dane.saldo
    return jsonify("zakończono aktualizacje danych sukcesem"),200
@app.route('/konta/konto/<pesel>',methods=['DELETE'])
def usun_konto(pesel):
    konto = RejestrKont.wyszukaj_konto(pesel)
    print(konto)
    if konto == None:
        return jsonify("brak takiego konta"),404
    else:
        RejestrKont.usun_konto(pesel)
        return jsonify("pomyślnie usunięto konto"),200
    
    