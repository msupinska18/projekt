from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# Dane logowania
EMAIL = "msupinska18@gmail.com"
PASSWORD = "Motylek25%"

# Ustawienia dla Chrome (aby przeglądarka się nie zamykała)
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("detach", True)

# Uruchomienie przeglądarki
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()  # Maksymalizacja okna

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


# Wyszukaj tekst "Nowości"
try:
   search_filed = driver.find_element(By.XPATH, "//*[@id='menu_search_text']")
   search_filed.send_keys("Nowości")
   print("Wpisano wyszukiwanie - Nowości")
except:
   print("Brak wyszukiwanego produktu w zakładce Nowości. Spróbuj ponownie.")

# Kliknij "szukaj" 
try:
  accept_button = driver.find_element(By.XPATH, "//*[@id='menu_search']/div/button")
  accept_button.click()
  print("Wybrano lupkę.")
  time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Wybranie lupy nie powiodło się. Spróbuj ponownie.") 

# Wyszukaj produkt
try:
   search_result = driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div/h3/a")
   print("Widoczny produkt")
except:
   print("Wyszukiwarka nic nie znalazła. Spróbuj ponownie.")

# Kliknij "szukaj" 
try:
  accept_product = driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div/div[1]/a[1]/picture/div/div/img")
  accept_product.click()
  print("Wybrano produkt. Szczegóły widoczne")
  time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Wybranie produktu nie powiodło się. Spróbuj ponownie.")

# Kliknij "Dodaj do koszyka"
try:
   accept_add = driver.find_element(By.XPATH, "//*[@id='projector_button_basket']")
   accept_add.click()
   print("Dodano produkt do koszyka.")
   time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Produkt nie został dodany do koszyka. Spróbuj ponownie.") 

 # Kliknij "Kontynuuj zakupy"
try:
   accept_continue = driver.find_element(By.XPATH, "//*[@id='dialog_product_details']/div[2]/a[2]")
   accept_continue.click()
   print("Kontynuuj zakupy.")
   time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Spróbuj ponownie.")   

# Weryfikacja czy produkt znajduje się w koszyku
try:
  accept_basket = driver.find_element(By.XPATH, "//div[@id='menu_basket']/a[@class='basket__link']")
  accept_basket.click()
  print("Widoczne szczegóły koszyka!")
except:
  print("Brak produktu w koszyku.")   

    

  
  
