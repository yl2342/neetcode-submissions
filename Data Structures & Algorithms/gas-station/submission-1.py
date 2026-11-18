class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy problem
        if sum(gas) < sum(cost):
            return -1
        total = 0 # cumulative
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                # start over
                total = 0
                res = i + 1
        return res

        