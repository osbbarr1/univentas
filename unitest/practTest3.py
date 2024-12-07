from ejercicio import mult
import unittest

class TestPracticaEjercicio1(unittest.TestCase):
    
    def test_1(self):
        resultado = mult(1)
        self.assertFalse(resultado == 10)

if __name__ == '__main__':
    unittest.main()