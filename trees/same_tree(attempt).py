# This was an iterative way to solve the problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    tree = []
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack = [p]
        q_stack = [q]

        while p_stack or q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            print(p_node, "        ", q_node)
            if not p_node and q_node:
                return False
            if not q_node and p_node:
                return False
            if p_node and q_node:
                if p_node.val != q_node.val:
                    return False
                p_stack.append(p_node.left)
                p_stack.append(p_node.right)
                
                q_stack.append(q_node.left)
                q_stack.append(q_node.right)
        return True
