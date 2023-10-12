# Okay this took way too fucking long. There was a weird catch that I was not getting.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        hasAppended = False
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if not hasAppended:
                    res.append(node.val)
                    hasAppended = True
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            hasAppended = False
        return res        