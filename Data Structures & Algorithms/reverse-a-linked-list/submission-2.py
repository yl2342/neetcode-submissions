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
            temp = curr.next # save where curr.next points as temp
            curr.next = prev # reverse
            prev = curr # move prev to curr
            curr = temp # move curr 1 step forward to previously stored temp
        return prev



        # #############
        # # recursion #
        # #############
        # One-liner: Recursively dive to the last node to find the new head, then reverse one pointer per frame on the way back up.
        # Key insight: newHead=4 was returned unchanged all the way up the chain. Only head.next.next and head.next were modified in each frame.
        # # base case
        #  None goes up one level, gets ignored, and dies. None just disappears. It never gets assigned anywhere. 
        # if not head:
        #     return None
        # newHead = head # will be overwritten as head's next move forward
        # if head.next:
        #     newHead = self.reverseList(head.next) # base case skipped, if head.next was none, this will not be executed
        #     head.next.next = head # point the NEXT node backward at me
        # head.next = None # cut MY forward pointer (prevents a cycle), always execute

        # return newHead


        






    
        