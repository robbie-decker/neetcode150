# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            # Both greater so go right
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            
            # Both less so go left
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left

            # p and q in different branches or cur node = p or = q
            # so return current node
            else:
                return cur