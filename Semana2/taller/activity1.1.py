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

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()