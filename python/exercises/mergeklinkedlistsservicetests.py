from typing import List
import unittest
from parameterized import parameterized
from mergeklinkedlistsservice import ListNode, MergeKLinkedListsService
import time

class MergeKLinkedListsServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = MergeKLinkedListsService()

    @parameterized.expand([
        (
            [
                ListNode(1, ListNode(4, ListNode(15))), 
                ListNode(3, ListNode(9, ListNode(10))), 
                ListNode(6, ListNode(7, ListNode(20)))
            ], 
            [1,3,4,6,7,9,10,15,20]
        ),
        (
            [
                ListNode(6, ListNode(7, ListNode(20))),
                ListNode(3, ListNode(9, ListNode(10))), 
                ListNode(1, ListNode(4, ListNode(15)))
            ], 
            [1,3,4,6,7,9,10,15,20]
        ),
        (
            [
                ListNode(1, ListNode(6, ListNode(7))),
                ListNode(8, ListNode(9))
            ], 
            [1,6,7,8,9]
        ),
        (
            [
                ListNode(1, ListNode(4, ListNode(5))),
                ListNode(1, ListNode(3, ListNode(4))), 
                ListNode(2, ListNode(6))
            ], 
            [1,1,2,3,4,4,5,6]
        ),
        (
            [
                ListNode(1, ListNode(2, ListNode(3))),
                ListNode(2, ListNode(3, ListNode(9))),
                ListNode(4, ListNode(4, ListNode(7)))
            ], 
            [1,2,2,3,3,4,4,7,9]
        ),
        (
            [
                ListNode(1, ListNode(1, ListNode(1))),
                ListNode(1, ListNode(1, ListNode(1))),
                ListNode(1, ListNode(1, ListNode(1)))
            ], 
            [1,1,1,1,1,1,1,1,1]
        ),
        (
            [
                ListNode(7, ListNode(8, ListNode(9))),
                ListNode(4, ListNode(5, ListNode(6))),
                ListNode(1, ListNode(2, ListNode(3)))
            ], 
            [1,2,3,4,5,6,7,8,9]
        ),
        (
            [
                ListNode(7, ListNode(8, ListNode(9))),
                ListNode(4, ListNode(5)),
                ListNode(1, ListNode(2, ListNode(3)))
            ], 
            [1,2,3,4,5,7,8,9]
        ),
        (
            [
                ListNode(7, ListNode(8, ListNode(9))),
                ListNode(4, ListNode(5)),
                ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
            ], 
            [1,2,3,4,4,5,7,8,9]
        ),
        (
            [
                ListNode(7),
                ListNode(4, ListNode(5))
            ], 
            [4,5,7]
        ),
        (
            [
                ListNode(1)
            ], 
            [1]
        ),
        (
            [
                ListNode(1),
                ListNode(1)
            ], 
            [1,1]
        ),
        (
            [
                ListNode(1),
                ListNode(2)
            ], 
            [1,2]
        ),
        (
            [
                ListNode(3),
                ListNode(2),
                ListNode(1)
            ], 
            [1,2,3]
        )
    ])
    def test_must_solve_with_solution_one(self, input_array, expected_output):
        value = self.service.solution_one(input_array)
        self.assertEqual(value.to_arr(), expected_output)

if __name__ == '__main__':
    unittest.main()