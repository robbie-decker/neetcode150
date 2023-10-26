# I am not entirely seeing the heap method here.
class Twitter:

    def __init__(self):
        # Keep track of users and who they follow
        self.users = {}
        # Keep track of tweets 
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Have not seen user yet so add
        if userId not in self.users:
            self.users[userId] = {"following": []}
        # [{userId, tweetId}, ...]
        self.tweets.append({"userId": userId, "tweetId": tweetId})
    
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        if userId not in self.users:
            return res

        followedUsers = self.users[userId]['following'] + [userId]
        for tweet in reversed(self.tweets):
            if tweet["userId"] in followedUsers:
                res.append(tweet["tweetId"])
            # Only want 10 most recent tweets
            if len(res) >= 10:
                break
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # Have not seen this user yet
        if followerId not in self.users:
            self.users[followerId] = {"following": [followeeId]}
        else:
            self.users[followerId]["following"].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            return
        if followeeId not in self.users[followerId]["following"]:
            return
        self.users[followerId]["following"].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)