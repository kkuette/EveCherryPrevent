from belt import Belt
from user import User

belt = Belt()
usr = User("KKuette")

class Calc:

    def __init__(self, distrib):
        self.cherry = ['Arkonor', 'Bistot', 'Gneiss', 'Crokite', 'Spodumain',  'Mercoxit']
        self.dirty = ['Dark Ochre']
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
        for idx, value in distrib.items():
            if idx in self.dirty:
                distrib[idx] = (value / (self.dist_dirty)) / 2
            else:
                distrib[idx] = (value / (self.dist_cherry)) / 2

        c = 0
        d = 0
        for idx, value in distrib.items():
            if idx in self.cherry:
                c += value
            else:
                d += value
        print ("\n### Distrib value of categories ###\n")
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
        print ("")
        print ("### Total reward ###\n")
        return reward


distrib = belt.calcAvgDistrib()
extracted = belt.raw['Colossal']
extracted['Spodumain'] = 0
calc = Calc(distrib)


print (calc.calcReward(extracted))
