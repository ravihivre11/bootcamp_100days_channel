class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

User1 = User(1,"ravi")
User2 = User(2,"kumar")
User1.follow(User2)
print(User1.followers)
print(User2.followers)
