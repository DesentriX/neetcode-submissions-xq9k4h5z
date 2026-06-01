# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, l , r):
            if not node:
                return True

            if not (l < node.val < r):
                return False

            return traverse(node.left,l, node.val) and traverse(node.right, node.val, r)
        return traverse(root, float("-inf"), float("inf"))

            




        