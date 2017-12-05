# Popraw klasę Person tak, żeby posiadała ona własność full_name, którą możemy
# odczytać i ustawiać. Dodatkowo własność age powinna być ustawialna ale tylko
# jeśli podaliśmy wartość < 100


if __name__ == '__main__':
    import unittest

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.person_kid = Person('Arya', 'Stark', 11)
            self.person_adolescent = Person('Sansa', 'Stark', 17)
            self.person_adult = Person('Tyrion', 'Lannister', 27)

        def test_save_age(self):
            with self.assertRaises(ValueError):
                self.person_kid.age = 122
            self.assertEqual(self.person_kid.age, 11)

        def test_full_name(self):
            self.assertEqual(self.person_adolescent.full_name, 'Sansa Stark')
            self.person_adolescent.full_name = 'Alayne Stone'
            self.assertEqual(self.person_adolescent.first_name, 'Alayne')
            self.assertEqual(self.person_adolescent.last_name, 'Stone')

    unittest.main()

