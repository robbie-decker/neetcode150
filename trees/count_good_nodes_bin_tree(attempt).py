# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + self.checkNodes(root.left, root.val) + self.checkNodes(root.right, root.val)

    def checkNodes(self, node, max):
        if not node:
            return 0
        addition = 0

        # If current val > max, make sure to add 1 and overwrite max
        if node.val >= max:
            addition = 1
            max = node.val
        # Recursive call
        return addition + (self.checkNodes(node.left, max)
                    + self.checkNodes(node.right, max))

