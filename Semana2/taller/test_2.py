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
		urlGeneral = 'https://www.flashscore.co/futbol/colombia/'
		urls = ['primera-a/', 'primera-b', 'liga-femenina']

		for url in urls:
			print("Resultado -> %s" % url)
			print("%s%s" % (urlGeneral, url))
			self.browser.get("%s%s" % (urlGeneral, url))
			numberList = self.browser.find_elements(By.CLASS_NAME, 'heading__info')
			res = []
			for number in numberList:
				res.append(number.text)
				self.assertEqual("2024", number.text)

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()