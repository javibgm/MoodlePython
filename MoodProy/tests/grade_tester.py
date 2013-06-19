'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.auxiliar import show
from config import info,users

def test_get_definitions(test):
    if test == '0':
        # get grades definitions manually
        print "Required parameters: course module id and area name"
        show(t.get_definitions([raw_input()], raw_input()))
    elif test == '1':
        # get a grade definitions
        show(t.get_definitions(['5'], 'resource'))
    # Errors
    elif test == '2':
        # get a grade definitions
        show(t.get_definitions(['50000'], 'resource'))
    
if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    test_get_definitions(raw_input())