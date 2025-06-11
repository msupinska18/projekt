import pytest

from test_wyszukiwanie.wyszukiwaniePageObject import wyszukiwaniePage


def wczytaj_parametry(plik):
    with open(plik, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]  # Usunięcie białych znaków

@pytest.mark.parametrize("zakladka", wczytaj_parametry("dane\\zakladki.txt"))
def test_wyszukiwanie(zakladka):

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

    