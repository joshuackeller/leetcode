# LINKED LIST - faster because it doesn't require rehashing when removing from a group of items with the same index (like open addressing does)
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 0
        self.map = [None, None]

    def hash(self, key: int) -> int:
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)

        if self.map[index]:
            node = self.map[index]
            while True:
                if node.key == key:
                    node.val = value
                    return
                if node.next is None:
                    node.next = Node(key, value)
                    return
                node = node.next

        self.map[index] = Node(key, value)
        self.size += 1
        if self.size * 2 >= len(self.map):
            self.rehash()

    def get(self, key: int) -> int:
        index = self.hash(key)

        if self.map[index]:
            node = self.map[index]
            while node:
                if node.key == key:
                    return node.val
                node = node.next

        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)

        if self.map[index]:
            prev, node = None, self.map[index]
            while node:
                if node.key == key:
                    if not prev:
                        if node.next:
                            self.map[index] = node.next
                        else:
                            self.map[index] = None
                            self.size -= 1
                    else:
                        prev.next = node.next
                    return
                else:
                    prev, node = node, node.next

    def rehash(self) -> None:
        new_map = [None for _ in range(len(self.map) * 2)]
        old_values = self.map

        self.map = new_map
        self.size = 0

        for val in old_values:
            if val is not None:
                node = val
                while node:
                    self.put(node.key, node.val)
                    node = node.next

    def print(self):
        vals = []
        for val in self.map:
            new_vals = []
            if val is not None:
                node = val
                while node:
                    new_vals.append((node.key, node.val))
                    node = node.next
            vals.append(new_vals)
        print(vals)


map = MyHashMap()

map.put(1, 2)
map.put(2, 3)
map.put(9, 4)
map.put(17, 5)
map.put(25, 6)
map.print()
print(map.get(10))

# OPEN ADDRESSING
# class MyHashMap:
#
#     def __init__(self):
#         self.len = 0
#         self.map = [None, None]
#
#     def hash(self, key: int) -> int:
#         return key % len(self.map)
#
#     def put(self, key: int, value: int) -> None:
#         index = self.hash(key)
#
#         while True:
#             if self.map[index] is None:
#                 self.map[index] = (key, value)
#                 self.len += 1
#                 if self.len * 2 >= len(self.map):
#                     self.rehash(True)
#                 return
#             elif self.map[index][0] != key:
#                 index = self.hash(index + 1)
#             elif self.map[index][0] == key:
#                 self.map[index] = (key, value)
#                 return
#
#     def get(self, key: int) -> int:
#         index = self.hash(key)
#
#         while self.map[index] is not None:
#             if self.map[index][0] == key:
#                 return self.map[index][1]
#             index = self.hash(index + 1)
#
#         return -1
#
#     def remove(self, key: int) -> None:
#         index = self.hash(key)
#         count = 0
#
#         while self.map[index] is not None:
#             count += 1
#             if self.map[index][0] == key:
#                 self.map[index] = None
#                 self.len -= 1
#                 self.rehash(False)
#                 return
#             index = self.hash(index + 1)
#
#
#     def rehash(self, resize: bool) -> None:
#         if resize:
#             new_map = [None for _ in range(len(self.map) * 2)]
#         else:
#             new_map = [None for _ in range(len(self.map))]
#         old_values = self.map
#
#         self.map = new_map
#         self.len = 0
#
#         for val in old_values:
#             if val is not None:
#                 self.put(val[0], val[1])
