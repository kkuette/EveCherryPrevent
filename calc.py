from belt import ORE, Belt
from user import User

from collections import Counter

class Calc:

    def __init__(self, weights, distrib):
        self.distrib = self.calcDistrib(distrib)
        self.calcCoef(weights)
        self.cherry = ['Arkonor', 'Bistot', 'Gneiss', 'Crokite']
        self.dirty = ['Dark Ochre', 'Spodumain', 'Mercoxit']

    def calcDistrib(self, distrib):
        total = 0
        _distrib = {}
        for idx, value in distrib.items():
            total += value
        for idx, value in distrib.items():
            _distrib[idx] = value / total
        return _distrib


    def calcCoef(self, weights):
        self.coefficients = {key: value['Volume'] for (key, value) in weights.items()}
        for idx, value in self.distrib.items():
            self.coefficients[idx] /= value

    def calcDenoms(self):
        self.sumCherry = 0
        self.sumDirty = 0
        for i, v in self.distrib.items():
            if i in self.cherry:
                self.sumCherry += v * self.coefficients[i]
            else:
                self.sumDirty += v * self.coefficients[i]

    def calcReward(self, extracted):
        rewardCherry = 0
        rewardDirty = 0
        self.calcDenoms()
        for idx, value in extracted.items():
            if idx in self.cherry:
                rewardCherry += value * self.coefficients[idx]
            else:
                rewardDirty += value * self.coefficients[idx]
        rewardCherry /= self.sumCherry
        rewardDirty /= self.sumDirty
        print(rewardCherry)
        print(rewardDirty)
        print ("\n### Total reward ###\n")
        #oef = 10000
        return int(rewardDirty-rewardCherry)

belt = ORE() # Init belt values

basic = Counter()
nb_belt = 0
for i, v in belt.raw.items():
    basic += Counter(v)
    nb_belt += 1
for idx, value in basic.items():
    basic[idx] /= nb_belt

# Normally it will get user extraction info
extracted = belt.raw['Colossal']


calc = Calc(belt._ore, basic) # Init calc object with average distribution

usr = User("KKuette") # Init user

#extracted['Gneiss'] = 0
extracted['Mercoxit'] = 0
print (calc.calcReward(extracted)) # Calc reward from user extraction info
