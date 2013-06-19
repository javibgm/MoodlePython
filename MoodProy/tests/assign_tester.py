'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.auxiliar import show
from config import info,users


def test_get_assigments(test):
    if test == '0':
    #  Search assignments in 1 course without capabilities filter
        print 'Course ID to show assigments:'
        show(t.get_assigments([raw_input()]))
    elif test == '1':
    # Search in all courses where user is enrolled
        show(t.get_assigments())
    elif test == '2':
    # Filter with a student role capability
        show(t.get_assigments([], ['moodle/user:viewdetails']))
    elif test == '3':
    # Filter with a manager role capability
        show(t.get_assigments(capabilities=['enrol/authorize:managepayments']))
    elif test == '4':
        show(t.get_assigments([2],['moodle/user:viewdetails']))
    elif test == '5':
    # Warning: user not enrolled in course
        show(t.get_assigments([-1]))
    elif test == '6':
    # Errors
        show(t.get_assigments('2'))
    elif test == '7':
        show(t.get_assigments([],['moodle/user:falsecapability']))

def test_get_grades(test):
    if test == '0':
    # Manually show 1 assignment grades 
        print 'Assignment ID to show grades:'
        show(t.get_grades([raw_input()]))
    elif test == '1':
        show(t.get_grades(['1']))
    elif test == '2':
        show(t.get_grades([1,8],'1366499369'))
    elif test == '3':
        show(t.get_grades([42101]))
    # Errors
    elif test == '4':
        show(t.get_grades([]))
    elif test == '5':
        show(t.get_grades('1'))
    elif test == '6':
        show(t.get_grades([1],'-a'))

def test_get_submissions(test):
    if test == '0':
    # Manually show 1 assignment submissions 
        print 'Assignment ID to show submissions:'
        show(t.get_submissions([raw_input()]))
    elif test == '1':
        show(t.get_submissions([1]))
    elif test == '2':
        show(t.get_submissions([1],'submitted',1362385052, 1362385052))
    # Errors
    elif test == '3':
        show(t.get_submissions(['a']))
    elif test == '4':
        show(t.get_submissions([1],'submitted','a'))

if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    #test_get_assigments(raw_input())
    #test_get_grades(raw_input())
    #test_get_submissions(raw_input())