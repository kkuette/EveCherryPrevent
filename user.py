class User:

    def __init__(self, name):
        self.name = name
        self.extracted = 0
        self.reward = 0

    def setReward(self, reward):
        self.reward = reward

    def setExtracted(self, value):
        self.extracted = value

    def getReward(self):
        return self.reward

    def getExtracted(self):
        return self.extracted

class UserStorage:

    def __init__(self):
        self.users = []

    def addUser(self, user):
        self.users.append(user)

    def getUser(self, name):
        for user in self.users:
            if name == user.name:
                return user
