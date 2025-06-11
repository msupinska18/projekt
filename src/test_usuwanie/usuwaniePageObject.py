from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time, sys, os

sys.path.append(os.path.abspath("src"))  # Dodaje katalog nadrzędny do ścieżki
from KlasaWspolnaFile import KlasaWspolnaPage

class usuwaniePage(KlasaWspolnaPage):
    def __init__(self):
        super().__init__()

    def otworz_strone(self):
        # Otwórz przeglądarkę Bing
        self.driver.get("https://ebutik.pl/")

    def wprowadz_Tshirty(self, zakladka):
        try:
            wpisz_nazwe = self.driver.find_element(By.XPATH, "//*[@id='menu_search_text']")
            wpisz_nazwe.send_keys(zakladka)
        except:
            print("Brak wyszukiwanego produktu w zakładce T-Shirty. Spróbuj ponownie.")


    def przejdz_do_produktu(self):
        try:
            przejdz_do_produktu = self.driver.find_element(By.XPATH, "//*[@id='search']/div[2]/div/div[1]/a[1]/picture/div/div/img")
            przejdz_do_produktu.click()
        except:
            print("Wyszukiwarka nic nie znalazła. Spróbuj ponownie.") 


    def rozmiar_s(self):        
        # Kliknij na rozmiar produktu "S"
        try:
            guzik_rozmiar_s = self.driver.find_element(By.XPATH, "//*[@id='projector_sizes_cont']/div[2]")
            guzik_rozmiar_s.click()
        except:
            print("Produkt nie dostęp w wybranym rozmiarze. Spróbuj ponownie.") 
            

    def usun_(self):
        try:
             guzik_usun = self.driver.find_element(By.XPATH, "//*[@id='basketedit_productslist']/table/tbody/tr[2]/td[8]/a")
             guzik_usun.click()
        except:
             print("Produkt nie dostęp w wybranym rozmiarze. Spróbuj ponownie.")      

                  
    def rezultat(self):        
        # Weryfikacja czy produkt znajduje się w koszyku
        div_napis = self.driver.find_element(By.XPATH, "//*[@id='return_sub_basket_empty']/h3")
        return div_napis
        
    

    
    