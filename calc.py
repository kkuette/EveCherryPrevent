from belt import ORE, Belt
from user import User

from collections import Counter

class Calc:

    def __init__(self, ore, avg_belt_quantity):
        '''ore: dict composed of all ORE volume
           distrib: average ORE quantity in belt'''

        self.distrib = self.calcDistrib(avg_belt_quantity)
        self.ore = ore
        self.calcCoef(ore)
        self.cherry = ['Arkonor', 'Bistot', 'Gneiss', 'Crokite']
        self.dirty = ['Dark Ochre', 'Spodumain', 'Mercoxit']
        self.extracted_volume = 0
        self.extracted_isk_value = 0

    def getExtractedVolume(self, name):
        ''' If calcReward not called extracted volume value is 0
        All: return list of all component Volume'''
        if self.extracted_volume == 0:
            return 0
        if name == "All":
            lst = []
            for idx, value in self.exracted_volume.items():
                lst.append([idx, value])
            return lst
        else:
            return self.extracted_volume[name]

    def getExtractedIskValue(self, name):
        ''' If calcReward not called extracted volume value is 0
        All: return list of all component Volume'''
        if self.extracted_isk_value == 0:
            return 0
        if name == "All":
            lst = []
            for idx, value in self.exracted_isk.items():
                lst.append([idx, value])
            return lst
        else:
            return self.extracted_isk_value[name]

    def calcDistrib(self, distrib):
        ''' Calc distribution of average ore quantity in belt'''
        total = 0
        _distrib = {}
        for idx, value in distrib.items():
            total += value
        for idx, value in distrib.items():
            _distrib[idx] = value / total
        return _distrib


    def calcCoef(self, ore):
        ''' Calc coefficient based on ORE volume / ORE distribution'''
        self.coefficients = {key: value['Volume'] for (key, value) in ore.items()}
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
        '''Calc extraction reward based on coefficient * extracted quantity'''
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
        self.extracted_volume = self.calcExtractedVolume(extracted)
        self.extracted_isk_value = self.calcExtractedIskValue(extracted)
        return int(rewardDirty-rewardCherry)

    def calcExtractedVolume(self, extracted):
        '''Calc extracted volume based on extracted quantity * ORE Volume'''
        _volume = {}
        total = 0
        for idx, value in extracted.items():
            _volume[idx] = value * self.ore[idx]['Volume']
            total += _volume[idx]
        _volume['Total'] = total
        return _volume

    def calcExtractedIskValue(self, extracted):
        _isk_value = {}
        total = 0
        for idx, value in extracted.items():
            _isk_value[idx] = value * self.ore[idx]['IskValue']
            total += _isk_value[idx]
        _isk_value['Total'] = total
        return _isk_value


belt = ORE() # Init belt values

extracted = belt.raw['Colossal']# Normally it will get user extraction info

calc = Calc(belt._ore, belt.AvgBeltQuantity()) # Init calc object with average distribution

usr = User("KKuette") # Init user

print (calc.calcReward(extracted)) # Calc reward from user extraction info
