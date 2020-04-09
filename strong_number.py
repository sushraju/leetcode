#!/usr/bin/env python

def main():
    num = 144
    temp = num
    sum = 0
    while (num > 0):
        n = num % 10
        f = fact(n)
        sum = sum + f
        num = num // 10

    print(temp, sum)


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i

    return f


if __name__ == "__main__":
    main()
