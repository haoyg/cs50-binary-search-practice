"""Find the boundary bug in an inclusive binary search."""

import unittest


def binary_search(values, target):
    lo, hi = 0, len(values) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


class BinarySearchTests(unittest.TestCase):
    def test_middle(self):
        self.assertEqual(binary_search([2, 5, 9], 5), 1)

    def test_last_element(self):
        self.assertEqual(binary_search([2, 5, 9], 9), 2)

    def test_single_element(self):
        self.assertEqual(binary_search([9], 9), 0)

    def test_missing(self):
        self.assertEqual(binary_search([2, 5, 9], 4), -1)

    def test_empty(self):
        self.assertEqual(binary_search([], 9), -1)


if __name__ == "__main__":
    unittest.main()
