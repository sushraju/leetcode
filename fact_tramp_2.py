#!/usr/bin/env python

def trampoline(f):
    def wrapped(*args):
        res = f(*args)
        while hasattr(res, '__call__'):
            res = res()

        return res

    return wrapped


@trampoline
def fact(n, a):
    if n == 0:
        return a
    else:
        a2 = n * a
        return lambda: fact(n - 1, a2)


def main():
    for n in range(101):
        print(n, fact(n, 1))


if __name__ == "__main__":
    main()
