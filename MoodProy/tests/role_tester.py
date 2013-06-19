'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import show
from config import info,users

def test_assign_roles(test):
    if test == '0':
        # Assign a role to a user manually
        print "Required parameters: roleid, userid and contextid"
        show(t.assign_roles([{'roleid': raw_input(),
                              'userid': raw_input(),
                              'contextid': raw_input()}]))
    elif test == '1':
        # Assign a role to a user
        show(t.assign_roles([{'roleid': '2',
                              'userid':'4' ,
                              'contextid': '2'}]))
    # Errors
    elif test == '2':
        # Assign a role to a user in a invalid context
        show(t.assign_roles([{'roleid': '6',    # guest role id
                              'userid':'4' ,    # Any user id
                              'contextid': '1'}]))  # System context
    
def test_unassign_roles(test):
    if test == '0':
        # Unassign a role to a user manually
        print "Required parameters: roleid, userid and contextid"
        show(t.unassign_roles([{'roleid': raw_input(),
                              'userid': raw_input(),
                              'contextid': raw_input()}]))
    elif test == '1':
        #Unassign a role to a user
        show(t.unassign_roles([{'roleid': '2',
                              'userid':'4' ,
                              'contextid': '1'}]))
    
if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    #test_assign_roles(raw_input())
    #test_unassign_roles(raw_input())