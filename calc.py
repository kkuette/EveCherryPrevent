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
                raw_value[idx] = -value
            elif idx is 'Mercoxit':
                raw_value[idx] = 1
            else:
                raw_value[idx] =  value
        for idx, value in raw_value.items():
            print (idx, ":", value)
        return raw_value

    def calcReward(self, extracted):
        reward = 0
        for idx, value in extracted.items():
            if idx is not "Total":
                reward += value * self.raw_value[idx]
        return reward

print ("\n### Reward value per unit ###\n")
distrib = belt.calcAvgDistrib()
extracted = belt.raw['Colossal']
calc = Calc(distrib)
print ("")
print ("### Total reward ###\n")
print (calc.calcReward(extracted))
