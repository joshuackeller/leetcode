from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def solve(root: Optional[TreeNode], targetSum: int, runningSum: int) -> bool:
            if not root:
                return False

            runningSum += root.val 

            if not root.left and not root.right:
                return runningSum == targetSum

            if solve(root.left, targetSum, runningSum):
                return True
            if solve(root.right, targetSum, runningSum):
                return True

            return False
        
        return solve(root, targetSum, 0)

s = Solution();

root = TreeNode(1, TreeNode(2), TreeNode(3))

print(s.hasPathSum(root, 3));

