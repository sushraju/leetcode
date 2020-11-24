#!/usr/bin/env python

# Solution to https://twitter.com/UntangleIndia/status/13310784837709168640

def find_pouch_size(max_num_coins):
    mod_dict = {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 7,
        9: 8,
        10: 9
    }

    for i in range(1, max_num_coins):
        found = True
        for k, v in mod_dict.items():
            if i % k != v:
                found = False
                break

        if found:
            print(i)


def main():
    find_pouch_size(3500)


if __name__ == "__main__":
    main()
