"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # I dont think I need a dummy node
        # Ok maybe I do need one
        copy = ListNode(0)
        copy_pointer = copy
        curr_node = head
        # This will get nodes pointing to next node
        while curr_node:
            # Set values of current node 
            copy_pointer.next = Node(curr_node.val, curr_node.next)
            if curr_node.random:
                copy_pointer.next.random = curr_node.random.val
            # Move down linked list
            curr_node = curr_node.next
            # Move down copy
            copy_pointer = copy_pointer.next
        
        # Now set random pointers
        copy_pointer = copy.next
        # Loop through copy
        # This feels very brute forcey but I really want an answer
        self.display(copy_pointer)
        while copy_pointer:
            curr_node = copy.next
            # Loop through list again to find random val
            while curr_node:
                # Bad because there can be repeats
                if curr_node.val == copy_pointer.random:
                    copy_pointer.random = curr_node
                curr_node = curr_node.next
            copy_pointer = copy_pointer.next
        return copy.next

    def display(self, node):
        nodes = []
        head = node
        while head:
            if head.random:
                nodes.append((head.val, head.random))
            else:
                nodes.append((head.val, None))    
            head = head.next
        print(nodes)