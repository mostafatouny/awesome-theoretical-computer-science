from module import *

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
            header = parseToCitem(key, keyRef)
            print("  "*lev + "- " + header )
            # recursively call beneath items
            genToC(val, printLev, lastOneLine, lev+1, keyRef+'_')

    # case only one list is remaining, and
    #  printing in one line is activated
    # elif (treeDepth == 1 and lastOneLine):
    #     finalItem = "  "*lev + "- "
    #     for key, val in data.items():
    #         keyRef = convKeyRef(key, prevRef)
    #         header = parseToCitem(key, keyRef)
    #         finalItem = finalItem + header + " | "
    #     # remove final additional " | "
    #     finalItem = finalItem[:-3]
    #     print(finalItem)
    #     # no recursive call as this is a leaf list

###

import sys, json

# user's input
fileName = sys.argv[1]
printLev = (int)(sys.argv[2]) # str converted to int
lastOneLine = True if sys.argv[3] == '1' else False # str converted to bool

# open json file
f = open(fileName)
# convert to dict
data = json.load(f)

# print table of contents
genToC(data, printLev, lastOneLine, 0, '')

# close file
f.close()