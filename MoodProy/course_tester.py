'''
Created on 24/03/2013

@author: javi
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import info, show


def test_get_site_info():
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

def test_get_categories(test):
    array = []
    if test == '1':
        array = [{'key': 'id', 'value':'1'}]
    elif test == '2':
        array = [{'key': 'name', 'value':'Miscellaneous'}]
    elif test == '3':
        array = [{'key': 'parent', 'value':'0'}]
    elif test == '4':
        array = [{'key': 'idnumber', 'value':'10'}]
    elif test == '5':
        array = [{'key': 'visible', 'value':'1'}]
    elif test == '6':
        array = [{'key': 'theme', 'value':'None'}]
    # Errors
    elif test == '7':
        array = [{'key': 'id', 'value':'100'}]
    elif test == '8':
        array = [{'key': 'id', 'value':'a'}]
    elif test == '9':
        array = [{'key': 'false_key', 'value':'1'}]
    elif test == '10':
        array = [{'keys': 'id', 'values':'1'}]
    show(t.get_categories(array))

if __name__ == '__main__':
    t = MoodLib(info['web'], '0458ea98862eecc3eef61dd776ffbdf2')
    # t = MoodLib(info['web'], '', info['user'], info['pasw'], info['service'])
    # test_get_site_info()
    # test_get_courses(raw_input())
    # test_course_contents(raw_input())
    test_get_categories(raw_input())