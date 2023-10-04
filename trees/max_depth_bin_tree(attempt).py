# Kinda wonky but it is recursive and cool :)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.max
        self.reachEnd(root.left, 1)
        self.reachEnd(root.right,1)
        return self.max

    def reachEnd(self, branch, count):
        if not branch:
            self.max = max(self.max, count)
            return
        
        count += 1
        self.reachEnd(branch.left, count)
        self.reachEnd(branch.right, count)        