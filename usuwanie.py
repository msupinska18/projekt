from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# Dane logowania (zmień na swoje)
#EMAIL = "msupinska18@gmail.com"
#PASSWORD = "Motylek25%"

# Ustawienia dla Chrome (aby przeglądarka się nie zamykała)
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("detach", True)

# Uruchomienie przeglądarki
driver = webdriver.Chrome(options=chrome_options)

# Otwórz przeglądarkę Bing
driver.get("https://ebutik.pl/")

# Poczekaj na załadowanie strony
time.sleep(2)

# Znajdź i kliknij przycisk "Akceptuj"
try:
    accept_button = driver.find_element(By.XPATH, "//a[text()='Potwierdzam wszystkie']")
    accept_button.click()
    print("Zaakceptowano cookies.")
    time.sleep(2)  # Czekaj na reakcję strony
except:
    print("Nie znaleziono komunikatu o cookies. Kontynuuję.")


# Wyszukaj tekst "T-Shirty"
try:
   search_filed = driver.find_element(By.XPATH, "//*[@id='menu_search_text']")
   search_filed.send_keys("T-Shirty")
   print("Wpisano wyszukiwanie - T-Shirty")
except:
   print("Brak wyszukiwanego produktu w zakładce T-Shirty. Kontynuuję.")

# Kliknij "szukaj" 
try:
  accept_button = driver.find_element(By.XPATH, "//*[@id='menu_search']/div/button")
  accept_button.click()
  print("Wybrano lupkę.")
  time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Wybranie lupy nie powiodło się. Kontynuuję.") 

# Wyszukaj produkt
try:
   search_result = driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div/h3/a")
   print("Widoczny produkt")
except:
   print("Wyszukiwarka nic nie znalazła.")

# Kliknij "szukaj" 
try:
  accept_product = driver.find_element(By.XPATH, "//*[@id='search']/div[2]/div/div[1]/a[1]/picture/div/div/img")
  accept_product.click()
  print("Wybrano produkt. Szczegóły widoczne")
  time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Wybranie produktu nie powiodło się. Spróbuj ponownie.")

# Kliknij na rozmiar produktu "S"
try:
   accept_size = driver.find_element(By.XPATH, "//*[@id='projector_sizes_cont']/div[2]")
   accept_size.click()
   print("Wybrano rozmiar produktu.")
   time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Produkt nie dostęp w wybranym rozmiarze. Spróbuj ponownie.") 

# Kliknij "Dodaj do koszyka"
try:
   accept_add = driver.find_element(By.XPATH, "//*[@id='projector_button_basket']")
   accept_add.click()
   print("Dodano produkt do koszyka.")
   time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Produkt nie został dodany do koszyka. Spróbuj ponownie.") 

 # Kliknij "Przejdź do koszyka"
try:
   accept_continue = driver.find_element(By.XPATH, "//*[@id='dialog_product_details']/div[2]/a[1]")
   accept_continue.click()
   print("Kontynuuj zakupy.")
   time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Spróbuj ponownie.")   

 # Kliknij "usuń" produkt
try:
   accept_delete = driver.find_element(By.XPATH, "//*[@id='basketedit_productslist']/table/tbody/tr[2]/td[8]/a")
   accept_delete.click()
   print("Wybrano rozmiar produktu.")
   time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Produkt nie dostęp w wybranym rozmiarze. Spróbuj ponownie.")    

# Weryfikacja czy produkt znajduje się w koszyku
try:
  accept_basket = driver.find_element(By.XPATH, "//div[@id='menu_basket']/a[@class='basket__link']")
  accept_basket.click()
  print("Twój koszyk jest pusty!")
except:
  print("Produkt widoczny w koszyku.")   



  
  

