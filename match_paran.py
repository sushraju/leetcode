#!/usr/bin/env python
import sys
import unittest


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


class TestCases(unittest.TestCase):

    def test_match(self):
        self.assertTrue(isValid('([{}])'))
        self.assertFalse(isValid('({)}'))


if __name__ == "__main__":
    unittest.main()
