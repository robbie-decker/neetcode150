# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        newnewList = None
        topList1 = list1
        topList2 = list2
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list2 == None and list1 == none:
            return None
        
        if list1.val <= list2.val:
            current = topList1
            topList1 = topList1.next
        else:
            current = topList2
            topList2 = topList2.next
        # newList = current
        # current.next = None
        while current:
            print(1, current)
            print(2, current.next)
            
            current.next = newList
            newList = current
            # while newList.next:

            
            print(3, newList)

            if topList1 != None and topList2 != None:
                if topList1.val <= topList2.val:
                    current = topList1
                    topList1 = topList1.next
                else:
                    current = topList2
                    topList2 = topList2.next
            # elif topList1 != None and topList1.val > topList2.val:
            else:
                if topList1 == None and topList2 == None:
                    current = None
                else:
                    if topList1 == None:
                        current = topList2
                        topList2 = topList2.next
                    else:
                        current = topList1
                        topList1 = topList1.next
        current = newList
        while current:
            # Get next node and assign it to variable
            next_node = current.next
            # Set the current next value to the list we made so far 
            current.next = newnewList
            newnewList = current
            current = next_node
        return newnewList

