class SocialMediaAccount:
    def __init__(self, username, password):
        self.username= username
        self.password= password 
    def log_in(self):
        print("Logging in-")
        
    def post(self):
        print("Posting-")
        
    

class InstagramAccount(SocialMediaAccount): 
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password, number_of_followers)
        self.number_of_followers= number_of_followers
    def sharestory(self):
        print("Sharing Story-")
        
        
class TwitterAccount(SocialMediaAccount): 
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password, number_of_tweets)
        self.number_of_tweets= number_of_tweets
    def tweet(self):
        print("Tweeting")