import pytest

from wyszukiwaniePageObject import wyszukiwaniePage


# Dane do wprowadzenia
zakladka = "bluza"



def test_wyszukiwanie():
    wyszukiwanie = wyszukiwaniePage()

    wyszukiwanie.otworz_strone()
    
    wyszukiwanie.akceptuj_cookies()
    wyszukiwanie.poczekaj(2)

    wyszukiwanie.wprowadz_bluza(zakladka)
    wyszukiwanie.poczekaj(3)

    wyszukiwanie.szukaj()
    wyszukiwanie.poczekaj(2)

    rezultat_testu = wyszukiwanie.rezultat()

    if rezultat_testu != None :
        assert rezultat_testu.text == "WYNIKI WYSZUKIWANIA"
    else:
        assert False

    rezultat_testu_ilosc = wyszukiwanie.rezultat_ilosc()

    if rezultat_testu_ilosc != None :
        assert int(rezultat_testu_ilosc.text) > 0
    else:
        assert False

    wyszukiwanie.close_browser()


#test_wyszukiwanie()

    