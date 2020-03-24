#!/usr/bin/env python
import os
import hashlib
import unittest
from collections import defaultdict


# This script builds a dictionary of identical files in a directory (and nested contents)

# Find the files in a directory.  The worst case complexity is O(n2), which, is not great.
def find_files(path, all_files=None):
    if all_files is None:
        all_files = []
    dir_list = os.listdir(path)
    for fn in dir_list:
        if os.path.isfile(path + "/" + fn):
            all_files.append(path + "/" + fn)
        elif os.path.isdir(path + "/" + fn):
            find_files(path + "/" + fn, all_files)
        else:
            continue

    return all_files


def build_hash(all_files):
    hash_file_names = defaultdict(list)
    for i in range(len(all_files)):
        with open(all_files[i], "r") as fd:
            file_contents = fd.read()
            fd.close()
            result = str(hashlib.md5(file_contents.encode()).hexdigest())
            hash_file_names[result].append(all_files[i])

    return hash_file_names


def main(path):
    all_files = find_files(path)
    hash_file_names = build_hash(all_files)
    for k, v in hash_file_names.items():
        print(v)


class HashFileTest(unittest.TestCase):

    def test_simple_traverse(self):
        main("test")

    def test_second_traverse(self):
        main("test/test1")


if __name__ == "__main__":
    unittest.main()
