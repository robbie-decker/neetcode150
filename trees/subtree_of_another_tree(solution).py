# This is basically what I wrote B)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # will always have a subtree if t (subroot) is null
        if not t: return True 
        # will always not have a subtree if s (root) is null
        if not s: return False
        if self.sameTree(s,t):
            return True

        # Not the same tree
        return (self.isSubtree(s.left, t) or
        self.isSubtree(s.right,t))

    def sameTree(self, s, t):
        if not s and not t:
            return True

        # Compare the trees cause values match
        if s and t and s.val == t.val:
           return (self.sameTree(s.left, t.left) and
                   self.sameTree(s.right, t.right))

        # One tree is empty and one is not empty
        return False