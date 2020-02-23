#!/usr/bin/env python

class NumStuff(object):
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

   def has_dupe(self):
      hasdupe = False
      sorted_nums = sorted(self.nums)
      print sorted_nums
      for i in range(0,len(sorted_nums)-1):
         if (sorted_nums[i] == sorted_nums[i+1]):
            hasdupe = True
            break

      return hasdupe

   def max(self):
      sorted_nums = sorted(self.nums)
      max_num = sorted_nums[len(sorted_nums)-1]
      max_num_index = self.nums.index(max_num)
      return(max_num, max_num_index)

def main():
   nums = [12,3,4,5,12,6,7,9]
   target = 16
   numstuff = NumStuff(nums)
   print (numstuff.two_sum(target))
   if numstuff.has_dupe():
      print " has dupes"
   else:
      print " has no dupes"

   print (numstuff.max())

if __name__ == "__main__":
   main()
