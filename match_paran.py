#!/usr/bin/env python
import sys


def isValid(expr: str) -> bool:
    pairs = {'(': ')', '[': ']', '{': '}'}
    s = []

    for char in expr:
        if char in pairs.keys():
            s.append(char)
        elif len(s) > 0 and pairs.get(s[-1]) == char:
            s.pop()
        else:
            return False

    return len(s) == 0


def main(expr):
    if isValid(expr):
        print("This is a balanced expression")
    else:
        print("This is not a balanced expression")


if __name__ == "__main__":
    main('([{}])')
