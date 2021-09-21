import unittest
import random
class AbsTest(unittest.TestCase):
    def test_abs_n_accepte_pas_une_chaine_de_caracteres(self):
        with self.assertRaises(TypeError):
            abs("a")
    
    def test_abs_positif(self):
        i = random.randint(0, 100)
        self.assertEqual(i, abs(i))
    
    def test_abs_negatif(self):
        i = random.randint(-100, 0)
        self.assertEqual(i, -abs(i))
    

if __name__ == '__main__':
    unittest.main()