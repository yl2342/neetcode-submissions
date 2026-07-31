class MedianFinder:

    def __init__(self):
        # small and large should be ~ equal sizw
        self.small = [] # maxHeap
        self.large = [] # minHeap
        
    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else: # default to small
            heapq.heappush(self.small, -1 * num)

        # balance if uneven
        if len(self.small) - len(self.large) > 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (-1 *self.small[0]+self.large[0]) / 2
        
        