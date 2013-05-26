'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import show
from config import info,users
import time


def test_enrolled_users(test):
    if test == '0':
    #  Get enrolled users from 1 course manually
        print 'Course ID enrolled user get from:'
        show(t.enrolled_users(raw_input()))
    elif test == '1':
    #  Get enrolled users from 1 course manually with options (only full user names and only 2 results)
        print 'Course ID enrolled user get from:'
        show(t.enrolled_users(raw_input(),[{'name':'userfields','value':'fullname'}, {'name':'limitnumber','value':'2'}]))
    elif test == '2':
        show(t.enrolled_users('1',[{'name':'userfields','value':'fullname'}]))
    # Errors
    elif test == '3':
        show(t.enrolled_users('-1'))
    elif test == '4':
        show(t.enrolled_users('a'))
    elif test == '5':
        show(t.enrolled_users('1',[{'name':'userfields','value':'nofield'}]))

def test_get_enrolled_users_with_capability(test):
    if test == '0':
    #  Get all enrolled users' info from 1 course manually with a student capability
        print 'Course ID enrolled users get from:'
        show(t.get_enrolled_users_with_capability([{'courseid':raw_input(),'capabilities':['moodle/blog:view']}]))
    elif test == '1':
    #  Get enrolled users from 1 course with a student capability (options: show only fullname)
        show(t.get_enrolled_users_with_capability([{'courseid':2,'capabilities':['moodle/blog:view']}],[{'name':'userfields','value':'fullname'}]))
    elif test == '2':
    #  Get enrolled users from 1 course with a manager capability (options: show only fullname)
        show(t.get_enrolled_users_with_capability([{'courseid':2,'capabilities':['enrol/authorize:managepayments']}],[{'name':'userfields','value':'fullname'}]))
    #Errors
    elif test == '3':
        show(t.get_enrolled_users_with_capability([{'courseid':2}]))
    elif test == '4':
        show(t.get_enrolled_users_with_capability([{'courseid':-1,'capabilities':['moodle/blog:view']}]))
    elif test == '5':
        show(t.get_enrolled_users_with_capability([{'courseid':2,'capabilities':[]}]))
    elif test == '6':
        show(t.get_enrolled_users_with_capability([{'courseid':2,'capabilities':['moodle/blog:view']}],[{'name':'userfields','value':'nofileds'}]))

def test_get_users_courses():
    #  Get all courses where a user is rolled in manually
    print 'User ID to get courses enrolled in:'
    show(t.get_users_courses(raw_input()))
    # Error: input not an integer

def test_manual_enrol_users(test):
    if test == '0':
    #  Enroll a user in a course with specified role manually
        print 'Role ID to assign user in course, user ID to enroll and course ID where enroll'
        show(t.manual_enrol_users([{'roleid':raw_input(), 'userid':raw_input(), 'courseid':raw_input()}]))
    elif test == '1':
    #  Enroll a user in a course with specified role manually, starts in 30 seconds and ends in 2 mins
        print 'Role ID to assign user in course, user ID to enroll and course ID where enroll'
        show(t.manual_enrol_users([{'roleid':raw_input(), 'userid':raw_input(), 'courseid':raw_input(),'timestart':int(time.time())+30,'timeend':int(time.time())+150}]))
    #  Errors
    elif test == '2':
        show(t.manual_enrol_users([{'roleid':-1, 'userid':4, 'courseid':4}]))
    elif test == '3':
        show(t.manual_enrol_users([{'roleid':1, 'userid':-4, 'courseid':4}]))
    elif test == '4':
        show(t.manual_enrol_users([{'roleid':1, 'userid':4, 'courseid':-4}]))
    elif test == '5':
        show(t.manual_enrol_users([{'userid':4, 'courseid':4}]))
    elif test == '6':
        show(t.manual_enrol_users([{'roleid':1, 'userid':4, 'courseid':4,'suspend':'a'}]))

if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    #test_enrolled_users(raw_input())
    test_get_enrolled_users_with_capability(raw_input())
    #test_get_users_courses()
    #test_manual_enrol_users(raw_input())