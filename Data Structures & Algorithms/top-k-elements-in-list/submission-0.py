class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # result
        res = []
        # hash map to count: O(n)
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #########################
        # Bucket sort: optimal O(n) + O(n)
        #########################
        freq = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1, -1, -1): # len(num)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res





        
        #########################################
        # # create and sory an array: O(nlogn) + O(n)
        #########################################

        # arr = [[c,n] for n, c in count.items()]
        # arr.sort()
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

        ######################
        # MinHeap: O(nlogk) +  O(n+k)
        ######################
        ## By pushing (frequency, value) pairs into the heap and removing the smallest whenever the heap grows beyond size k, we ensure that the heap always contains the top k most frequent elements.
        # heap = []
        # for n,c in count.items():
        #     heapq.heappush(heap, (c,n))
        #     if len(heap) > k:
        #         heapq.heappop(heap) # keep the heap size <=k
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        # OR use the max heap: T: O(nlogn)
        # heap = []
        # for n, c in count.items():
        #     heapq.heappush(heap, (c * (-1),n))
        # for i in range(k):
        #     res.append((heapq.heappop(heap)[1]))
        # return res




        # Minheap: heapq is a built-in module that implements a min-heap — a data structure that always gives you the smallest element first in O(log n) time.
        # heapq.heapify(nums)         # rearranges list into heap in-place, O(n): because most nodes are leaves and leaves need zero work, converge to 2n
        # heapq.heappush(nums, 2)     # inserts 2, maintains heap, O(log n)
        # heapq.heappop(nums)         # removes and returns smallest, O(log n)
        # Max-heap (heapq only does min) — negate the values:
        # nums = [3, 1, 4, 1, 5]
        # heap = []
        # for n in nums:
        #     heapq.heappush(heap, -n)    # store negated
        # -heapq.heappop(heap)            # → 5 (the actual max)
        # Heap of tuples — useful for priority queues:
        # heap = []
        # heapq.heappush(heap, (2, "task B"))   # (priority, value)
        # heapq.heappush(heap, (1, "task A"))
        # heapq.heappush(heap, (3, "task C"))
        # heapq.heappop(heap)     # → (1, "task A")  lowest priority number first




        


        