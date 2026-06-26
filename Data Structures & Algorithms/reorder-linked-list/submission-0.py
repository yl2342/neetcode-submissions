# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        # once travervse finished, find the head of second sub-link-list
        second = s.next
        prev = s.next = None # break it

        # reverse the second part of the link-list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp # move to next
        
        # once finish reverse, insert one from one sublsit at a time
        first_ll, second_ll = head, prev # prev now points to last node
        while second_ll: # we know this should be shorter
            tmp1, tmp2 = first_ll.next, second_ll.next
            first_ll.next = second_ll
            second_ll.next = tmp1
            first_ll, second_ll = tmp1, tmp2 # move to next 


    






        
        