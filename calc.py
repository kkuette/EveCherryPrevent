from belt import Belt
from user import User

class Calc:

    def __init__(self, distrib):
        self.cherry = ['Arkonor', 'Bistot', 'Gneiss', 'Crokite']
        self.dirty = ['Dark Ochre', 'Spodumain', 'Mercoxit']
        self.raw_value = self.clacRawValue(self.calcRedistrib(distrib))

    def calcDistribDirty(self, distrib):
        self.dist_dirty = 0
        for idx, value in distrib.items():
            if idx in self.dirty:
                self.dist_dirty += value

    def calcDistribCherry(self, distrib):
        self.dist_cherry = 0
        for idx, value in distrib.items():
            if idx in self.cherry:
                self.dist_cherry += value

    def calcRedistrib(self, distrib):
        self.calcDistribDirty(distrib)
        self.calcDistribCherry(distrib)
        print ("\n### Distrib value of categories before redistrib###\n")
        print ("cherry", self.dist_cherry, "dirty", self.dist_dirty, "\n")
        for idx, value in distrib.items():
            if idx in self.dirty:
                distrib[idx] = (value / self.dist_dirty) / 2
            else:
                distrib[idx] = (value / self.dist_cherry) / 2

        c = 0
        d = 0
        for idx, value in distrib.items():
            if idx in self.cherry:
                c += value
            else:
                d += value
        print ("### Distrib value of categories after redistrib###\n")
        print ("cherry", c, "dirty", d, "\n")
        print ("### Reward value per unit ###\n")
        return distrib

    def clacRawValue(self, distrib):
        raw_value = {}
        for idx, value in distrib.items():
            if idx in self.cherry:
                raw_value[idx] = -value
            else:
                raw_value[idx] = value
        for idx, value in raw_value.items():
            print (idx, ":", value)
        return raw_value

    def calcReward(self, extracted):
        reward = 0
        print ("\n### Total unit per ore mined ###\n")
        for idx, value in extracted.items():
            if idx is not "Total":
                reward += value * self.raw_value[idx]
                print (idx, ":", value)
        print ("\n### Total reward ###\n")
        return reward

belt = Belt() # Init belt values
distrib = belt.calcAvgDistrib() # Calc average distribution from belt values

calc = Calc(distrib) # Init calc object with average distribution

usr = User("KKuette") # Init user

extracted = belt.raw['Small'] # Normaly it will get user extraction info
#extracted['Gneiss'] = 0

print (calc.calcReward(extracted)) # Calc reward from user extraction info
