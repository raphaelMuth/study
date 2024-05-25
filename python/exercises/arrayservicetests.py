import unittest
from arrayservice import ArrayService

class ArrayServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = ArrayService()

    def test_say_hello(self):
        self.assertEqual(self.service.say_hello("GitHub Copilot"), "Hello, GitHub Copilot!")

if __name__ == '__main__':
    unittest.main()