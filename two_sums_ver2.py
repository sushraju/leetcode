#!/usr/bin/env python

"""
Two sums - find pairs in a list that add up to a target sum
"""


class TwoSum():
    """
    Two sums - find pairs in a list that add up to a target sum
    """

    def __init__(self, nums):
        self.nums = nums

    def two_sum(self, target):
        """
        This uses a dictionary for a lookup and uses a set to avoid duplication of pairs.
        :param target: target sum
        :return: a set of pairs
        """
        lookup_d = {}
        pairs = set()
        for i in self.nums:

            if str(target - i) in lookup_d:
                pairs.add((i, (target - i)))

            lookup_d[str(i)] = i

        return pairs


def main():
    """
    Driver code
    :return:
    """
    nums = [7, 3, 4, 5, 2, 2, 7, 9, 9]
    target = 11

    print(TwoSum(nums).two_sum(target))


if __name__ == "__main__":
    main()
