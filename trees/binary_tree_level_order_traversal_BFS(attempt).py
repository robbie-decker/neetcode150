# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # I think this is just a breadth first search
        # BFS iteratively uses a queue
        if not root:
            return None

        vals = []
        myQueue = [(root, 0)]

        while myQueue:
            elem = myQueue.pop(0)
            node = elem[0]
            level = elem[1]
            # Need to group values with their level
            # Check if the level/ index already exists in list
            # Exists
            if level <= len(vals)-1:
                vals[level].append(node.val)

            else:
                vals.append([node.val])

            if node.left:
                myQueue.append((node.left, level + 1))

            if node.right:
                myQueue.append((node.right, level + 1))

        return vals