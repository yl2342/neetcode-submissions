class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key: [val, timestamp]

        # Key Behaviors of defaultdict:
        # accessing missing key → creates it with default value
        # Use .get() if you DON'T want to create the key on access
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # All the timestamps of set are strictly increasing.
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        data = self.store[key]
        # sorted, logn -> binary search
        l, r = 0, len(data)-1
        while l <= r:
            m = (l+r) // 2
            if data[m][1] <= timestamp:
                res = data[m][0] # update result first
                l = m + 1
            else:
                r = m - 1
        return res
        

        
