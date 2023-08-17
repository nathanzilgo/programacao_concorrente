
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
            node.next.prev = node

    def remove(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head = new_node

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


dl = DoubleLinkedList()
dl.append(23)
dl.append(32)
dl.append(43)
dl.append(54)
dl.print()
