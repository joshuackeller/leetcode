from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        node_map = {}
        queue = deque()

        queue.append(node)
        root = Node(node.val)
        node_map[node.val] = root

        while len(queue) > 0:
            for _ in range(len(queue)):
                og_node = queue.popleft()
                new_node = node_map[og_node.val]

                for n in og_node.neighbors:
                    if n.val not in node_map:
                        queue.append(n)
                        new = Node(n.val)
                        node_map[n.val] = new

                    new_node.neighbors.append(node_map[n.val])

        return root


s = Solution()

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

one.neighbors.append(two)
one.neighbors.append(four)
two.neighbors.append(one)
two.neighbors.append(three)
three.neighbors.append(two)
three.neighbors.append(four)
four.neighbors.append(one)
four.neighbors.append(three)

node = s.cloneGraph(one)
queue = deque()
visited = set()
queue.append(node)
visited.add(node.val)

while len(queue) > 0:
    for _ in range(len(queue)):
        cur = queue.popleft()
        neighbors = []
        for n in cur.neighbors:
            neighbors.append(n.val)
            if n.val not in visited:
                queue.append(n)
                visited.add(n.val)

        print(cur.val, neighbors)
