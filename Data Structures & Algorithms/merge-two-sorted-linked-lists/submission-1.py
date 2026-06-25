# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node deal with edge cases
        # The dummy node solves a specific problem: how do you build a linked list when you don't know what the head will be yet?
        # The Problem Without Dummy
        # If you tried to track head directly, your first iteration needs special-casing: 
        # you'd need an if head is None branch just for the first node. Messy.
        # dummy is a fake node at position -1. You never return it — it exists purely so that 
        # node.next = ... works uniformly from the very first iteration, with no special case for the head.
        # dummy is a permanent anchor, never moves, node is the "moving pen"
        # Dummy lets you treat "attaching the first node" and "attaching every subsequent node" as the exact same operation: node.next = ..., node = node.next.
        # This pattern appears constantly in linked list problems — reverse, merge sort, partition, etc. 
        # Whenever you're building a new list and don't know the head upfront, reach for a dummy node.
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        # any link list traversed already
        node.next = list1 or list2

        return dummy.next
        



        