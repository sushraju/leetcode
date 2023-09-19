#!/usr/bin/env python

def stair_climb(n,m=3):
    if n <= 1:
        return n
    res = 0
    i = 1
    print(n, m)
    while i<=m and i<=n:
        res = res + stair_climb(n-i, m)
        i = i + 1
    return res

def main(stairs):
    print ("Number of climbing " + str(stairs) + " stairs = " + str(stair_climb(stairs+1)))

if __name__ == "__main__":
   main(3)
