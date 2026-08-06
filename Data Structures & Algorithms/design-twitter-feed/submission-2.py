class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.tweets[userId].append((tweetId, self.t))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.follows[userId])
        users.add(userId) 
        tweet_lists = []
        for user in users:
            if len(self.tweets[user]) > 0:
                tweet_lists.append(self.tweets[user])
        h = []
        for i, tweet_list in enumerate(tweet_lists):
            index = len(tweet_list) - 1
            tw_id, time = tweet_list[index]
            heapq.heappush(h, (-time, tw_id, i, index))
        res = []
        while len(res) < 10 and h:
            _, tw_id, list_id, item_index = heapq.heappop(h)
            res.append(tw_id)
            if item_index > 0:
                next_tw, next_tw_time = tweet_lists[list_id][item_index - 1]
                heapq.heappush(h, (-next_tw_time, next_tw, list_id, item_index - 1))
        return res
        
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

