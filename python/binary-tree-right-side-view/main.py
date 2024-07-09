from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []

        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            last_index = len(queue) - 1
            for x in range(len(queue)):
                node = queue.popleft()

                if x == last_index:
                    ans.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return ans


s = Solution()

root = TreeNode(
    1,
    TreeNode(2),
)

print(s.rightSideView(root))
