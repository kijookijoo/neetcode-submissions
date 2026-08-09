class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.time = 0
        self.posts = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.following[userId].add(userId)
        idx = len(self.posts[userId])
        self.posts[userId].append((-self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        for f in self.following[userId]:
            if self.posts[f]:   
                idx = len(self.posts[f]) - 1
                timestamp, tweetId, followeeId = self.posts[f][idx]
                heapq.heappush(heap, (timestamp, tweetId, followeeId, idx - 1))
        
        while len(res) < 10 and heap:
            timestamp, tweetId, followeeId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:    
                timestamp, postId, userId = self.posts[followeeId][idx]
                heapq.heappush(heap, (timestamp, postId, userId, idx - 1))
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
