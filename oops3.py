#Class Methods ----------------->>>>>>>>>>

'''Attributes are the things that the object has & the methods are the behaviour of the objects'''

class youtube:
    def __init__(self,username,subscribers=0,subscription = 0):
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription
    def subscribe(self,user):
        user.subscribers += 1
        self.subscription += 1
    
user1 = youtube("Nittyansh")
user2 = youtube("Shivansh")
user1.subscribe(user2)
print(user1.subscribers)
print(user1.subscription)
print("now for user 2")
print(user2.subscribers)
print(user2.subscription)