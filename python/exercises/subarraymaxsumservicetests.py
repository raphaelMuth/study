import unittest
from parameterized import parameterized
from subarraymaxsumservice import SubArrayMaxSumService
import time

class SubArrayMaxSumServicePerformanceTest(unittest.TestCase):
    def setUp(self):
        self.service = SubArrayMaxSumService()

    @parameterized.expand([
        ([-1, -2, -3, -4, -5],),
        ([1, 2, 3],),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4],),
        ([-2, -3, 4, -1, -2, 1, 5, -3],),
        ([5, 4, 1, 7, 8],),
        ([-2, -1, -3, -4, -1, -2, 1, -5, 4, 4, -5, -6, -1, -9, 8, 0, -2, 1, -1, 45, -6, -7, 2, -4, 1, -4, -2, -6, 7, -8, 1, -2, 5, -1, 2, -9, 0],),
    ])
    def test_performance(self, input):
        results_one = []
        for _ in range(20):
            start_time = time.time()
            self.service.solution_one(input) 
            results_one.append(time.time() - start_time)

        results_two = []
        start_time = time.time()
        for _ in range(20):
            start_time = time.time()
            self.service.solution_two(input) 
            results_two.append(time.time() - start_time)

        results_three = []
        for _ in range(20):
            start_time = time.time()
            self.service.solution_three(input) 
            results_three.append(time.time() - start_time)

        print(f"\r\n  one => {round(sum(results_one)/len(results_one), 8):.8f} | two => {round(sum(results_two)/len(results_two), 8):.8f} | three => {round(sum(results_three)/len(results_three), 8):.8f} | arr => {input}")

        self.assertTrue(True)

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