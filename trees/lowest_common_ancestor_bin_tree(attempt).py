# I could not get this to be right. I am pretty mad at myself cause the solution was
# super easy, but I did't realize that the Tree was actually kinda sorted
# cause it was a Binary SEARCH Tree instead of just a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    p_bool = False
    q_bool = False
    ancestor = False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return self.ancestor

        # Run through current node
        if self.runThroughTree(root, p, q):
            self.ancestor = root
        
        self.lowestCommonAncestor(root.left, p, q)
        self.lowestCommonAncestor(root.right, p, q)
        print(self.ancestor)
        return self.ancestor
        
    # Run through tree and see if p and q nodes are in it
    # Return true if they both are found
    def runThroughTree(self, node, p, q):
        if not node:
            return False
        if node.val == p:
            self.p_bool = True
        if node.val == q:
            self.q_bool = True
        if self.p_bool and self.q_bool:
            self.p_bool, self.q_bool = False, False
            return True
        
        return (self.runThroughTree(node.left, p, q) or 
                self.runThroughTree(node.right, p, q))
        