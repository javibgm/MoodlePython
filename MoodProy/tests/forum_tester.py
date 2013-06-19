'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.auxiliar import show
from config import info,users

def test_get_forum_discussions(test):
    if test == '0':
    # Get discussions from 1 forum manually
        print 'Forum ID:'
        show(t.get_forum_discussions([raw_input()]))
    elif test == '1':
        show(t.get_forum_discussions([1,4]))
    # Errors
    elif test == '2':
        show(t.get_forum_discussions(1))
    elif test == '3':
        show(t.get_forum_discussions([-1]))
    elif test == '4':
        show(t.get_forum_discussions(['a']))

def test_get_forums_by_courses(test):
    if test == '0':
    # Get discussions from 1 forum manually
        print 'Course ID:'
        show(t.get_forums_by_courses([raw_input()]))
    elif test == '1':
    # Return all forum instances the user has access
        show(t.get_forums_by_courses())
    elif test == '2':
        show(t.get_forums_by_courses([2]))
    # Errors
    elif test == '3':
        show(t.get_forums_by_courses(2))
    elif test == '4':
        show(t.get_forums_by_courses(['a']))
    elif test == '5':
        show(t.get_forums_by_courses([-1]))
    
if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    #test_get_forum_discussions(raw_input())
    #test_get_forums_by_courses(raw_input())