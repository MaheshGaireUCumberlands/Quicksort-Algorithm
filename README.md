# Assignment 5: Quicksort Algorithm

This repository contains Python implementations and analysis for both deterministic and randomized versions of Quicksort.

## Files

- `quicksort.py`: deterministic and randomized Quicksort implementations, a benchmark helper, and validation utilities.
- `report.md`: analysis covering time complexity, space complexity, and empirical observations.

## Running the code

1. Ensure Python 3.8+ is installed.
2. Run the benchmark:

```bash
python3 quicksort.py
```

## Summary

- `deterministic_quicksort` uses the last element of the current subarray as the pivot.
- `randomized_quicksort` selects a random pivot from the subarray to reduce the chance of worst-case behavior.
- The benchmark compares both implementations on random, sorted, and reverse-sorted inputs.

## Testing

Run the unit tests with:

```bash
python3 -m unittest test_quicksort.py
```

The current suite includes edge cases, sorted and reverse-sorted inputs, random input, and input-preservation checks. All tests pass.
