from unittest import TestCase


def some_func(num):
    return num + 10


class SomeFuncTestCase(TestCase):
    def test_1(self):
        result = some_func(10)
        self.assertEqual(result, 20)

    def test_2(self):
        result = some_func(0)
        self.assertEqual(result, 10)

    def test_3(self):
        result = some_func(-10)
        self.assertEqual(result, 0)