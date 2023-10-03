# This was my simple solution. I had a recursive one that I did in the past.
# This is problem 2 so maybe go check it out.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
    # get right order of first list as an int
    # get right order of second list as an int
    # add together both ints
    # reverse order the sum
    # return the sum

        num1, num2 = "", ""
        cur_node = l1
        # Pass one, transform l1 to string
        while cur_node:
            num1 = str(cur_node.val) + num1
            cur_node = cur_node.next

        cur_node = l2
        # Pass two, transform l2 to string
        while cur_node:
            num2 = str(cur_node.val) + num2
            cur_node = cur_node.next

        sum = str(int(num1) + int(num2))
        node = ListNode()
        cur_node = node
        for num in reversed(sum):
            cur_node.next = ListNode(num)
            cur_node = cur_node.next

        return node.next