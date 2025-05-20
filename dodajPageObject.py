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

class DodajPage(KlasaWspolnaPage):

    def __init__(self):
        super().__init__()
        

    def otworz_strone(self):
        # Otwórz przeglądarkę Bing
        self.driver.get("https://ebutik.pl/")


    def wprowadz_Nowosci(self, zakladka):
        try:
            wpisz_nazwe = self.driver.find_element(By.XPATH, "//*[@id='menu_search_text']")
            wpisz_nazwe.send_keys(zakladka)
        except:
            print("Wybranie lupy nie powiodło się. Spróbuj ponownie.") 


  #  def szukaj(self):
   #     try:
    #        guzik_szukaj = self.driver.find_element(By.XPATH, "//*[@id='menu_search']/div/button")
     #       guzik_szukaj.click()
      #  except:
       #     print("Wybranie produktu nie powiodło się. Spróbuj ponownie.")

    def wyszukaj_produkt(self):
        try:
            wyszukaj_produkt = self.driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div/h3/a")
            wyszukaj_produkt.click()
        except:
            print("Wyszukiwarka nic nie znalazła. Spróbuj ponownie.") 

    def wyszukaj(self):
        try:
            wyszukaj_ = self.driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div/div[1]/a[1]/picture/div/div/img")
            wyszukaj_.click()
        except:
            print("Wybranie produktu nie powiodło się. Spróbuj ponownie.")

   # def dodaj_do_koszyka(self):
       # try:
        #    guzik_dodaj_do_koszyka = self.driver.find_element(By.XPATH, "//*[@id='projector_button_basket']")
         #   guzik_dodaj_do_koszyka.click()
        #except:
         #   print("Produkt nie został dodany do koszyka. Spróbuj ponownie.")    
    
    def kontynuuj_zakupy(self):
        try:
            guzik_kontynuuj_zakupy = self.driver.find_element(By.XPATH, "//*[@id='dialog_product_details']/div[2]/a[2]")
            guzik_kontynuuj_zakupy.click()
        except:
            print("Spróbuj ponownie.")    

    def idz_do_koszyka(self):        
        # Weryfikacja czy produkt znajduje się w koszyku
        try:
            guzik_zakladka_koszyk = self.driver.find_element(By.XPATH, "//div[@id='menu_basket']/a[@class='basket__link']")
            guzik_zakladka_koszyk.click()
        except:
            print("Nie mozna przejsc do koszyka")    

    def rezultat(self):
            pole_rezultat = self.driver.find_element(By.XPATH, "//*[@id='basketedit_productslist']/h2")  
            return pole_rezultat  

            