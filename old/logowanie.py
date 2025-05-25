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



# Przejdź do logowania
try:
    login_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/login.php?login"]')
    login_button.click()
    print("Przejście do strony logowania")
except Exception as e:
    print("Nie można znaleźć przycisku logowania", e)


    
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

    # Kliknij przycisk logowania "Zaloguj się"
    login_submit = driver.find_element(By.XPATH, "//button[contains(., 'Zaloguj się')]")
    login_submit.click()
    print("Kliknięto przycisk logowania")

    time.sleep(3) 

    # Weryfikacja poprawnego logowania "Twoje konto"
    span_element = driver.find_element(By.XPATH, "//span[text()='Twoje konto']")
    print("Pomyślnie zalogowano do konta!")
    
    # Dodatkowe potwierdzenie
    time.sleep(30)
    print("Przeglądarka pozostanie otwarta...")

except Exception as e:
    print(f"Błąd podczas logowania: {e}")
    print("Przeglądarka pozostanie otwarta do ręcznej inspekcji...")