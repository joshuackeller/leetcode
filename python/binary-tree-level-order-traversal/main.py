from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        queue = deque()

        queue.append(root)

        while len(queue) != 0:
            new_arr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                new_arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(new_arr)

        return ans


s = Solution()

# root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3, TreeNode(6)))

print(s.levelOrder(None))
