# Got this on my own, LETS FUCKING GOOOOO!!!


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        dummy = ListNode(None, head)
        length = 0
        # Loop through list to get length of the list
        while tail.next:
            tail = tail.next
            length += 1

        # Calculate index of erased node by subtracting from length
        index = length - (n-1)
        length = 0
        cur_node = dummy
        while cur_node:
            # erase node by using a prev_node pointer
            prev_node = cur_node
            cur_node = cur_node.next
            if length == index:
                # this overwrites the value of the current node
                prev_node.next = cur_node.next
            length+=1
        return dummy.next