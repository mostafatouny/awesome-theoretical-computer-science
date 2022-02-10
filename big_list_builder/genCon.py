from module import *

def genCon(data, lev, prevRef):

    # if dict type
    if ( isinstance(data, dict) ):
        # print title, then its subtree
        for key, val in data.items():
            keyRef = convKeyRef(key, prevRef)
            item = parseConItem(lev, key, keyRef)
            print(item)

            genCon(val, lev+1, keyRef+'_')

    # if list of strings
    elif ( isinstance(data, list) ):
        for el in data:
            print("  "*lev + "- " + el)

###

import sys, json

# user's input
fileName = sys.argv[1]

# open json file
f = open(fileName)
# convert to dict
data = json.load(f)

# print table of contents
genCon(data, 0, '')

# close file
f.close()