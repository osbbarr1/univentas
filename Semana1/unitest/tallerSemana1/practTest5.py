from ejercicio import length
import unittest

class TestPracticaEjercicio1(unittest.TestCase):
    
    def test_1(self):
        resultado = length([2, 3, 5, 2,9,6,5,4,1,0])
        self.assertEqual("Longer than 5", resultado)

if __name__ == '__main__':
    unittest.main()