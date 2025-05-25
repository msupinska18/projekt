import pytest

from koszykPageObject import koszykPage


# Dane logowania
EMAIL = "msupinska18@gmail.com"
PASSWORD = "Motylek25%"

# Dane do wprowadzenia
zakladka = "Akcesoria"


def test_koszyk():
    koszyk = koszykPage()

    koszyk.otworz_strone()
    koszyk.poczekaj(3)

    koszyk.akceptuj_cookies()
    koszyk.poczekaj(2)

    koszyk.wprowadz_akcesoria(zakladka)
    koszyk.poczekaj(2)

    koszyk.szukaj()
    koszyk.poczekaj(2)

    koszyk.znajdz_produktu()
    koszyk.poczekaj(2)

    koszyk.szukaj_()
    koszyk.poczekaj(2)

    koszyk.dodaj_do_koszyka()
    koszyk.poczekaj(2)

    koszyk.przejdz_do_koszyka()
    koszyk.poczekaj(2)

    koszyk.przejdz_dalej()
    koszyk.poczekaj(2)
       
    koszyk.wprowadz_login_uzytkownika(EMAIL)
    koszyk.poczekaj(1)

    koszyk.wprowadz_haslo_uzytkownika(PASSWORD)
    koszyk.poczekaj(1)

    koszyk.zaloguj_sie()
    koszyk.poczekaj(1)

    koszyk.koszyk_zawartosc()
    koszyk.poczekaj(2)

    koszyk.zaplac()
    koszyk.poczekaj(2)

    koszyk.paczka_orlen()
    koszyk.poczekaj(2)

    koszyk.blik()
    koszyk.poczekaj(2)

    koszyk.przejdz_dalej_1()
    koszyk.poczekaj(2)

    koszyk.punkt_odbioru()
    koszyk.poczekaj(2)

    koszyk.przejdz_dalej_2()
    koszyk.poczekaj(2)

    koszyk.zamawiam()
    koszyk.poczekaj(2)

    rezultat_testu = koszyk.rezultat()
    if rezultat_testu != None :
        assert rezultat_testu.get_attribute("value") == "Zamawiam z obowiązkiem zapłaty"
    else:
        assert False


#test_koszyk()

            

            