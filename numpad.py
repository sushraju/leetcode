#!/usr/bin/env python

import sys

numpad = {
   2:'abc',
   3:'def',
   4:'ghi',
   5:'jkl',
   6:'mno',
   7:'pqrs',
   8:'tuv',
   9:'wxyz' 
}

def combonumpad(a, b):
   if numpad[a]:
      if  numpad[b]: 
         for i in range(0,len(numpad[a])):
            for j in range(0,len(numpad[b])):
                combo = numpad[a][i] + numpad[b][j]
                print combo
 
def main():
   combonumpad(2,9)

if __name__ == "__main__":
   main()
