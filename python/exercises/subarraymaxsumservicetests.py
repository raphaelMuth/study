import unittest
from parameterized import parameterized
from subarraymaxsumservice import SubArrayMaxSumService

class SubArrayMaxSumServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = SubArrayMaxSumService() 

    @parameterized.expand([
        ([-1, -2, -3, -4, -5], [-1]),
        ([1, 2, 3], [1, 2, 3]),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [4, -1, 2, 1]),
        ([-2, -3, 4, -1, -2, 1, 5, -3], [4, -1, -2, 1, 5]),
        ([5, 4, 1, 7, 8], [5, 4, 1, 7, 8])
    ])
    def test_must_solve_with_solution_one(self, input_array, expected_output):
        value = self.service.solution_one(input_array)
        self.assertEqual(value, expected_output)

    @parameterized.expand([
        ([-1, -2, -3, -4, -5], [-1]),
        ([1, 2, 3], [1, 2, 3]),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [4, -1, 2, 1]),
        ([-2, -3, 4, -1, -2, 1, 5, -3], [4, -1, -2, 1, 5]),
        ([5, 4, 1, 7, 8], [5, 4, 1, 7, 8])
    ])
    def test_must_solve_with_solution_two(self, input_array, expected_output):
        value = self.service.solution_two(input_array)
        self.assertEqual(value, expected_output)

    @parameterized.expand([
        ([-1, -2, -3, -4, -5], [-1]),
        ([1, 2, 3], [1, 2, 3]),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [4, -1, 2, 1]),
        ([-2, -3, 4, -1, -2, 1, 5, -3], [4, -1, -2, 1, 5]),
        ([5, 4, 1, 7, 8], [5, 4, 1, 7, 8])
    ])
    def test_must_solve_with_solution_three(self, input_array, expected_output):
        value = self.service.solution_three(input_array)
        self.assertEqual(value, expected_output)

if __name__ == '__main__':
    unittest.main()