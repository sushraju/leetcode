#!/usr/bin/env python
import sys


def main(expr):
    s = []
    for i in range(0, len(expr)):
        if expr[i] == '(' or expr[i] == '{' or expr[i] == '[':
            s.append(expr[i])
            continue

        if expr[i] == ')':
            m = s.pop()
            if m == '{' or m == '[':
                print(expr + ' is _not_ Balanced')
                sys.exit(0)

        if expr[i] == '}':
            m = s.pop()
            if m == '(' or m == '[':
                print(expr + ' is _not_ Balanced')
                sys.exit(0)

        if expr[i] == ']':
            m = s.pop()
            if m == '(' or m == '{':
                print(expr + ' is _not_ Balanced')
                sys.exit(0)

    if len(s):
        print(expr + ' is _not_ Balanced')
    else:
        print(expr + ' is Balanced')


if __name__ == "__main__":
    main('([{}])')
