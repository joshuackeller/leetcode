class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1 

        node = self.head
        for x in range(index + 1):
            if x == index:
                return node.val
            node = node.next

        return -1

    def addAtHead(self, val: int) -> None:
        self.len += 1
        node = ListNode(val, None, self.head)
        if self.head:
            self.head.prev = node

        self.head = node

        if not self.tail:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        self.len += 1
        if self.tail:
            self.tail.next = ListNode(val, self.tail, None)
            self.tail = self.tail.next
        else:
            self.tail = ListNode(val, None, None)
            self.head = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.len:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return

        if index > self.len:
            return

        node = self.head

        for x in range(index + 1):
            if x == index:
                self.len += 1
                new_node = ListNode(val, node.prev, node)

                node.prev.next = new_node
                node.prev = new_node
                return

            node = node.next

        if not self.tail:
            self.tail = self.head

    def deleteAtIndex(self, index: int) -> None:
        node = self.head

        if index >= self.len or index < 0 or self.len == 0:
            return
        
        if index == self.len - 1 and self.tail:
            self.len -= 1
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else: 
                self.tail = None
                self.head

        for x in range(index + 1):
            if x == index:
                self.len -= 1
                if node.prev and node.next:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                elif node.prev:
                    self.tail = node.prev
                    self.tail.next = None
                    node.prev.next = None
                elif node.next:
                    self.head = node.next
                    self.head.prev = None
                else:
                    self.head = None
                    self.tail = None
                return

            if node.next:
                node = node.next
            else:
                return

    def print(self):
        print("length:", self.len)
        node = self.head
        while node:
            if node.prev:
                p = node.prev.val
            else:
                p = "-"
            if node.next:
                n = node.next.val
            else:
                n = "-"
            print(p, node.val, n)
            node = node.next

    def print_tail(self):
        if self.tail.prev:
            p = self.tail.prev.val
        else:
            p = "-"
        if self.tail.next:
            n = self.tail.next.val
        else:
            n = "-"
        print("tail", p, self.tail.val, n)


ll = MyLinkedList()

ll.addAtHead(2)
ll.deleteAtIndex(1)
ll.addAtHead(2)
ll.addAtHead(7)
ll.addAtHead(3)
ll.addAtHead(2)
ll.addAtHead(5)
ll.addAtTail(5)
ll.get(5)
ll.deleteAtIndex(6)
ll.deleteAtIndex(4)


ll.print()
