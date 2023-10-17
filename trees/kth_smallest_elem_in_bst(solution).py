# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 
        stack = []
        curr = root
        # Going as far left as we can and then popping right when we need to
        while curr or stack:
            # Keep going left
            while curr:
                stack.append(curr)
                curr = curr.left
            # get most recently added elem
            curr = stack.pop()
            n += 1
            # when n == k we found our value
            if n == k:
                print(curr)
                return curr.val
            curr = curr.right
