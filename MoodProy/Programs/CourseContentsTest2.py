'''
Created on 07/06/2013

@author: javi
'''
from MoodPyth.MoodLib import MoodLib

if __name__ == '__main__':
    url = 'http://adry3000.dyndns.org/'     # initializes constructor parameters
    token = 'f03f665848ef2a85e3aee8a1db198ac0'
    t = MoodLib(url, token)         # class constructor
    contents = t.get_contents(2)    # get contents form the course which identifier is 2
    for section in contents:        # go through course sections
        if 'modules' in section:
            for module in section['modules']:   # go through section modules
                if 'contents' in module:
                    for content in module['contents']:  # go through module contents
                        if str(content['type'])=='file':    # if the content is a file
                            print content['filename']       # its name is printed