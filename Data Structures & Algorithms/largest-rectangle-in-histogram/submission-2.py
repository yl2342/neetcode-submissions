class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # pattern: monotonic/ most recent -> stack
        max_area = 0
        stack = [] # store (index, height)
        for i, h in enumerate(heights):
            # discontinuation and pop
            start_index = i
            while stack and stack[-1][1] > heights[i]:
                s_i, s_h = stack.pop()
                max_area = max(max_area, s_h * (i - s_i))
                start_index = s_i # update the stat index for added stack item
            stack.append((start_index, h))
        
        # calculte the rest in stack:
        for s_i, s_h in stack:
            max_area = max(max_area, s_h * (len(heights) - s_i))
        
        return max_area
            



        