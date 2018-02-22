import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


class HelloWordTestCase(unittest.TestCase):
    def hello_world(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
