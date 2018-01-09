from belt import Belt
from user import User

belt = Belt()
usr = User("KKuette")

class Calc:

    def __init__(self, distrib):
        self.rare = ['Arkonor', 'Bistot', 'Gneiss', 'Crokite']
        self.raw_value = self.clacRawValue(distrib)

    def clacRawValue(self, distrib):
        raw_value = {}
        for idx, value in distrib.items():
            if idx in self.rare:
                raw_value[idx] = 1 - value
            else:
                raw_value[idx] = value
        return raw_value

    def calcReward(self, extracted):
        reward = 0
        for idx, value in extracted.items():
            if idx is not "Total":
                reward += value * self.raw_value[idx]
        return reward

distrib = belt.calcAvgDistrib()
calc = Calc(distrib)
print (calc.calcReward(belt.raw['Colossal']))
