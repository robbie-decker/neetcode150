# Okay so I got kinda close I think but I just can't get my recursion to work.
# It feels super tangible


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prevVal=0) -> Optional[ListNode]:
        print(head, prevVal)
        # if prev >= 1:
        #     return head
        
        # At end of linked list
        if(head.next is None):
            print("this happened", head)
            return ListNode(head.val, self.reverseList(ListNode(prevVal)))
        else:
            self.reverseList(head.next, head.val)