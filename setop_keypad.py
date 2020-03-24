#!/usr/bin/env python
import string


class KeyPad(object):

    def __init__(self, r=5, c=5):
        self.rows = r
        self.cols = c
        a = list(string.ascii_uppercase)[::-1]
        self.keypad = [[a.pop() for i in range(self.cols)] for j in range(self.rows)]


def main():
    k = KeyPad(5, 5)
    for r in range(k.rows):
        print(k.keypad[r])


if __name__ == "__main__":
    main()
