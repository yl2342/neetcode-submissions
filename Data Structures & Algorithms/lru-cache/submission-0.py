
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        # add left and right pointer to keep track and maintain the node of doubly linked list
        self.left, self.right = Node(0,0), Node(0,0) # left/right dummy node
        self.left.next = self.right
        self.right.prev = self.left

    # remove, remove any node
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert to the right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        

        
    
    

        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # remove it
            self.insert(self.cache[key]) # shift to right
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # remove it
        self.cache[key] = Node(key, value) # update node/value
        self.insert(self.cache[key]) # shift to right
        # add one, check cap
        if len(self.cache) > self.cap: 
            lru = self.left.next
            self.remove(lru) # remove least recently used
            del self.cache[lru.key]
















        
