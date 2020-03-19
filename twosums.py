#!/usr/bin/env python


class TwoSum(object):
    def __init__(self, nums):
        self.nums = nums

    def two_sum(self, target):
        s = set()
        for i in self.nums:
            print(s)
            if (target - i) in s:
                return True

            s.add(i)

        return False


def main():
    nums = [2, 3, 4, 5, 6, 7, 9]
    target = 11

    if TwoSum(nums).two_sum(target):
        print(str(target) + ' present in ' + str(nums) + ' as a sum.')
    else:
        print(str(target) + ' not present in ' + str(nums) + ' as a sum.')

if __name__ == "__main__":
    main()
