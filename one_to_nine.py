#!/usr/bin/env python
from random import randint


# A brute force solution to https://twitter.com/UntangleIndia/status/1331803009500676096

def solve_puzzle():
    not_found = True;
    while not_found:

        l = list()
        while len(l) < 9:
            n = randint(1, 9)
            if n not in l:
                l.append(n)

        a_b = l[0] * 10 + l[1]
        c = l[2]
        d_e = l[3] * 10 + l[4]
        f_g = l[5] * 10 + l[6]
        h_i = l[7] * 10 + l[8]

        if ((a_b * c) == d_e) and ((f_g - d_e) == h_i):
            print(str(a_b) + " " + str(c) + " " + str(d_e) + " " + str(f_g) + " " + str(h_i))
            not_found = False


if __name__ == "__main__":
    solve_puzzle()
