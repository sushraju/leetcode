
"""
linked list2
"""

class Node(object):
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class LinkedList(object):
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        if value is not None:
            self.add(value)

    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next_node = Node(value, None, self.tail)
            self.tail = self.tail.next_node
        
        return self.tail

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

    def remove(self, value):
        current = self.head
        while current:
            if current.value == value:
                current.prev_node.next_node = current.next_node
            
            current = current.next_node
        
        #self.iterate_list()

    def getLast(self):
        current = self.tail
        return(current.value)

    def getRandom(self):
        # get length and random(len)
        current = self.head
        while current:
            print(current.value)
            current = current.next_node

    def getMax(self):
        pass
    
def main():
  linked_list = LinkedList()
  linked_list.add(2)
  linked_list.add(4)
  linked_list.add(1)    
  for l in linked_list:
    print(l.value)
  linked_list.remove(1)
  for l in linked_list:
    print(l.value)

if __name__ == "__main__":
  main()