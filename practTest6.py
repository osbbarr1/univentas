from ejercicio import reverse
import unittest

class TestPracticaEjercicio1(unittest.TestCase):
    
    def test_1(self):
        resultado = reverse("casa")
        self.assertEqual("asac", resultado)

if __name__ == '__main__':
    unittest.main()