from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return self.solve(root, "") 
    
    def solve(self, root: Optional[TreeNode], cur) -> str:
        if not root.left and not root.right:
            return chr(ord("a") + root.val) + cur
        
        cur = chr(ord("a") + root.val) + cur

        if root.left and root.right:
            return min(self.solve(root.left, cur), self.solve(root.right, cur))

        if root.left:
            return self.solve(root.left, cur)
        if root.right:
            return self.solve(root.right, cur)


# [25,1,null,0,0,1,null,null,null,0]
root = TreeNode(25,
             TreeNode(1, 
                      TreeNode(0,
                               TreeNode(1,
                                        TreeNode(0)
                                 )
                         ),
                      TreeNode(0)
             ),
         )


# root = TreeNode(25,
#               TreeNode(1, TreeNode(1), TreeNode(3)),
#               TreeNode(3, TreeNode(0), TreeNode(2))
#           )

solution = Solution()
answer = solution.smallestFromLeaf(root)
print(answer)
