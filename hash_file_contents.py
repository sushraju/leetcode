#!/usr/bin/env python
import os
import hashlib
import unittest
from collections import defaultdict


# This script builds a dictionary of identical files in a directory (and nested contents)

class FileNameHash(object):

    def __init__(self, path):
        self.path = path
        self.all_files = None
        self.hash_file_names = None
        self.find_files(self.path)
        self.build_file_names_hash()

    # Find the files in a directory.  The worst case complexity is O(N^2), which is not great.
    def find_files(self, path):
        if self.all_files is None:
            self.all_files = []
        dir_list = os.listdir(path)
        for fn in dir_list:
            if os.path.isfile(path + "/" + fn):
                self.all_files.append(path + "/" + fn)
            elif os.path.isdir(path + "/" + fn):
                self.find_files(path + "/" + fn)
            else:
                continue

    def build_file_names_hash(self):
        self.hash_file_names = defaultdict(list)
        for i in range(len(self.all_files)):
            with open(self.all_files[i], "r") as fd:
                file_contents = fd.read()
                fd.close()
                result = str(hashlib.md5(file_contents.encode()).hexdigest())
                self.hash_file_names[result].append(self.all_files[i])

    def identical_files(self):
        print("List of identical files:")
        for k,v in self.hash_file_names.items():
            if len(v) > 1:
                print(v)


class HashFileTest(unittest.TestCase):

    # $ ls -lRt test
    # total 40
    # -rw-r--r--  1 zaphod  staff    9 Mar 24 13:55 l
    # drwxr-xr-x  8 zaphod  staff  256 Mar 24 11:25 test1
    # -rw-r--r--  1 zaphod  staff   21 Mar 23 16:50 c.txt
    # -rw-r--r--  1 zaphod  staff   21 Mar 23 16:50 d.txt
    # -rw-r--r--  1 zaphod  staff   12 Mar 23 16:50 b.txt
    # -rw-r--r--  1 zaphod  staff   12 Mar 23 16:50 a
    #
    # test/test1:
    # total 40
    # drwxr-xr-x  4 zaphod  staff  128 Mar 23 17:39 test2
    # -rw-r--r--  1 zaphod  staff   12 Mar 23 16:50 c
    # -rw-r--r--  1 zaphod  staff   12 Mar 23 16:50 w
    # -rw-r--r--  1 zaphod  staff   12 Mar 23 16:50 x
    # -rw-r--r--  1 zaphod  staff   12 Mar 23 16:50 y
    # -rw-r--r--  1 zaphod  staff   12 Mar 23 16:50 z
    #
    # test/test1/test2:
    # total 16
    # -rw-r--r--  1 zaphod  staff  21 Mar 23 17:39 f
    # -rw-r--r--  1 zaphod  staff  12 Mar 23 17:39 e

    def test_simple_traverse(self):
        fn_hash1 = FileNameHash("test")
        print("\n" + self._testMethodName)
        fn_hash1.identical_files()
        self.assertTrue(len(fn_hash1.hash_file_names), 3)

    def test_second_degree(self):
        fn_hash2 = FileNameHash("test/test1")
        print(self._testMethodName)
        fn_hash2.identical_files()
        self.assertTrue(len(fn_hash2.hash_file_names), 2)


if __name__ == "__main__":
    unittest.main()
