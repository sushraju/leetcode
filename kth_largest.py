#!/usr/bin/env python

def main():
    numbers = [-9,-6,3,-15,-10,9,-7,15,1,6,0,-9,-6,12,-3,5,-1,-9,-13,-14,8,2,-7,-7,0,0,0,8,15,6,-7]
    nums = sorted(numbers)
    k = 3
    max = None
    max_count=0
    i = len(nums) - 1
    while i >= 0:
        max_count = max_count+1
        if max_count == k:
            max = nums[i]
        i = i - 1

    print max,nums

if __name__ == "__main__":
    main()