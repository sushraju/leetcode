#!/usr/bin/env python

class TwoSum(object):
   def __init__(self, nums):
      self.nums = nums     

   def two_sum(self, target):
      a = 0
      b = 0
      for i in range(0,len(self.nums)-1):
         if (self.nums[i] + self.nums[i+1]) == target:
            a = i
            b = i+1

      return(a,b) 

def main():
   nums = [2,3,4,5,6,7,9]
   target = 26
   a,b = TwoSum(nums).two_sum(target)
   print a,b

if __name__ == "__main__":
   main()
