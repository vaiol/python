from datetime import date
from unittest import TestCase, skip, expectedFailure
from person import Person


class PersonTestCase(TestCase):
    def setUp(self):
        self.person = Person('TestName', 'TestLastName', date(1995, 7, 8))

    def tearDown(self):
        del self.person

    def test_age(self):
        self.assertEqual(self.person.age, 27)

    def test_age_getter(self):
        self.assertEqual(self.person.get_age(), 27)

    def test_age_zero(self):
        self.person.birth_date = date(2022, 7, 8)
        self.assertEqual(self.person.age, 0)

    def test_age_zero(self):
        self.person.birth_date = date(1990, 7, 8)
        self.assertEqual(self.person.age, 32)

    def test_x_str(self):
        self.assertEqual(str(self.person), 'Person TestName TestLastName, 27 years old.')

    def test_ask_false(self):
        self.assertFalse(self.person.ask('Some question?'))
    
    @skip("temp false")
    def test_ask_true(self):
        self.assertTrue(self.person.ask('Do you love coffee?'))

    @expectedFailure
    def test_ask_failure(self):
        self.person.ask('Do you know pragramming?')

    def test_ask_exc(self):
        with self.assertRaises(Exception) as cm:
            self.person.ask('Do you know programming?')




## Available asserts
# assertEqual(a, b) -> a == b
# assertNotEqual(a, b) -> a != b
# assertTrue(x) -> bool(x) is True
# assertFalse(x) -> bool(x) is False
# assertIs(a, b) -> a is b
# assertIsNot(a, b) -> a is not b
# assertIsNone(x) -> x is None
# assertIsNotNone(x) -> x is not None
# assertIn(a, b) -> a in b
# assertNotIn(a, b) -> a not in b
# assertIsInstance(a, b) -> isinstance(a, b)
# assertNotIsInstance(a, b) -> not isinstance(a, b)
