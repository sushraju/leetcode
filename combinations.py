"""
Find unique combinations from a given list that add to a desired target sum.
"""
#!/usr/bin/env python

from itertools import combinations


def unique_combinations(nums, combo_len=3) -> set:
    """
    Finds unique combinations of length (combo_len) in a list (nums)
    :param nums: list
    :param combo_len: length of combination
    :return: set
    """
    all_combinations = combinations(nums, combo_len)
    unique_set = set()

    for combo in all_combinations:
        unique_set.add(tuple(sorted(combo)))

    return unique_set


def target_sum_combinations(unique_set, target_sum):
    """

    :param unique_set: A set of unique combinations (tuples)
    :param target_sum: Target sum of the tuples in the unique_set
    :return: none
    """
    print("\nAll unique combinations of length %d with a target sum of %d" % (len(min(unique_set)), target_sum))
    for combo in unique_set:
        if sum(combo) == target_sum:
            print(combo, sum(combo))


def main():
    """
    Driver code
    :return:
    """
    unique_set = unique_combinations([-1, 0, 1, 2, -1, 2], 3)
    target_sum_combinations(unique_set, 2)

    # output
    # $ python combinations.py
    #
    # All unique combinations of length 3 with a target sum of 2
    # (-1, 1, 2) 2


if __name__ == "__main__":
    main()
