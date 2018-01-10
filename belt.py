''' Ore Qty need to be updated '''

from collections import Counter

class Belt:

    def __init__(self):
        self.raw = {
        'Small' : self.Small(),
        'Medium' : self.Medium(),
        'Large' : self.Large(),
        'Enormous' : self.Enormous(),
        'Colossal' : self.Colossal()
        }

    def AvgBeltQuantity(self):
        basic = Counter()
        nb_belt = 0
        for i, v in self.raw.items():
            basic += Counter(v)
            nb_belt += 1
        for idx, value in basic.items():
            basic[idx] /= nb_belt
        return basic

    def Small(self):
        _Small = {
        'Arkonor' : 9600,
        'Bistot' : 12800,
        'Crokite' : 30000,
        'Dark Ochre' : 16000,
        'Gneiss' : 170000,
        'Spodumain' : 300000,
        'Mercoxit' : 0
        }
        return _Small

    def Medium(self):
        _Medium = {
        'Arkonor' : 28000,
        'Bistot' : 38700,
        'Crokite' : 84700,
        'Dark Ochre' : 31000,
        'Gneiss' : 340000,
        'Spodumain' : 270000,
        'Mercoxit' : 2600
        }
        return _Medium

    def Large(self):
        _Large = {
        'Arkonor' : 29900,
        'Bistot' : 57000,
        'Crokite' : 124000,
        'Dark Ochre' : 60000,
        'Gneiss' : 313500,
        'Spodumain' : 368100,
        'Mercoxit' : 3500
        }
        return _Large

    def Enormous(self):
        _Enormous = {
        'Arkonor' : 58000,
        'Bistot' : 86000,
        'Crokite' : 169000,
        'Dark Ochre' : 50000,
        'Gneiss' : 	540000,
        'Spodumain' : 542000,
        'Mercoxit' : 5200
        }
        return _Enormous

    def Colossal(self):
        _Colossal = {
        'Arkonor' : 60800,
        'Bistot' : 114300,
        'Crokite' : 225200,
        'Dark Ochre' : 115000,
        'Gneiss' : 630000,
        'Spodumain' : 736200,
        'Mercoxit' : 7000
        }
        return _Colossal

class ORE(Belt):

    def __init__(self):
        Belt.__init__(self)
        self._ore = {
        'Arkonor': self.Arkonor(),
        'Bistot': self.Bistot(),
        'Crokite': self.Crokite(),
        'Dark Ochre': self.Dark_Ochre(),
        'Gneiss': self.Gneiss(),
        'Spodumain': self.Spodumain(),
        'Mercoxit': self.Mercoxit()
        }

    def getVolume(self, ore):
        if ore == "All":
            lst = []
            for idx, value in self._ore.items():
                lst.append([idx, value['Volume']])
            return lst
        else:
            return self._ore[ore]['Volume']

    def getIskValueRaw(self, ore):
        if ore == "All":
            lst = []
            for idx, value in self._ore.items():
                lst.append([idx, value['IskValueRaw']])
            return lst
        else:
            return self._ore[ore]['IskValueRaw']

    def setIskValueRaw(self, ore, value):
        self._ore[ore]['IskValueRaw'] = value

    def Arkonor(self):
        _Arkonor = {
        'Volume': 16,
        'IskValueRaw': 0
        }
        return _Arkonor

    def Bistot(self):
        _Bistot = {
        'Volume': 16,
        'IskValueRaw': 0
        }
        return _Bistot

    def Crokite(self):
        _Crokite = {
        'Volume': 16,
        'IskValueRaw': 0
        }
        return _Crokite

    def Dark_Ochre(self):
        _Dark_Ochre = {
        'Volume': 8,
        'IskValueRaw': 0
        }
        return _Dark_Ochre

    def Gneiss(self):
        _Gneiss = {
        'Volume': 5,
        'IskValueRaw': 0
        }
        return _Gneiss

    def Spodumain(self):
        _Spodumain = {
        'Volume': 16,
        'IskValueRaw': 0
        }
        return _Spodumain

    def Mercoxit(self):
        _Mercoxit = {
        'Volume': 40,
        'IskValueRaw': 0
        }
        return _Mercoxit
