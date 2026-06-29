# Quicksort Implementation and Analysis

## 1. Implementation

This assignment includes two Quicksort implementations in `quicksort.py`:

- `deterministic_quicksort(arr)`: classic Quicksort using the last element as the pivot.
- `randomized_quicksort(arr)`: randomized Quicksort that picks the pivot uniformly at random from the current subarray.

Both implementations use a helper `_partition(arr, low, high)` that moves elements less than or equal to the pivot to the left side and returns the pivot's final index.

## 2. Time Complexity Analysis

### Best case

- Best-case behavior occurs when the pivot splits the array into two balanced halves at every recursion.
- The recurrence is:
  - `T(n) = 2T(n/2) + O(n)`
- Solving gives `T(n) = O(n log n)`.

### Average case

- On average, a pivot divides the array into reasonably balanced partitions.
- The average recurrence is similar to the balanced case, yielding `O(n log n)`.
- Intuitively, each element is compared a constant number of times per partition step, and there are about `log n` recursive levels.

### Worst case

- The worst case occurs when the pivot is always the smallest or largest element and partitions are highly unbalanced.
- The recurrence becomes:
  - `T(n) = T(n-1) + O(n)`
- Solving this recurrence gives `T(n) = O(n^2)`.
- This can happen for deterministic Quicksort on already sorted or reverse-sorted arrays when using the last element as pivot.

## 3. Space Complexity

- Quicksort is an in-place algorithm for the partitioning step, so the extra space beyond the input array is `O(1)`.
- However, recursion creates stack overhead.
- In the best and average cases, recursion depth is `O(log n)`, so space complexity is `O(log n)`.
- In the worst case, recursion depth is `O(n)`, so the space cost may rise to `O(n)`.

## 4. Randomized Quicksort

### Implementation details

- `randomized_quicksort` chooses a random index between `low` and `high` and swaps it with the last element before partitioning.
- This random pivot selection avoids consistently poor pivot choices for specific input patterns.

### Impact of randomization

- Randomization does not change the average time complexity; it remains `O(n log n)`.
- It reduces the probability of hitting the worst-case scenario because the pivot choice is not tied to the input order.
- For an adversarial input, randomized Quicksort is much less likely to recur in the worst-case pattern.

## 5. Empirical Analysis

The benchmark in `quicksort.py` compares both algorithms on three input distributions:

- random input
- sorted input
- reverse-sorted input

### Measured results

The following timings were measured on the assignment machine using Python 3:

| Distribution    | Size | Deterministic Quicksort | Randomized Quicksort |
|-----------------|------|-------------------------|----------------------|
| random          | 1000 | 0.001006 s              | 0.001544 s           |
| random          | 5000 | 0.006465 s              | 0.008248 s           |
| sorted          | 1000 | 0.040066 s              | 0.001394 s           |
| sorted          | 5000 | 1.048916 s              | 0.007747 s           |
| reverse-sorted  | 1000 | 0.028159 s              | 0.001370 s           |
| reverse-sorted  | 5000 | 0.716179 s              | 0.008104 s           |

### Expected results

- Deterministic Quicksort should perform well on random input.
- Deterministic Quicksort may degrade on sorted or reverse-sorted data because the chosen pivot is the last element.
- Randomized Quicksort should show more stable performance across distributions because the pivot is selected randomly.

### Observed behavior

The measured data confirms the theory:

- On random input, both versions are fast, and deterministic Quicksort is slightly faster in this sample.
- On sorted input, deterministic Quicksort becomes very slow, taking over 1 second for 5,000 items, while randomized Quicksort stays fast at under 0.008 seconds.
- On reverse-sorted input, deterministic Quicksort also slows significantly, while randomized Quicksort remains stable.

These real measurements illustrate how random pivot selection dramatically reduces the likelihood of worst-case behavior for Quicksort.

## 6. Conclusions

- Quicksort is an efficient comparison-based sorting algorithm with average-case time complexity `O(n log n)`.
- The deterministic pivot strategy can expose the algorithm to `O(n^2)` behavior on specially ordered inputs.
- Randomized Quicksort is a robust alternative that reduces the likelihood of worst-case performance while preserving the same average-case complexity.

## 7. How to use

1. Run the benchmark with `python3 quicksort.py`.
2. Add more sizes or distributions in `quicksort.py` if deeper analysis is desired.
3. Verify correctness with `is_sorted` in the provided helper.
