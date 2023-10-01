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
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next    # shift slow by one
            fast = fast.next.next # shift fast by two

        second = slow.next  # second half of list
        prev = slow.next = None

        # reverse second half of list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge the two halfs
        first, second = head, prev
        while second:   # second can be shorter than first
            tmp1, tmp2 = first.next, second.next
            first.next = second
            # Insert second node inbetween first and first.next (thats what tmp1 is)
            second.next = tmp1
            first, second = tmp1, tmp2