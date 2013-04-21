"""
    'user': 'admin',
    'pasw': 'AdminP@ss1',
    
    'user': 'manager1',
    'pasw': 'ManagerP@ss1',

    'user': 'student1',
    'pasw': 'StudentP@ss1',
"""

info = {
    'web': 'http://adry3000.dyndns.org',
    'user': 'admin',
    'pasw': 'AdminP@ss1',
    'service': 'ext_ser'
}

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
        buf += _tabulate(tab)
        buf += "{" + "\n"
        for a in data.keys():
            buf += _tabulate(tab)
            buf += str(a) + ": " + _showt(data[a], tab+1)
        buf += _tabulate(tab)
        buf += "}" + "\n"
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
