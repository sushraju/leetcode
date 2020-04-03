#!/usr/bin/env python

class NumOps(object):
    def __init__(self, nums):
        self.nums = nums

    def two_sum(self, target):
        a = 0
        b = 0
        for i in range(0, len(self.nums) - 1):
            if (self.nums[i] + self.nums[i + 1]) == target:
                a = i
                b = i + 1

        return a, b

    def has_dupe(self):
        has_dupe = False
        sorted_nums = sorted(self.nums)
        print(sorted_nums)
        for i in range(0, len(sorted_nums) - 1):
            if (sorted_nums[i] == sorted_nums[i + 1]):
                hasdupe = True
                break

        return has_dupe


def main():
    nums = [12, 3, 4, 5, 12, 6, 7, 9]
    target = 16
    num_ops = NumOps(nums)
    a, b = num_ops.two_sum(target)
    print(a, b)
    if num_ops.has_dupe():
        print(" has dupes")
    else:
        print(" has no dupes")


if __name__ == "__main__":
    main()
