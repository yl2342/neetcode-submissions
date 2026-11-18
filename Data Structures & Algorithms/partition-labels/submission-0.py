class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # extract last index for each unique character
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        res = []
        size = 0
        end = 0
        for j in range(len(s)):
            end = max(end, lastIndex[s[j]])
            size += 1
            if j == end:
                res.append(size)
                size = 0
        return res
        