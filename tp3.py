import unittest
from typing import Tuple

def est_bissextile(a : int) -> bool:
    return (a % 4 == 0) and (a % 100 != 0 or a % 400 == 0)

# a = [1, 2, 3] => liste
# a = (1, 2, 3) => tuple (dans ce cas, c'est un 3-uple, soit un triplet). Un tuple n'est pas modifiable.

def lendemain(j : int, m : int, a : int) -> Tuple[int, int, int]:
    jours_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if est_bissextile(a):
        jours_mois[1] = 29
    j = j + 1
    if j > jours_mois[m-1]:
        j = 1
        m += 1
    if m == 13:
        m = 1
        a += 1
    return (j, m, a)

class Lendemain(unittest.TestCase):

    def test_bissextile_bizarre(self):
        with self.assertRaises(TypeError):
            est_bissextile("a")

    def test_bissextile_simple(self):
        self.assertFalse(est_bissextile(2021))

    def test_bissextile_simple_negatif(self):
        self.assertTrue(est_bissextile(-4))

    def test_bissextile_simple_400(self):
        self.assertFalse(est_bissextile(1900))

    def test_bissextile_simple_00(self):
        self.assertTrue(est_bissextile(2000))
        self.assertTrue(est_bissextile(1600))
        self.assertTrue(est_bissextile(2400))

    def test_demain_simple(self):
        self.assertEqual(lendemain(1,1,1), (2,1,1))

    def test_demain_simple_31janvier(self):
        self.assertEqual(lendemain(31,1,1), (1,2,1))

    def test_demain_simple_annee(self):
        self.assertEqual(lendemain(31,12,1), (1,1,2))

    def test_demain_simple_annee_negative(self):
        self.assertEqual(lendemain(31,12,-4), (1,1,-3))

    def test_demain_simple_juillet(self):
        self.assertEqual(lendemain(30,6,1), (1,7,1))

    def test_demain_simple_bissextile(self):
        self.assertEqual(lendemain(28,2,4), (29, 2, 4))

if __name__ == '__main__':
    ## Si on lance le fichier par un
    # python tp3.py
    # à la différence de
    # import tp3
    unittest.main()
