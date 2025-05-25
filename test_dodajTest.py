import pytest

from dodajPageObject import DodajPage


# Dane do wprowadzenia
zakladka = "Nowości"



def test_dodaj():
    dodajProdukt = DodajPage()

    dodajProdukt.otworz_strone()
    
    dodajProdukt.akceptuj_cookies()
    dodajProdukt.poczekaj(2)

    dodajProdukt.wprowadz_Nowosci(zakladka)
    dodajProdukt.poczekaj(2)

    dodajProdukt.szukaj()
    dodajProdukt.poczekaj(2)

    dodajProdukt.wyszukaj_produkt()
    dodajProdukt.poczekaj(2)

    dodajProdukt.wyszukaj()
    dodajProdukt.poczekaj(2)

    dodajProdukt.dodaj_do_koszyka()
    dodajProdukt.poczekaj(3)

    dodajProdukt.kontynuuj_zakupy()
    dodajProdukt.poczekaj(3)

    dodajProdukt.idz_do_koszyka()
    dodajProdukt.poczekaj(2)

    rezultat_testu = dodajProdukt.rezultat()

    if rezultat_testu != None :
        assert rezultat_testu.text == "LISTA PRODUKTÓW W KOSZYKU"
    else:
        assert False

    dodajProdukt.close_browser()

#test_dodaj()

    