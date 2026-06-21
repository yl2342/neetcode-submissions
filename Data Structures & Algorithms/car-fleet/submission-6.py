class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # for sorting 2-d array/list of tuples
        # Python compares lists like tuples — first elements first, then second if tied:
        # sorted(arr)[::-1]sorted(arr)[::-1]
        # It's two operations chained together:
        # 1. sorted(arr)
        # Returns a new sorted list in ascending order (default).
        # 2. [::-1] Reverses the result. This is Python's slice syntax:
        # [start : stop : step]
        # With step = -1 and no start/stop → iterate the whole list backwards.
        # Sorting by a specific column: arr.sort(key=lambda x: x[0]) 
        # Multi-key sort (sort by col 0, break ties with col 1): arr.sort(key=lambda x: (x[0], x[1]))
        # Reverse order: arr.sort(key=lambda x: x[0], reverse=True)
        # Mixed direction (col 0 asc, col 1 desc): Mixed direction (col 0 asc, col 1 desc): arr.sort(key=lambda x: (x[0], -x[1]))

        pairs = [[p, s] for p, s in zip(position, speed)]
        # sort by the position first, by descending order / or we can use reverse = True
        pairs.sort(reverse = True) # or add ,reverse = True

        stack = [] # store time to target
        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack)>=2 and stack[-1] <= stack[-2]: # collide
                stack.pop()
        return len(stack)

