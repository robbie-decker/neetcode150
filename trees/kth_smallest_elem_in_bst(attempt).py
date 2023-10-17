# Attempt that couldn't solve 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedList = []
        rightList = []
        # Loop while root is not null
        while root:
            print(root)
            if root.left:
                prev = root
                root = root.left
                if prev.right:
                    prev.left = None
                    rightList.append(prev)
            # If only right child then make curr right child
            elif root.right:
                sortedList.append(root.val)
                root = root.right
            # If no left child append current val to list
            else:
                sortedList.append(root.val)
                if rightList:
                    root = rightList.pop()
                else:
                    root = None
        print(sortedList)
        return sortedList[k-1]
    

# This was the attempt after some googling


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedList = []
        while root:
            # no left so append and go right
            if root.left is None:
                sortedList.append(root.val)
                root = root.right

            else:
                # Previous node
                prev = root.left
                while(prev.right is not None and prev.right != root):
                    prev = prev.right

                # Make current node right child of its prev
                if(prev.right is None):
                    prev.right = root
                    root = root.left
                # fix the right
                else:
                    prev.right = None
                    sortedList.append(root.val)
                    root = root.right

        return sortedList[k-1]