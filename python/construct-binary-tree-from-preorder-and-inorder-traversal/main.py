from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        node = TreeNode(preorder[0])

        index = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1 : index + 1], inorder[:index])
        node.right = self.buildTree(preorder[index + 1 :], inorder[index + 1 :])

        return node


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]


def print_preorder(node):
    if not node:
        print("nope")
        return

    print(node.val)
    print_preorder(node.left)
    print_preorder(node.right)


s = Solution()

print_preorder(s.buildTree(preorder, inorder))
