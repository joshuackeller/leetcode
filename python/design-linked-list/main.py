class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.linked_list = None
        self.tail = None
        self.len = 0

    def print(self):
        print("length:", self.len)
        node = self.linked_list
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

    def get(self, index: int) -> int:
        if index >= self.len:
            return

        node = self.linked_list
        for x in range(index):
            if x == index:
                return node
            node = node.next

        return -1

    def addAtHead(self, val: int) -> None:
        self.len += 1
        node = ListNode(val, None, self.linked_list)
        if self.linked_list:
            self.linked_list.prev = node

        self.linked_list = node

        if not self.tail:
            self.tail = self.linked_list

    def addAtTail(self, val: int) -> None:
        self.len += 1
        if self.tail:
            self.tail.next = ListNode(val, self.tail, None)
            self.tail = self.tail.next
        else:
            self.tail = ListNode(val, None, None)
            self.linked_list = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.len:
            self.addAtTail(val)
            return
        if index == 0:
            self.addAtHead(val)
            return

        if index > self.len:
            return

        node = self.linked_list

        for x in range(index):
            if x == index - 1:
                self.len += 1
                new_node = ListNode(val, node.prev, node.next)
                if node.prev:
                    node.prev.next = new_node
                if node.next:
                    node.next.prev = new_node
                return

            node = node.next

        if not self.tail:
            self.tail = self.linked_list

    def deleteAtIndex(self, index: int) -> None:
        node = self.linked_list

        if index >= self.len or self.len == 0:
            return

        if index == self.len - 1 and self.tail:
            self.len -= 1
            self.tail = self.tail.prev
            self.tail.next = None
            return

        for x in range(index):
            if x == index:
                self.len -= 1
                if node.prev and node.next:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                elif node.prev:
                    node.prev.next = None
                elif node.next:
                    node.next.prev = None
                else:
                    self.linked_list = None
                return

            node = node.next


ll = MyLinkedList()

ll.addAtTail(3)
ll.addAtHead(1)
ll.addAtIndex(0, 0)
ll.addAtIndex(3, 4)
ll.print()
ll.addAtIndex(2, 2)

ll.print()
