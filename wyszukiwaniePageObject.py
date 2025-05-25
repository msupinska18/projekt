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

class wyszukiwaniePage(KlasaWspolnaPage):

    def __init__(self):
        super().__init__()
        

    def otworz_strone(self):
        # Otwórz przeglądarkę Bing
        self.driver.get("https://ebutik.pl/")


    def wprowadz_bluza(self, zakladka):
        try:
            #wpisz_sukienka = self.driver.find_element(By.XPATH, "//*[@id='search']/div[4]/div/div[1]/a[1]/picture/div/div/img") 
            wpisz_bluza = self.driver.find_element(By.XPATH, "//*[@id='menu_search_text']") 
            wpisz_bluza.send_keys(zakladka)
        except:
            print("Brak wyszukiwanego produktu. Spróbuj ponownie.")
    

    def rezultat(self):        
        # Weryfikacja tekst "Wyniki wyszukiwania"
        div_napis = self.driver.find_element(By.XPATH, "//*[@id='content']/section[1]/h1/span")
        return div_napis      

    def rezultat_ilosc(self):        
        # Weryfikacja tekst "Wyniki wyszukiwania"
        span_napis = self.driver.find_element(By.XPATH, "//*[@id='content']/section[1]/span/span")
        return span_napis    
    

    #//*[@id="content"]/section[1]/span/span