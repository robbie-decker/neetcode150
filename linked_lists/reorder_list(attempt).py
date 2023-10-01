# These linked lists are fucking me up a little :/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # # Make copy of head
        # dummy = ListNode()
        # dummy.next = head
        # tail = dummy.next
        # headVal = head.val

        # # Get last element of list
        # while tail.next.next:
        #     tail = tail.next
        # # Insert last where the current head is at.
        # dummy.next.val = tail.next.val
        # tail.next = None

        # head = ListNode(headVal, head)
        # # This is close but I overwriting the address of head.