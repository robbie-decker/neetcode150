# This solution was garbage


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return 1 + self.diameterOfBinaryTree(root.right)
        
        if not root.right:
            return 1 + self.diameterOfBinaryTree(root.left)
        

        return self.diameterOfBinaryTree(root.left) + self.diameterOfBinaryTree(root.right)