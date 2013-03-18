"""
from MoodProy.aux import *
"""
def _tabulate(tab):
# return the number of tabulations indicated in a string
    buf = ''
    for tab in range(tab):
        buf += "\t"
    return buf

def _showt(data, tab):
# Recursive function that returns printable JSON converted to python string
    buf = ''
    if (type(data)==type({})):
        buf += "{"
        for a in data.keys():
            buf += _tabulate(tab)
            buf += str(a) + ": " + _showt(data[a], tab+1)
        buf += "}"
    elif (type(data)==type([])):
        buf += "[\n"
        for a in data:
            buf += _showt(a, tab)
        buf += _tabulate(tab)
        buf += "]" + "\n"
    else:
        buf += str(data) + "\n"
    return buf

def show(data):
# Prints JSON converted to tabulated python data
    print _showt(data,0)
