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


    def poczekaj(self, ileSekund):
          # Poczekaj na załadowanie strony
        time.sleep(ileSekund)
      

    def akceptuj_cookies(self):
        try:
            guzik_zakceptuj = self.driver.find_element(By.XPATH, "//a[text()='Potwierdzam wszystkie']")
            guzik_zakceptuj.click()
        except:
            print("Brak baneru z ciasteczkami")
