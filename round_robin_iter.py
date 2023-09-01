"""
Iterator:
    has_next() - true if there are more elements
    next() - returns the next element & advances

while iter.has_next():
    print(iter.next())

ListIterator([1, 2, 3, 4])

<0 1 2>, <3, 4, 5, 6>, <7, 8>
0 3 7 1 4 8 2 5 6

RoundRobinIterator:
    has_next() - true if there are more elements
    next() - returns the next element from the next iterator in round-robin order & advances


RoundRobinIterator([ListIterator([...]), ListIterator([...])])
"""

class ListIterator(object):
    def __init__(self, our_list=[]):
        self.our_list = our_list
        self.list_len = len(self.our_list)
        self.curr_ind = 0

    def has_next(self):
        if self.curr_ind < self.list_len:
            return True
        else:
            return False

    def next(self):
        if self.curr_ind < self.list_len:
            curr_element = self.our_list[self.curr_ind]
            self.curr_ind += 1
            return curr_element

class RoundRobinIterator(ListIterator):
    def __init__(self, ListIterator=[]):
        self.list_iterators=ListIterator
        self.list_len = len(self.list_iterators)
        self.curr_ind = 0

    def has_next(self):
        if self.curr_ind < self.list_len:
            if self.list_iterators[self.curr_ind].has_next():
                return True
            else:
                self.curr_ind = 0
        else:
            self.curr_ind = 0
        
        while self.curr_ind < self.list_len:
            if self.list_iterators[self.curr_ind].has_next():
                return True
            else:
                self.curr_ind += 1
        return False

    
    def next(self):
        if self.curr_ind < self.list_len:
            curr_element = self.list_iterators[self.curr_ind].next()
            self.curr_ind += 1
            return curr_element

def main():
    list_iter = ListIterator([1,2,3,4,5])
    round_robin_iter = RoundRobinIterator([ListIterator([0,1,2]),ListIterator([3,4,5,6]),ListIterator([8,9,10,12,14,15])])

    print("This is the output of the ListIterator:")
    while list_iter.has_next():
        print(list_iter.next())

    print("\nThis is the output of the Round-Robin ListIterator:")
    while round_robin_iter.has_next():
        print(round_robin_iter.next())


if __name__ == "__main__":
    main()
