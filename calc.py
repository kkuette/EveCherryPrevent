from belt import Belt
from user import User

from collections import Counter

class Calc:

    def __init__(self, distrib):
        self.distrib = distrib
        self.coefficients = {key: 1 for (key, value) in self.distrib.items()}
        self.cherry = ['Arkonor', 'Bistot', 'Gneiss', 'Crokite']
        self.dirty = ['Dark Ochre', 'Spodumain', 'Mercoxit']

    def calcDenoms(self):
        self.sumCherry = 0
        self.sumDirty = 0
        for i, v in self.distrib.items():
            if i == "Total":
                continue
            if i in self.cherry:
                self.sumCherry += v * self.coefficients[i]
            else:
                self.sumDirty += v * self.coefficients[i]

    def calcReward(self, extracted):
        rewardCherry = 0
        rewardDirty = 0
        self.calcDenoms()
        for idx, value in extracted.items():
            if idx is not "Total":
                if idx in self.cherry:
                    rewardCherry += value * self.coefficients[idx]
                else:
                    rewardDirty += value * self.coefficients[idx]
        rewardCherry /= self.sumCherry
        rewardDirty /= self.sumDirty
        print(rewardCherry)
        print(rewardDirty)
        print ("\n### Total reward ###\n")
        return rewardDirty-rewardCherry

belt = Belt() # Init belt values

basic = Counter()
for i, v in belt.raw.items():
    basic += Counter(v)

# Normally it will get user extraction info
extracted = Counter(belt.raw['Small']) + Counter(belt.raw['Colossal']) + Counter({"Arkonor":1})

calc = Calc(basic) # Init calc object with average distribution

usr = User("KKuette") # Init user

#extracted['Gneiss'] = 0

print (calc.calcReward(extracted)) # Calc reward from user extraction info
