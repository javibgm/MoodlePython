'''
Created on 24/03/2013

@author: javi
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import *
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

def test_MoodLib():
    show(t.get_site_info())

def test_get_courses(test):
    if test == '1':
        show(t.get_courses())
    elif test == '2':
        show(t.get_courses([2, 4]))
    # Errors
    elif test == '3':
        show(t.get_courses(2))
    elif test == '4':
        show(t.get_courses('24'))
    elif test == '5':
        show(t.get_courses([2, 'a']))

def test_course_contents(test):
    if test == '1':
        show(t.course_contents('2'))
    elif test == '2':
        show(t.course_contents(2))
    # Errors
    elif test == '3':
        show(t.course_contents('a'))
    elif test == '4':
        show(t.course_contents(255))
    elif test == '5':
        show(t.course_contents(2546453415))
    

if __name__ == '__main__':
    t = MoodLib(info['web'], '0458ea98862eecc3eef61dd776ffbdf2')
    # t = MoodLib(info['web'], '', info['user'], info['pasw'], info['service'])
    # test_MoodLib()
    # test_get_courses(raw_input())
    # test_course_contents(raw_input())