#!/usr/bin/env python


def first_duplicate(my_list):
    for index in my_list:
        if my_list[abs(index) - 1] < 0:
            return abs(index)
        else:
            my_list[abs(index) - 1] = my_list[abs(index) - 1] * -1
    return -1


def main():
    """
    Driver code
    :return:
    """
    nums = [1, 2, 3, 2, 3, 1]
    print(first_duplicate(nums))


if __name__ == "__main__":
    main()
