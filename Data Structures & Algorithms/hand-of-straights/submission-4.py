class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        # count = collections.Counter(hand)
        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)
        # min heap implementation
        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    # first is a static var  stays fixed for the entire loop
                    # minHeap[0] updates dynamically every time you pop from the heap.
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True

