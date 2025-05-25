from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = None

class KlasaWspolnaPage:
    
    def __init__(self):

        # Ustawienia dla Chrome (aby przeglądarka się nie zamykała)
        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("detach", True)

        # Uruchomienie przeglądarki
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()  # Maksymalizacja okna


    def close_browser(self):
        self.poczekaj(2)
        self.driver.close()


    def wprowadz_login_uzytkownika(self, emailUzytkownika):
        pole_uzytkownika_na_stronie = self.driver.find_element(By.NAME, "login")
        pole_uzytkownika_na_stronie.send_keys(emailUzytkownika)

        
    def wprowadz_haslo_uzytkownika(self, haslo):
        pole_haslo_na_stronie = self.driver.find_element(By.NAME, "password")
        pole_haslo_na_stronie.send_keys(haslo)


    def zaloguj_sie(self):
        guzik = self.driver.find_element(By.XPATH, "//button[contains(., 'Zaloguj się')]")
        guzik.click()


    def poczekaj(self, ileSekund):
          # Poczekaj na załadowanie strony
        time.sleep(ileSekund)
      

    def akceptuj_cookies(self):
        try:
            guzik_zakceptuj = self.driver.find_element(By.XPATH, "//a[text()='Potwierdzam wszystkie']")
            guzik_zakceptuj.click()
        except:
            print("Brak baneru z ciasteczkami")

    
    def szukaj(self):
        try:
            guzik_szukaj = self.driver.find_element(By.XPATH, "//*[@id='menu_search']/div/button")
            guzik_szukaj.click()
        except:
            print("Wybranie produktu nie powiodło się. Spróbuj ponownie.")


    def dodaj_do_koszyka(self):
        try:
            guzik_dodaj_do_koszyka = self.driver.find_element(By.XPATH, "//*[@id='projector_button_basket']")
            guzik_dodaj_do_koszyka.click()
        except:
            print("Produkt nie został dodany do koszyka. Spróbuj ponownie.")    


    def przejdz_do_koszyka(self):        
        try:
            guzik_przejdz_do_koszyka = self.driver.find_element(By.XPATH, "//*[@id='dialog_product_details']/div[2]/a[1]")
            guzik_przejdz_do_koszyka.click()
        except:
            print("Spróbuj ponownie.")         