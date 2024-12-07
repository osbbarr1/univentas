from ejercicio import addit
import unittest

class TestPracticaEjercicio1(unittest.TestCase):
    
    def test_1(self):
        resultado = addit(5)
        self.assertNotEqual(11, resultado)

if __name__ == '__main__':
    unittest.main()