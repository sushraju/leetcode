#!/usr/bin/env python
import functools


def identity(x):
    return x


def trampoline(f):
    def decorator(*args, **kwargs):
        result = f(*args, **kwargs)
        while callable(result):
            print("unwrapping...")
            result = result()
        return result

    return decorator


@trampoline
def unique_paths(m, n, cont=identity):
    if m == 1 or n == 1:
        return cont(1)

    return lambda: unique_paths(
        m-1, n, lambda x: unique_paths(
            m, n-1, lambda y: cont(x + y)))


if __name__ == "__main__":
    print(unique_paths(7, 7))
