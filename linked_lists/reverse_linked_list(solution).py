# I am gonna be honest, the recursive way kinda does not make sense in my head. I think
# two pointers way makes more sense
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head
        while current:
            # Get next node and assign it to variable
            next_node = current.next
            # Set the current next value to the list we made so far
            # Basically appending what we have seen so far 
            current.next = new_list
            # Add current node to the list
            new_list = current
            # Go to next node
            current = next_node
        return new_list

# From the internet
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If linked list is empty
        if (head == None):
            return head

        # At end of list 
        if (head.next == None):
            return head

        # Start of recursion 
        head1 = self.reverseList(head.next)
        # Put first element at the end
        head.next.next = head
        head.next = None
        return head1
    

# From neetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            # Reversing the link
            head.next.next = head
        head.next = None
        return newHead