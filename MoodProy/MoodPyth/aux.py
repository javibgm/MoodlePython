'''
Auxiliar external functions and variables
'''
"""
    'user': 'admin',
    'pasw': 'AdminP@ss1',
    t = MoodLib(info['web'], '0458ea98862eecc3eef61dd776ffbdf2') # admin
    t = MoodLib(info['web'], '', info['user'], info['pasw'], info['service'])
    
    'user': 'manager1',
    'pasw': 'ManagerP@ss1',
    t = MoodLib(info['web'], 'e1a3bfc5a6066730ce75e83fd0b0e47f') # manager
    t = MoodLib(info['web'], '', 'manager1', 'ManagerP@ss1', info['service'])

    'user': 'student1',
    'pasw': 'StudentP@ss1',
    t = MoodLib(info['web'], 'f03f665848ef2a85e3aee8a1db198ac0') # student
    t = MoodLib(info['web'], '', 'student1', 'StudentP@ss1', info['service'])
"""

info = {
    'web': 'http://adry3000.dyndns.org',
    'user': 'admin',
    'pasw': 'AdminP@ss1',
    'service': 'ext_ser'
}

def _tabulate(tab):
    ''' Returns the number of tabulations indicated in a string '''
    buf = ''
    for tab in range(tab):
        buf += "\t"
    return buf

def _showt(data, tab):
    ''' Recursive function that returns printable JSON converted to python string '''
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
    ''' Prints JSON converted to tabulated python data '''
    print _showt(data,0)
