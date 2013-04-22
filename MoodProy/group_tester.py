'''
Created on 24/03/2013

@author: javi
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import info, show

def test_add_group_members(test):
    if test == '0':
    # Add a member to a group manually
        print 'Required parameters: Group ID, User ID'
        show(t.get_forum_discussions([{'groupid':raw_input(),'userid':raw_input()}]))

def test_assign_grouping(test):
    if test == '0':
    # Assign a group from a grouping manually
        print 'Required parameters: Grouping ID, Group ID'
        show(t.get_forums_by_courses([{'groupid':raw_input(),'groupid':raw_input()}]))
    
if __name__ == '__main__':
    t = MoodLib(info['web'], 'e1a3bfc5a6066730ce75e83fd0b0e47f') # manager
    # t = MoodLib(info['web'], 'f03f665848ef2a85e3aee8a1db198ac0') # student
    # t = MoodLib(info['web'], '', 'student1', 'StudentP@ss1', info['service'])
    # test_add_group_members(raw_input())
    # test_assign_grouping(raw_input())