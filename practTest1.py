from ejercicio import total
import unittest

class TestPracticaEjercicio1(unittest.TestCase):
    
    def test_1(self):
        resultado = total([2,4])
        self.assertEqual(6, resultado)

if __name__ == '__main__':
    unittest.main()