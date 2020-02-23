#!/usr/bin/env python

def stair_climb(n,m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i<=m and i<=n:
        res = res + count_ways(n-i, m)
        i = i + 1
    return res

def main(stairs,jump=3):
    print ("Number of climbing " + str(n) + " stairs = " + str(count_ways(stairs+1, jump)))

if __name__ == "__main__":
   main(4,3)
