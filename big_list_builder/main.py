# assume no lowest level is always list

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
    return prevRef + keyRef

def parseHeader(key, keyRef):
    return "[" + key + "](#" + keyRef + ")"

###

def genToC(data, printLev, lastOneLine, lev, prevRef):
    treeDepth = getDepth(data)
    #print(treeDepth)

    # return if printLev is activated,
    #   and lev exceeded it
    if printLev != -1 and lev > printLev:
        return

    # if not dict type return
    if not ( isinstance(data, dict) ):
        return

    # case nested lists
    if (treeDepth > 1 or not lastOneLine):
        # get key and values out of dictionary
        for key, val in data.items():
            # parse strings and print
            keyRef = convKeyRef(key, prevRef)
            print("  "*lev + "- " + parseHeader(key, prevRef) )
            # recursively call beneath items
            genToC(val, printLev, lastOneLine, lev+1, keyRef+'_')

    # case only one list is remaining, and
    #  printing in one line is activated
    elif (treeDepth == 1 and lastOneLine):
        finalItem = "  "*lev + "- "
        for key, val in data.items():
            keyRef = convKeyRef(key, prevRef)
            header = parseHeader(key, keyRef)
            finalItem = finalItem + header + " | "
        # remove final additional " | "
        finalItem = finalItem[:-3]
        print(finalItem)
        # no recursive call as this is a leaf list


def genCon(data, printLev, lev, prevRef):

    # return if printLev is activated,
    #   and lev exceeded it
    if printLev != -1 and lev > printLev:
        return

    # if dict type
    if ( isinstance(data, dict) ):
        # print title, then its subtree
        for key, val in data.items():
            keyRef = convKeyRef(key, prevRef)
            print("  "*lev + "#"*(lev+1) + " " + key +"<a name="+keyRef+"></a>")

            genCon(val, printLev, lev+1, keyRef+'_')

    # if list of strings
    elif ( isinstance(data, list) ):
        for el in data:
            print("  "*lev + "- " + el)


###


import json

# open json file
f = open('source.json')

# convert to dict
data = json.load(f)


genToC(data, -1, True, 0, '')
#genCon(data, -1, 0, '')

# close file
f.close()