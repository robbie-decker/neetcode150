# Super happy with this attempt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
    
        # Go until node of root matches first val of subroot
        if not root:
            return False
        if root.val == subroot.val:
            if (self.checkNodes(root.left, subroot.left) and
             self.checkNodes(root.right, subroot.right)):
                return True
        return (self.isSubtree(root.left, subroot) or
         self.isSubtree(root.right, subroot))
        


    def checkNodes(self, node1, node2):
        if not node1 and not node2:
            return True
        if (not node1 and node2) or (node1 and not node2):
            return False
        elif node1.val == node2.val:
            return (self.checkNodes(node1.left, node2.left) and
             self.checkNodes(node1.right, node2.right))