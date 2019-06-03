# Popraw klasę Person tak, żeby posiadała
# ona własność full_name, którą możemy
# odczytać i ustawiać. Dodatkowo własność
# age powinna być ustawialna ale tylko
# jeśli podaliśmy wartość < 100. Przy błędzie rzuć ValueError


class Person():
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        if age > 100:
            raise ValueError('Too old')
        self.age = age

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])
    
    def set_full_name(self, full_name):
        self.first_name, self.last_name = full_name.split(' ')
        

if __name__ == '__main__':
    import unittest

    class TestPerson(unittest.TestCase):

        def setUp(self):
            self.person_kid = Person('Arya', 'Stark', 11)
            self.person_adolescent = Person('Sansa', 'Stark', 17)
            self.person_adult = Person('Tyrion', 'Lannister', 27)

        def test_init_old(self):
            with self.assertRaises(ValueError):
                Person('Arya', 'Stark', 121)

        def test_save_age(self):
            with self.assertRaises(ValueError):
                self.person_kid.age = 122
            self.assertEqual(self.person_kid.age, 11)
            self.person_kid.age = 14
            self.assertEqual(self.person_kid.age, 14)

        def test_full_name(self):
            self.assertEqual(self.person_adolescent.full_name, 'Sansa Stark')
            self.person_adolescent.full_name = 'Alayne Stone'
            self.assertEqual(self.person_adolescent.first_name, 'Alayne')
            self.assertEqual(self.person_adolescent.last_name, 'Stone')

    unittest.main()
