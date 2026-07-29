class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Minheap with K largest integers
        # heapq isn't a heap class — it's a module of functions that operate on ordinary Python lists. 
        # heapq.heapify(lst) just rearranges the elements of the list in place so they satisfy the heap invariant. 
        # It doesn't convert the list into some Heap object, so the list has no .heappush method. 
        # It's still a plain list, and type(self.minHeap) is still list after heapify.

        # The heap invariant is only maintained if you only mutate the list through heapq functions. If you do self.minHeap.append(val) directly, you break it.
        # heapq is a min-heap, always. heap[0] is the smallest element.

        # The heap property. Every parent is ≤ both of its children (min-heap). That's the only rule.

        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
