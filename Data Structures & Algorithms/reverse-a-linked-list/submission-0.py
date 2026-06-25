# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #############
        # Iteration #
        #############
        prev, curr = None, head
        while curr:
            # place holder to hold it
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev



        # #############
        # # recursion #
        # #############
        # Key insight: newHead=4 was returned unchanged all the way up the chain. Only head.next.next and head.next were modified in each frame.
        # # base case
        # if not head:
        #     return None
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return newHead


        






    
        