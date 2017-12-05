# Stwórz obiekt reprezentujący osobę
# Inicjalizowany imieniem, nazwiskiem, wiekiem
# Metoda `can_drink_beer` sprawdza pełnoletniość
# Metoda `add_year` postarza osobę o rok


if __name__ == '__main__':
    import unittest

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.person_kid = Person('Arya', 'Stark', 11)
            self.person_adolescent = Person('Sansa', 'Stark', 17)
            self.person_adult = Person('Tyrion', 'Lannister', 27)

        def test_can_drink_beer(self):
            self.assertFalse(self.person_kid.can_drink_beer())
            self.assertFalse(self.person_adolescent.can_drink_beer())
            self.assertTrue(self.person_adult.can_drink_beer())

        def test_add_year(self):
            self.assertFalse(self.person_adolescent.can_drink_beer())
            self.person_adolescent.add_year()
            self.assertTrue(self.person_adolescent.can_drink_beer())
    unittest.main()

