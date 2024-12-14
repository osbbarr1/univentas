from ejercicio import divide
import unittest

class TestPracticaEjercicio1(unittest.TestCase):
    
    def test_1(self):
        resultado = divide(1,1)
        self.assertIn(resultado,[1,0,2,221])

if __name__ == '__main__':
    unittest.main()