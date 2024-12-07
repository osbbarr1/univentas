from selenium import webdriver
import time

from warnings import filterwarnings
filterwarnings("ignore")

browser = webdriver.Chrome()
browser.get("https://campusvirtualunillanos.co/")
time.sleep(2)
browser.get("https://web.whatsapp.com/")
time.sleep(2)
browser.get("https://getbootstrap.com/")
time.sleep(2)
browser.back()
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
#browser.quit()

try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()




try:
    print("Navegador abierto. Presiona Ctrl+C para salir.")
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("\nCerrando navegador...")
    browser.quit()
