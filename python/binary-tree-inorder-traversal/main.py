from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def solve(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return

            solve(root.left)
            ans.append(root.val)
            solve(root.right)

        solve(root)
        return ans


s = Solution()

root = TreeNode(5, TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(4)))

print(s.inorderTraversal(root))
