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

# Wyszukaj tekst "Akcesoria"
try:
   search_filed = driver.find_element(By.XPATH, "//*[@id='menu_search_text']")
   search_filed.send_keys("Akcesoria")
   print("Wpisano wyszukiwanie - Akcesoria")
except:
   print("Brak wyszukiwanego produktu w zakładce Akcesoria. Kontynuuję.")

# Kliknij "szukaj" 
try:
  accept_button = driver.find_element(By.XPATH, "//*[@id='menu_search']/div/button/i")
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
  accept_product = driver.find_element(By.XPATH, "//*[@id='search']/div[1]/div/div[1]/a[1]/picture/div/div/img")
  accept_product.click()
  print("Wybrano produkt. Szczegóły widoczne")
  time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Wybranie produktu nie powiodło się. Kontynuuję.")

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
   accept_add = driver.find_element(By.XPATH, "//*[@id='dialog_product_details']/div[2]/a[1]")
   accept_add.click()
   print("Przejdź do koszyka.")
   time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Produkt nie jest widoczny w koszyku. Spróbuj ponownie.") 

 # Kliknij "Przejdź dalej"
try:
   accept_buy = driver.find_element(By.XPATH, "//*[@id='basket_go_next']")
   accept_buy.click()
   print("Przejdź dalej. Kup i zapłać.")
   time.sleep(2)  # Czekaj na reakcję strony
except:
  print("Spróbuj ponownie.")   
    
# Proces logowania
try:
    # Wprowadź email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    email_input.send_keys(EMAIL)
    print("Wprowadzono email")

    # Wprowadź hasło
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "password"))
    )

    ActionChains(driver).move_to_element(password_input).click().perform()

    password_input.send_keys(PASSWORD)
    print("Wprowadzono hasło")

    # Kliknij przycisk logowania
    login_submit = driver.find_element(By.XPATH, "//button[contains(., 'Zaloguj się')]")
    login_submit.click()
    print("Kliknięto przycisk logowania")

    time.sleep(3) 

except:
   print("Nie znaleziono komunikatu o cookies. Kontynuuję.")

# Weryfikacja czy produkt znajduje się w koszyku
try:
  accept_basket = driver.find_element(By.XPATH, "//div[@id='menu_basket']/a[@class='basket__link']")
  accept_basket.click()
  print("Widoczne szczegóły koszyka!")
except:
  print("Brak koszyka.")   

# Produkt znajduje się w koszyku "Zapłać"
try:
  accept_buy_ = driver.find_element(By.XPATH, "//*[@id='basket_go_next']")
  accept_buy_.click()
  print("Widoczne szczegóły koszyka! Przejdź do zamówienia")
except:
  print("Brak możliwości przejścia do zamówienia. Spróbuj ponownie.") 

# Kliknij sposób dostawy - "Orlen paczka"
try:
  accept_pack = driver.find_element(By.XPATH, "//*[@id='delivery_100280-1']/div/div[1]/span")
  accept_pack.click()
  print("Wybrany sposób dostawy - Orlen Paczka ! Przejdź do zamówienia")
except:
  print("Brak możliwości wybrania sposobu dostawy. Spróbuj ponownie.")    

# Kliknij sposób zapłaty "BLIK"
try:
  accept_blik = driver.find_element(By.XPATH, "//*[@id='delivery_100280-1']/div/div[1]/span")
  accept_blik.click()
  print("Wybrany sposób zapłaty - BLIK! Przejdź do zamówienia")
except:
  print("Brak możliwości wybrania sposobu płatności. Spróbuj ponownie.")    
  
# Kliknij "Przejdź dalej"
try:
  accept_order = driver.find_element(By.XPATH, "//*[@id='content']/form/div[5]/div/div/div[3]/div[3]/button")
  accept_order.click()
  print("Akceptuje! Przejdź do zamówienia")
except:
  print("Brak możliwości akceptacji zamówienia. Spróbuj ponownie.") 

# Kliknij "Punkt odbioru"
try:
  accept_collection_point = driver.find_element(By.XPATH, "//*[@id='pickup_list_form']/div[1]/div[2]/label[1]")
  accept_collection_point.click()
  print("Wybrano punkt odbioru! Kontynuuj")
except:
  print("Brak możliwości wybrania punktu odbioru. Spróbuj ponownie.") 

# Kliknij "Przejdź dalej"
try:
  accept_selected = driver.find_element(By.XPATH, "//*[@id='pickup_list_form']/div[2]/button")
  accept_selected.click()
  print("Akceptuje! Przejdź do zamówienia")
except:
  print("Brak możliwości akceptacji zamówienia. Spróbuj ponownie.") 

# Kliknij "Zamawiam z obowiązkiem zapłaty"
try:
  accept_selected = driver.find_element(By.XPATH, "//*[@id='content']/div[3]/form/div[5]/div/div/div[5]/div/input")
  accept_selected.click()
  print("Akceptuje! Zamawiam z obowiązkiem zapłaty")
except:
  print("Brak akceptacji  warunków regulaminu. Spróbuj ponownie.") 
