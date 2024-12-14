from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
filterwarnings("ignore")
import unittest

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		urlGeneral = 'https://www.llanogas.com/'
		print(urlGeneral)
		self.browser.get(urlGeneral)
		phone= self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div/footer/div[1]/div/div[3]/div/div/div/div/ul/li[1]/p/b")
		print(phone)
		self.assertEqual(323 254 0629, phone)


	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()