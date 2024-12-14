from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get("https://www.dannybrien.com/random/")

table = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/section[2]/div/div/div[2]/div/div[1]/div/h3')
	print(table.text)
	print('-----------------')
browser.quit()
