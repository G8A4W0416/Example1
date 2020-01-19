import unittest
from main_source import hello_world as hello

class MyTestCase(unittest.TestCase):
    def test_hello_message(self):
        self.assertEqual("Hello, World!", hello.hello_message())


if __name__ == '__main__':
    unittest.main()
