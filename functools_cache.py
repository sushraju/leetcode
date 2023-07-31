import functools

@functools.cache
def factorial(n):
    return n * factorial(n-1) if n else 1

def main():
    for n in range(50):
        print(n, factorial(n))

if __name__ == "__main__":
    main()