import unittest


class Node(object):

    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList(object):

    def __init__(self, value=None):
        self.head = None
        self.tail = None
        if value is not None:
            self.add(value)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node

    def __len__(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next_node
        return length

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node
        return self.tail

    def add_to_beginning(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head


class TestCases(unittest.TestCase):

    def test_add(self):
        ll = LinkedList()
        ll.add(2)
        ll.add(3)
        self.assertFalse(ll is None)
        self.assertTrue(len(ll) == 2, "Length was checked")
        self.assertEquals(len(ll), 2)

    def test_add_to_beginning(self):
        ll = LinkedList()
        ll.add(2)
        ll.add(3)
        ll.add_to_beginning(1)
        self.assertFalse(ll is None)
        self.assertEquals(len(ll), 3)


if __name__ == "__main__":
    unittest.main()
