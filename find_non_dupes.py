#!/usr/bin/env python

def trampoline(f):
    def wrapped(*args):
        res = f(*args)
        print(res, *args)
        while hasattr(res, '__call__'):
            print("unwrapping...")
            res = res()
        return res

    return wrapped

@trampoline
def find_non_dupes(nums):

    num_dict = {}
    single_nums = set()

    for num in nums:
        if num in num_dict:
            single_nums.remove(num)
        else:
            single_nums.add(num)
            num_dict[num] = 1

    return list(single_nums)


def main():
    """
    Driver code
    :return:
    """
    nums = [1, 2, 4, 3, 5, 4, 1, 2]
    print(find_non_dupes(nums))


if __name__ == "__main__":
    main()
