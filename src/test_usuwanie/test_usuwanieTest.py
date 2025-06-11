import pytest

from test_usuwanie.usuwaniePageObject import usuwaniePage


# Dane do wprowadzenia
zakladka = "T-shirty"



def test_usuwanie():
    usuwanieProduktu = usuwaniePage()

    usuwanieProduktu.otworz_strone()
    usuwanieProduktu.poczekaj(2)
    
    usuwanieProduktu.akceptuj_cookies()
    usuwanieProduktu.poczekaj(2)

    usuwanieProduktu.wprowadz_Tshirty(zakladka)
    usuwanieProduktu.poczekaj(2)

    usuwanieProduktu.szukaj()
    usuwanieProduktu.poczekaj(2)

    usuwanieProduktu.przejdz_do_produktu() 
    usuwanieProduktu.poczekaj(2)

    usuwanieProduktu.rozmiar_s()
    usuwanieProduktu.poczekaj(2)

    usuwanieProduktu.dodaj_do_koszyka()
    usuwanieProduktu.poczekaj(3)

    usuwanieProduktu.przejdz_do_koszyka()
    usuwanieProduktu.poczekaj(2)
    
    usuwanieProduktu.usun_()
    usuwanieProduktu.poczekaj(2)

    rezultat_testu = usuwanieProduktu.rezultat()

    if rezultat_testu != None :
        assert rezultat_testu.text == "Twój koszyk jest pusty."
    else:
        assert False

    usuwanieProduktu.close_browser()

#test_usuwanie()

            