# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Has no branches
        if not root.left and not root.right:
            return True
            
        # Current node has branches
        currentVal = root.val
        if root.left and root.right:
            if root.left.val < currentVal and root.right.val > currentVal:
                return self.isValidBST(root.left) and self.isValidBST(root.right)

            else:
                return False

        elif root.left:
            if root.left.val < currentVal:
                return self.isValidBST(root.left)
            else:
                return False

        elif root.right:
            if root.right.val > currentVal:
                return self.isValidBST(root.right)
            else:
                return False




# This is another attempt I did and I could probably keep trying, but I am tired and want to go to bed