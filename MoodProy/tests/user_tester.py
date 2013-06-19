'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.auxiliar import show
from config import info,users

def test_create_users(test):
    if test == '1':
        # Create a test user
        show(t.create_users([{'username':'pythontest',
                           'password':'PythonP@ss1',
                           'firstname':'Python',
                           'lastname':'Test Student',
                           'email':'python@test.com'}]))
    #Errors
    elif test =='2':
        # Try to create a user with an invalid pasword
        show(t.create_users([{'username':'pythontest',
                           'password':'pass',
                           'firstname':'Python',
                           'lastname':'Test Student',
                           'email':'python@test.com'}]))
    elif test =='3':
        # Try to create a user with an invalid email
        show(t.create_users([{'username':'pythontest',
                           'password':'PythonP@ss1',
                           'firstname':'Python',
                           'lastname':'Test Student',
                           'email':'pythontest@t'}]))

def test_update_users():
    # Change a user name
    print 'Required parameters: id of the user to change its name'
    origUser = t.get_users_by_field('id',[raw_input()])[0]
    show(t.update_users([{'id':origUser['id'],
                       'username':'changedname',
                       'firstname':'Changed'}]))
    print "Press enter to restore its original user's name"
    raw_input()
    show(t.update_users([{'id':origUser['id'],
                       'username':origUser['username'],
                       'firstname':origUser['firstname']}]))

def test_delete_users():
    # Change a user name
    print 'Required parameters: id of the user to delete'
    show(t.delete_users([raw_input()]))


def test_get_users(test):
    if test == '0':
        # Manually search users 
        print 'Required parameters: key ("id", "lastname", "firstname", "idnumber", "username", "email" or "auth"), value'
        show(t.get_users([{'key':raw_input(),
                           'value':raw_input()}]))
    elif test == '1':
        # Search the user with the userid = 3
        show(t.get_users([{'key':'id',
                           'value':'3'}]))
    elif test == '2':
        # Search without criteria: return all users and a warning (value field cannot be empty)
        show(t.get_users([{'key':'',
                           'value':'3'}]))
    elif test == '3':
        # Search using '%' character: search all users whose firstname contains an 'a'
        show(t.get_users([{'key':'firstname',
                           'value':'a%'}]))
    #Errors
    elif test == '4':
        show(t.get_users([]))

def test_get_course_user_profiles(test):
    if test == '0':
        # Manually get 1 user profile
        print 'Required parameters: userid, courseid'
        show(t.get_course_user_profiles([{'userid':raw_input(),
                                          'courseid':raw_input()}]))

def test_get_users_by_field(test):
    if test == '0':
        # Manually get users with 1 value
        print 'Required parameters: field (id or idnumber or username or email), value'
        show(t.get_users_by_field(raw_input(), [raw_input()]))
    elif test == '1':
        # Get the user with the userid = 3
        show(t.get_users_by_field('id',['3']))
    elif test == '2':
        # Get the user by its username
        show(t.get_users_by_field('username',['student1']))
    elif test == '3':
        # Try to get a non-existing user
        show(t.get_users_by_field('username',['nouser']))
    #Errors
    elif test == '4':
        # Invalid input parameters
        show(t.get_users_by_field('username',[]))
    elif test == '4':
        # Invalid filed parameters
        show(t.get_users_by_field('nofield',['nouser']))

if __name__ == '__main__':
    t = MoodLib(info['web'], users['admin']['token'])
    #test_create_users(raw_input())
    #test_update_users()
    #test_delete_users()
    #test_get_course_user_profiles(raw_input())
    #test_get_users(raw_input())
    #test_get_users_by_field(raw_input())
    