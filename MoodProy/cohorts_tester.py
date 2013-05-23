'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import show
from config import info,users


def test_create_cohorts(test):
    if test == '0':
    #  Create 1 cohort manually
        print 'Required parameters: type, value, name, idnumber'
        show(t.create_cohorts([{'type':raw_input(),'value':raw_input(),'name':raw_input(),'idnumber':raw_input()}]))
    elif test == '1':
    # Create 1 cohort
        show(t.create_cohorts([{'type':'id','value':'1','name':'Python Cohort','idnumber':'35','description':'This cohort has been created with the MoodLib python library.'}]))

if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    test_create_cohorts(raw_input())