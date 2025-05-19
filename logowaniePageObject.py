from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from KlasaWspolnaFile import KlasaWspolnaPage

class LoginPage(KlasaWspolnaPage):
    def __init__(self):
        super().__init__()

    def otworz_strone(self):
        # Otwórz przeglądarkę Bing
        self.driver.get("https://ebutik.pl/login.php?login")


    def wprowadz_login_uzytkownika(self, emailUzytkownika):
        pole_uzytkownika_na_stronie = self.driver.find_element(By.NAME, "login")
        pole_uzytkownika_na_stronie.send_keys(emailUzytkownika)

        
    def wprowadz_haslo_uzytkownika(self, haslo):
        pole_haslo_na_stronie = self.driver.find_element(By.NAME, "password")
        pole_haslo_na_stronie.send_keys(haslo)


    def zaloguj_sie(self):
        guzik = self.driver.find_element(By.XPATH, "//button[contains(., 'Zaloguj się')]")
        guzik.click()


    def rezultat(self):        
        # Weryfikacja poprawnego logowania "Twoje konto"
        try:
            span_element = self.driver.find_element(By.XPATH, "//span[text()='Twoje konto']")
            return span_element
        except:
            print("PROBLEM !!!!")
    

    def zly_login(self):
        div_zly_login = self.driver.find_element(By.XPATH, "//*[@id='return_sub_account_badlogin']/h3")
        return div_zly_login
    