#!/usr/bin/env python

def main(str):

   left_ctr=0
   right_ctr=0
   print('Original string: ' + str)

   for i in range(0,len(str)):
      if str[i] == '<':
         left_ctr = left_ctr + 1
      elif str[i] == '>':
         right_ctr = right_ctr + 1    

   for j in range(0,left_ctr):
      str = str + '>'

   for k in range(0,right_ctr):
      str = '<' + str

   print('Modified string: ' + str)

if __name__ == "__main__":
   main("><<><")
   #main("><")
   #"<><<><>>"
   #"<<>>>>>"
