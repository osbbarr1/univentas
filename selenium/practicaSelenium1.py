from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://campusvirtualunillanos.co/")
numberList = browser.find_elements(By.CLASS_NAME, 'h-100')

for number in numberList:
  print(number.text)

browser.quit()
