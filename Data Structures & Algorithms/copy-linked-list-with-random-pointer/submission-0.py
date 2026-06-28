"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2copy = {None: None}
        
        # first pass construct the copy of node:
        curr = head
        while curr:
            node_copy = Node(x=curr.val)
            old2copy[curr] = node_copy
            curr = curr.next

        # restart, second pass, reassign pointer
        curr = head
        while curr:
            node_copy = old2copy[curr]
            node_copy.next = old2copy[curr.next]
            node_copy.random = old2copy[curr.random]
            curr = curr.next
        return  old2copy[head]
        
        



        