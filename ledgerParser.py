oreNames = ["Arkonor", "Bistot", "Crokite", "Dark Ochre", "Gneiss", "Spodumain", "Mercoxit"]

def parseLedger(ledger):
    ledgerData = {}
    lines = ledger.splitlines()
    print (lines)
    for line in lines:
        lineId = ""
        parts = line.split("    ")
        nameParts = parts[1].split(" ")
        for namePart in nameParts:
            if namePart in oreNames:
                lineId = namePart
                if lineId == "Ochre":
                    lineId = "Dark Ochre"
                break
        qt = int(parts[2].replace(" ", ""))
        try:
            ledgerData[lineId] += qt
        except:
            ledgerData[lineId] = qt
    return ledgerData

def parseLedgerV2(ledger):
    data = {}
    lines = ledger.split("\n")
    raw = 0
    for line in lines:
        if "" != line:
            line = ((line.replace("\xa0", "")).replace("Â", "")).replace("*", "")
            l = line.split("\t")
            try:
                l[1] = l[1].split(" ")[2]
            except:
                l[1] = l[1].replace(" ", "")
            if l[1] == "Ochre":
                l[1] = "Dark Ochre"
            if l[1] in oreNames:
                try:
                    data[l[1]] += int(l[2])
                except:
                    data[l[1]] = int(l[2])
    return data
