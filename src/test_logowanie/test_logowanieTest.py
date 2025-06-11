import pytest

from test_logowanie.logowaniePageObject import LoginPage


# Dane logowania
EMAIL = "msupinska18@gmail.com"
PASSWORD = "Motylek25%"


def test_logowanie_tylko_z_podanym_username():
    mojLoginPage = LoginPage()

    mojLoginPage.otworz_strone()
    mojLoginPage.poczekaj(3)

    mojLoginPage.akceptuj_cookies()
    mojLoginPage.poczekaj(1)

    mojLoginPage.wprowadz_login_uzytkownika(EMAIL)
    mojLoginPage.poczekaj(1)

    mojLoginPage.zaloguj_sie()

    rezultat_testu = mojLoginPage.rezultat()
    assert rezultat_testu == None

    mojLoginPage.poczekaj(2)

    rezultat_logowania = mojLoginPage.zly_login()
    assert rezultat_logowania.text == "Podany login lub hasło nie jest poprawne."

    mojLoginPage.close_browser()
    

def test_logowanie():
    mojLoginPage = LoginPage()

    mojLoginPage.otworz_strone()
    mojLoginPage.poczekaj(3)

    mojLoginPage.akceptuj_cookies()
    mojLoginPage.poczekaj(1)

    mojLoginPage.wprowadz_login_uzytkownika(EMAIL)
    mojLoginPage.poczekaj(1)

    mojLoginPage.wprowadz_haslo_uzytkownika(PASSWORD)

    mojLoginPage.zaloguj_sie()

    rezultat_testu = mojLoginPage.rezultat()

    assert rezultat_testu != None and rezultat_testu.text == "Twoje konto"


    mojLoginPage.close_browser()

#test_logowanie_tylko_z_podanym_username()

