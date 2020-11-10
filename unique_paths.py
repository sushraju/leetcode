#!/usr/bin/env python
import functools

def identity(x):
    return x

def trampoline(f):

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        res = f(*args, **kwargs)
        while callable(res):
            #print("unwrapping...")
            res = res()
        return res

    return wrapped


class Solution(object):
    def uniquePaths(self, m, n):
        def helper(a, b, cont=identity):
            """
            :type a: int
            :type b: int
            :rtype: int
            """
            #print("a={},b={}".format(a, b))
            if a == 1 or b == 1:
                return cont(1)
            else:
                return lambda: helper(a - 1, b, lambda x: helper(a, b - 1, lambda y: cont(x + y)))

        decorated_helper = trampoline(helper)
        return decorated_helper(m, n, 1)


if __name__ == "__main__":
    Solution().uniquePaths(5, 5)