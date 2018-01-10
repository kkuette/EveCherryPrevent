oreNames = ["Arkonor", "Bistot", "Crokite", "Ochre", "Gneiss", "Spodumain", "Mercoxit"]

def parseLedger(ledger):
    ledgerData = {}
    lines = ledger.splitlines()
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
