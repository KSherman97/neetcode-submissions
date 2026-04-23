# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp_node = ListNode(-1, None)
        curr_node = temp_node

        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    curr_node.next = list1
                    list1 = list1.next
                else:
                    curr_node.next = list2
                    list2 = list2.next

                curr_node = curr_node.next

            if list1 is not None:
                curr_node.next = list1
            else:
                curr_node.next = list2  
        return temp_node.next