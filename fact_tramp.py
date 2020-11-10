#!/usr/bin/env python
import functools

def trampoline_tailrec(f):

    @functools.wraps(f)
    def decorator(*args, **kwargs):
        v = f(*args, **kwargs)
        while callable(v):
            v = v()
        return v

    return decorator

def fact(n):

    def helper(k, a):
        if k == 0:
            return a
        else:
            a2 = k * a
            return lambda: helper(k - 1, a2)

    assert n >= 0
    decorated_helper = trampoline_tailrec(helper)
    return decorated_helper(n, 1)

def main():
    for n in range(100):
        print(n, fact(n))

if __name__ == "__main__":
    main()