import unittest
from subarraymaxsumservice import SubArrayMaxSumService

class SubArrayMaxSumServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = SubArrayMaxSumService()

    def test_say_hello(self):
        self.assertEqual(self.service.say_hello("GitHub Copilot"), "Hello, GitHub Copilot!")

    def test_say_helloa(self):
        value = self.service.solve([1,2,3])
        self.assertEqual(value, [1,2,3])

    def test_say_helloaaa(self): 
        value = self.service.solve([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(value, [4, -1, 2, 1])

if __name__ == '__main__':
    unittest.main()