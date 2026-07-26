class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python only support minHeap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) # negative value 
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first-second)
        
        heapq.heappush(stones, 0) # for edge case stones is empty
        return abs(stones[0])
        