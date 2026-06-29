"""Quicksort implementation for deterministic and randomized pivots.

This module provides:
- deterministic_quicksort: classic quicksort using the last element as pivot.
- randomized_quicksort: quicksort with a random pivot selection.
- empirical comparison helpers for random, sorted, and reverse-sorted input.
"""

import random
import time
from typing import List, Callable, Tuple


def deterministic_quicksort(arr: List[int]) -> List[int]:
    """Return a sorted copy of arr using deterministic Quicksort.

    This implementation does not modify the original list. It copies the input
    array and applies an in-place recursive Quicksort over the copied list.
    The pivot selection strategy is deterministic: the last element of each
    partition is used as the pivot.

    Args:
        arr: The input list of integers.

    Returns:
        A new list containing the sorted values.
    """
    if len(arr) <= 1:
        return arr[:]
    arr_copy = arr[:]
    _quicksort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def randomized_quicksort(arr: List[int]) -> List[int]:
    """Return a sorted copy of arr using randomized Quicksort.

    The algorithm randomly selects a pivot from the current subarray before
    partitioning. This reduces the chance of consistently poor pivot choices
    for certain input orderings.

    Args:
        arr: The input list of integers.

    Returns:
        A new list containing the sorted values.
    """
    if len(arr) <= 1:
        return arr[:]
    arr_copy = arr[:]
    _randomized_quicksort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def _quicksort(arr: List[int], low: int, high: int) -> None:
    """Sort the subarray arr[low:high+1] using deterministic in-place Quicksort."""
    while low < high:
        # Partition the array around the pivot and obtain the pivot index.
        pivot_index = _partition(arr, low, high)

        # Choose the smaller partition for recursion to keep the stack depth low.
        left_size = pivot_index - low
        right_size = high - pivot_index
        if left_size < right_size:
            _quicksort(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            _quicksort(arr, pivot_index + 1, high)
            high = pivot_index - 1


def _randomized_quicksort(arr: List[int], low: int, high: int) -> None:
    """Sort the subarray arr[low:high+1] using randomized in-place Quicksort."""
    while low < high:
        # Select a random pivot and swap it to the end of the current segment.
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]

        pivot_index = _partition(arr, low, high)

        # Recurse into the smaller partition first to reduce recursion depth.
        left_size = pivot_index - low
        right_size = high - pivot_index
        if left_size < right_size:
            _randomized_quicksort(arr, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            _randomized_quicksort(arr, pivot_index + 1, high)
            high = pivot_index - 1


def _partition(arr: List[int], low: int, high: int) -> int:
    """Partition arr[low:high+1] around the pivot and return its final index."""
    pivot = arr[high]
    i = low - 1

    # Iterate through the current segment and move elements <= pivot to the left.
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot immediately after the elements less than or equal to it.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def is_sorted(arr: List[int]) -> bool:
    """Return True if arr is sorted in non-decreasing order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def time_function(func: Callable[[List[int]], List[int]], arr: List[int], trials: int = 3) -> float:
    """Measure the average runtime of a sorting function over several trials."""
    total = 0.0
    for _ in range(trials):
        start = time.perf_counter()
        result = func(arr)
        end = time.perf_counter()
        if not is_sorted(result):
            raise AssertionError("Sorting failed: output is not sorted")
        total += end - start
    return total / trials


def generate_input(size: int, distribution: str) -> List[int]:
    """Generate a list of integers according to the specified distribution."""
    if distribution == "random":
        # Random values range from 0 to size, inclusive.
        return [random.randint(0, size) for _ in range(size)]
    if distribution == "sorted":
        # Already sorted ascending list.
        return list(range(size))
    if distribution == "reverse-sorted":
        # Sorted descending list to trigger worst-case behavior for deterministic pivot selection.
        return list(range(size, 0, -1))
    raise ValueError(f"Unknown distribution: {distribution}")


def benchmark(sizes: List[int], distributions: List[str], trials: int = 3) -> List[Tuple[str, int, float, float]]:
    """Run benchmark comparisons for deterministic and randomized Quicksort."""
    results = []
    for distribution in distributions:
        for size in sizes:
            arr = generate_input(size, distribution)
            deterministic_time = time_function(deterministic_quicksort, arr, trials)
            randomized_time = time_function(randomized_quicksort, arr, trials)
            results.append((distribution, size, deterministic_time, randomized_time))
    return results


def main() -> None:
    """Execute the empirical benchmark and print the results."""
    print("Quicksort empirical benchmark")
    sizes = [1000, 5000, 10000]
    distributions = ["random", "sorted", "reverse-sorted"]
    results = benchmark(sizes, distributions, trials=3)
    for distribution, size, det_time, rnd_time in results:
        print(f"{distribution:14} | n={size:5} | deterministic={det_time:.6f}s | randomized={rnd_time:.6f}s")


if __name__ == "__main__":
    main()
