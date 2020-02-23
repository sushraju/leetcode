#!/usr/bin/env

def main(str):
   found_index=-1
   look_for='s'
   found_flag = False
   found_count = 0
   for i in range(0,len(str)):
      if str.count(str[i]) == 1:
         if found_index == -1 and found_flag == False:
            found_index = i
            found_flag = True
            print found_index
         found_count = found_count + 1

   if found_flag == True:
      if found_count == len(str) and found_index > 0:
         found_index = -1
   else:
      found_index = -1

   print found_index, found_count

if __name__ == "__main__":
   main("rqmteywu")
