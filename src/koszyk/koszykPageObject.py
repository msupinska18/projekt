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

class koszykPage(KlasaWspolnaPage):
    def __init__(self):
        super().__init__()

    def otworz_strone(self):
        # Otwórz przeglądarkę Bing
        self.driver.get("https://ebutik.pl/")

    def wprowadz_akcesoria(self, zakladka):
        try:
            wpisz_akcesoria = self.driver.find_element(By.XPATH, "//*[@id='menu_search_text']")
            wpisz_akcesoria.send_keys(zakladka)
        except:
            print("Brak wyszukiwanego produktu w zakładce Akcesoria. Spróbuj ponownie.")      


    def znajdz_produktu(self):
        try:
            znajdz_produktu = self.driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div/h3/a")
            znajdz_produktu_produktu.click()
        except:
            print("Wyszukiwarka nic nie znalazła. Spróbuj ponownie.") 


    def szukaj_(self):        
        try:
            guzik_szukaj_ = self.driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div/div[1]/a[1]/picture/div/div/img")
            guzik_szukaj_.click()
        except:
            print("Wybranie produktu nie powiodło się. Spróbuj ponownie.")  

    
    def przejdz_dalej(self):        
        try:
          guzik_przejdz_dalej = self.driver.find_element(By.XPATH, "//*[@id='basket_go_next']")
          guzik_przejdz_dalej.click()
        except:
              print("Spróbuj ponownie.")     


    def koszyk_zawartosc(self):
        try:
             guzik_koszyk_zawartosc = self.driver.find_element(By.XPATH, By.XPATH, "//div[@id='menu_basket']/a[@class='basket__link']")
             guzik_koszyk_zawartosc.click()
        except:
             print("Produkt nie dostęp w wybranym rozmiarze. Spróbuj ponownie.")      


    def zaplac(self):
        try:
             guzik_zaplac = self.driver.find_element(By.XPATH, By.XPATH, "//*[@id='basket_go_next']")
             guzik_zaplac.click()
        except:
             print("Brak możliwości zapłacenia.")  

    
    def paczka_orlen(self):
        try:
             guzik_paczka_orlen = self.driver.find_element(By.XPATH, By.XPATH, "//*[@id='delivery_100280-1']/div/div[1]/span")
             guzik_paczka_orlen.click()
        except:
             print("Brak możliwości wybrania paczkomatu.")                 

    def blik(self):
        try:
             guzik_blik = self.driver.find_element(By.XPATH, By.XPATH, "//*[@id='delivery_100280-1']/div/div[1]/span")
             guzik_blik.click()
        except:
             print("Brak możliwości wybrania opcji blik.")  


    def przejdz_dalej_1(self):        
        try:
          guzik_przejdz_dalej_1 = self.driver.find_element(By.XPATH, "//*[@id='content']/form/div[5]/div/div/div[3]/div[3]/button")
          guzik_przejdz_dalej_1.click()
        except:
              print("Brak możliwości zamówienia. Spróbuj ponownie.")

    
    def punkt_odbioru(self):        
        try:
          guzik_punkt_odbioru = self.driver.find_element(By.XPATH, "//*[@id='pickup_list_form']/div[1]/div[2]/label[1]")
          guzik_punkt_odbioru.click()
        except:
              print("Brak możliwości wybrania punktu odbioru.")

    
    def przejdz_dalej_2(self):        
        try:
          guzik_przejdz_dalej_2 = self.driver.find_element(By.XPATH, "//*[@id='pickup_list_form']/div[2]/button")
          guzik_przejdz_dalej_2.click()
        except:
              print("Brak możliwości akceptacji zamówienia. Spróbuj ponownie.")   


    def zamawiam(self):        
        try:
          guzik_zamawiam = self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/form/div[5]/div/div/div[5]/div/input")
          guzik_zamawiam.click()
        except:
              print("Brak akceptacji warunków regulaminu. Spróbuj ponownie.")                              


    def rezultat(self):        
        # Weryfikacja czy produkt znajduje się w koszyku
        div_napis = self.driver.find_element(By.XPATH, "//*[@id='content']/div[3]/form/div[5]/div/div/div[5]/div/input")
        return div_napis
        
  