# Stwórz klasę Circle reprezentującą koło. Klasa ta powinna być inicjalizowana
# promieniem oraz posiadać właściwość area -- pole. Dodawanie obiektów tej
# klasy powinno dawać nam koło o *polu* równym sumie pól oryginalnych.
import math


if __name__ == '__main__':
    import unittest

    class TestCircle(unittest.TestCase):
        def setUp(self):
            self.circle1 = Circle(3.0)
            self.circle2 = Circle(7.0)

        def test_add(self):
            self.assertAlmostEqual(
                self.circle1.area + self.circle2.area, 
                (self.circle1 + self.circle2).area
            )

        def test_area(self):
            self.assertAlmostEqual(self.circle1.area, 28.274333882308138)
            self.assertAlmostEqual(self.circle2.area, 153.93804002589985)

    unittest.main()
