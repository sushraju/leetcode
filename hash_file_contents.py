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


class HashFileTest(unittest.TestCase):

    def test_simple_traverse(self):
        fn_hash = FileNameHash("test")
        print("\n" + self._testMethodName)
        for k,v in fn_hash.hash_file_names.items():
            print(k + ':' + str(v))
        self.assertTrue(len(fn_hash.hash_file_names), 2)

    def test_second_degree(self):
        fn_hash = FileNameHash("test/test1")
        print(self._testMethodName)
        for k,v in fn_hash.hash_file_names.items():
            print(k + ':' + str(v))
        self.assertTrue(len(fn_hash.hash_file_names), 2)


if __name__ == "__main__":
    unittest.main()
