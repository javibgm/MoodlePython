'''
Created on 24/03/2013

@author: javi
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import info, show


def test_get_site_info():
    show(t.get_site_info())

def test_get_courses(test):
    if test == '0':
    # Manually show 1 course
        print 'Course ID to show:'
        show(t.get_courses([raw_input()]))
    elif test == '1':
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
    # Manually show 1 course content 
        print 'Course ID to show contents:'
        show(t.course_contents(raw_input()))
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
    if test=='3':
    # In this case, we dont get subcategories info
        show(t.get_categories(array,0))
    else:
        show(t.get_categories(array))

def test_create_categories(test):
    array = []
    if test == '1':
        array = [{'name': 'Python Category', 'idnumber':'1', 'description':'Category created with MoodPyth'}]
    elif test == '2':
        array=[{'name': 'Python Category', 'idnumber':'2', 'description':'Category created with MoodPyth','parent':'1','descriptionformat':'0'}]
    # Errors
    elif test == '3':
        array = [{'idnumber':'1'}]
    # Error: try to create 2 categories with the same idnumber -> execute 2 times test 1
    show(t.create_categories(array))

def test_create_courses(test):
    array=[]
    if test=='1':
        array = [{'fullname':'Python course','shortname':'PythCourse','categoryid':'1'}]
    elif test =='2':
        array = [{'fullname':'Python course1','shortname':'PythCourse1','categoryid':'1'},{'fullname':'Python course2','shortname':'PythCourse2','categoryid':'1'}]
    elif test =='3':
        array = [{'fullname':'Python course','shortname':'PythCourse','categoryid':'1', 'courseformatoptions':[{'name':'numsections','value':'10'},{'name':'hiddensections','value':'0'},{'name':'coursedisplay','value':'0'}]}]
    # Errors: try to create 2 categories with the same idnumber -> execute 2 times test 1
    elif test =='4':
        array = [{'shortname':'PythCourse','categoryid':'1'}]
    elif test =='5':
    # Add a course in a non-existent category
        array = [{'fullname':'Python course','shortname':'PythCourse','categoryid':'100001'}]
    show(t.create_courses(array))

def test_delete_courses(test):
    array=[]
    if test=='0':
    # Delete manually 1 course
        print 'Course ID to delete:'
        array=[raw_input()]
    # Errors
    elif test=='1':
        array = [-1]
    elif test=='2':
        array = ['a']
    show(t.delete_courses(array))

def test_update_courses(test):
    array=[]
    if test=='1':
        array =[{'id':'2','fullname':'Course 1'}]
    show(t.update_courses(array))
    
if __name__ == '__main__':
    t = MoodLib(info['web'], '0458ea98862eecc3eef61dd776ffbdf2')
    # t = MoodLib(info['web'], '', info['user'], info['pasw'], info['service'])
    # test_get_site_info()
    # test_get_courses(raw_input())
    # test_course_contents(raw_input())
    # test_get_categories(raw_input())
    # test_create_categories(raw_input())
    # test_create_courses(raw_input())
    # test_delete_courses(raw_input())
    # test_update_courses(raw_input())