from typing import Optional


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        if node.prev and node.next:
            node.prev.next, node.next.prev = node.next, node.prev

    def add(self, node: Node):
        node.prev, node.next = self.right.prev, self.right
        if self.right.prev:
            self.right.prev.next, self.right.prev = node, node

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.add(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.map:
            self.remove(self.map[key])
        self.add(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            if self.left.next:
                del self.map[self.left.next.key]
                self.remove(self.left.next)


#
#         self.print()
#
#     def print(self):
#         map_vals = []
#         list_vals = []
#         for key in self.map:
#             map_vals.append(self.map[key].val)
#
#         node = self.left
#         while node:
#             list_vals.append(node.val)
#             node = node.next
#
#         print("map", map_vals)
#         print("list", list_vals)
#         print()
#
#
# c = LRUCache(2)
#
# c.put(1, 0)
# c.put(2, 2)
# c.get(1)
# c.put(3, 3)
# c.get(2)
# c.put(4, 4)
# c.get(1)
# c.get(3)
# c.get(4)
