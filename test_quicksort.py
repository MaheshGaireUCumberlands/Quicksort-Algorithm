import random
import unittest

from quicksort import (
    deterministic_quicksort,
    generate_input,
    is_sorted,
    randomized_quicksort,
)


class TestQuicksort(unittest.TestCase):
    """Unit tests for deterministic and randomized Quicksort implementations."""

    def test_empty_list(self):
        """Verify sorting an empty list returns an empty list."""
        self.assertEqual(deterministic_quicksort([]), [])
        self.assertEqual(randomized_quicksort([]), [])

    def test_single_element(self):
        """Verify sorting a single-element list returns the same element."""
        self.assertEqual(deterministic_quicksort([42]), [42])
        self.assertEqual(randomized_quicksort([42]), [42])

    def test_sorted_input(self):
        """Verify that already sorted input remains unchanged after sorting."""
        arr = list(range(10))
        self.assertEqual(deterministic_quicksort(arr), arr)
        self.assertEqual(randomized_quicksort(arr), arr)

    def test_reverse_sorted_input(self):
        """Verify that reverse-sorted input is correctly sorted into ascending order."""
        arr = list(range(10, 0, -1))
        expected = sorted(arr)
        self.assertEqual(deterministic_quicksort(arr), expected)
        self.assertEqual(randomized_quicksort(arr), expected)

    def test_random_input(self):
        """Verify sorting of a random list produces the correct output."""
        random.seed(123)
        arr = [random.randint(-100, 100) for _ in range(50)]
        expected = sorted(arr)
        self.assertEqual(deterministic_quicksort(arr), expected)
        self.assertEqual(randomized_quicksort(arr), expected)

    def test_does_not_modify_input(self):
        """Verify the original input list is not modified by sorting functions."""
        arr = [3, 1, 2]
        copy_for_deterministic = arr[:]
        copy_for_randomized = arr[:]
        deterministic_quicksort(copy_for_deterministic)
        randomized_quicksort(copy_for_randomized)
        self.assertEqual(arr, [3, 1, 2])

    def test_is_sorted_helper(self):
        """Verify the helper function correctly identifies sorted and unsorted lists."""
        self.assertTrue(is_sorted([1, 2, 2, 3]))
        self.assertFalse(is_sorted([1, 3, 2]))

    def test_generate_input_distributions(self):
        """Verify that input generation supports random, sorted, and reverse-sorted cases."""
        random.seed(0)
        random_data = generate_input(10, "random")
        self.assertEqual(len(random_data), 10)
        self.assertEqual(generate_input(5, "sorted"), [0, 1, 2, 3, 4])
        self.assertEqual(generate_input(5, "reverse-sorted"), [5, 4, 3, 2, 1])

    def test_same_result_for_deterministic_and_randomized(self):
        """Ensure both implementations produce the same sorted result on same input."""
        random.seed(0)
        arr = [random.randint(0, 200) for _ in range(100)]
        self.assertEqual(deterministic_quicksort(arr), randomized_quicksort(arr))


if __name__ == "__main__":
    unittest.main()
