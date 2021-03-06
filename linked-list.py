"""Problem statement:
   Date: 27/10/20
   Author: Bhargav Andhe"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Empty list')
        else:
            i = self.head
            s = ''
            while i:
                s += str(i.data) + '->'
                i = i.next

            print(s)


if __name__ == '__main__':
    l = LinkedList()
    l.insert(98)
    l.insert(5)
    l.print()
