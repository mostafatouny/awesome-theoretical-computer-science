def getDepth(d):
    if isinstance(d, dict):
        return 1 + (max(map(getDepth, d.values())) if d else 0)
    return 0

###

def convKeyRef(header, prevRef):
    keyRef = header.lower()
    keyRef = keyRef.replace(' ', '_')
    keyRef = keyRef.replace('/', '')
    keyRef = keyRef.replace('&', '')
    keyRef = keyRef.replace(',', '')
    return prevRef + keyRef

###

# for ToC
def parseToCitem(key, keyRef):
    return "[" + key + "](#" + keyRef + ")"

# for Con
def parseConItem(lev, key, keyRef):
    return "  "*lev + "#"*(lev+1) + " " + key +"<a name="+keyRef+"></a>"