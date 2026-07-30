class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userid ->[count, tweetid]
        self.followMap = defaultdict(set) # userid -> userid of followee

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # decrement for making minHeap 


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        # tweet feed should include the user's own tweet
        self.followMap[userId].add(userId)

        # set up starting point
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # does this user have more (older) tweets left to offer
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1]) # if make index <0, then no tweet left to offer
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
