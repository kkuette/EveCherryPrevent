class Belt:

    def __init__(self):
        ''' Ore Qty need to be updated '''
        self.raw = {
        'Small' : self.Small(),
        'Medium' : self.Medium(),
        'Large' : self.Large(),
        'Enormous' : self.Enormous(),
        'Colossal' : self.Colossal()
        }

    def calcDistrib(self):
        distrib = {}
        for idx, value in self.raw.items():
            tmp = {}
            for i, v in value.items():
                if i is not "Total":
                    tmp[i] = v / value['Total']
            distrib[idx] = tmp
        return distrib

    def calcAvgDistrib(self):
        distrib = self.calcDistrib()
        avg_distrib = {}
        nb_belt = 0
        for idx, value in distrib.items():
            for i, v in value.items():
                if i is not "Total":
                    if nb_belt > 0:
                        avg_distrib[i] += v
                    else:
                        avg_distrib[i] = v
            nb_belt += 1
        for idx, value in avg_distrib.items():
            avg_distrib[idx] = value / nb_belt
        return avg_distrib

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
        tot = 0
        for idx, value in _Small.items():
            tot += value
        _Small['Total'] = tot
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
        tot = 0
        for idx, value in _Medium.items():
            tot += value
        _Medium['Total'] = tot
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
        tot = 0
        for idx, value in _Large.items():
            tot += value
        _Large['Total'] = tot
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
        tot = 0
        for idx, value in _Enormous.items():
            tot += value
        _Enormous['Total'] = tot
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
        tot = 0
        for idx, value in _Colossal.items():
            tot += value
        _Colossal['Total'] = tot
        return _Colossal
