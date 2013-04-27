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
        show(t.add_group_members([{'groupid':raw_input(),'userid':raw_input()}]))

def test_assign_grouping(test):
    if test == '0':
    # Assign a group from a grouping manually
        print 'Required parameters: Grouping ID, Group ID'
        show(t.assign_grouping([{'groupingid':raw_input(),'groupid':raw_input()}]))

def test_create_groupings(test):
    if test == '0':
    # Create a grouping in a course manually
        print 'Required parameters: Course ID'
        show(t.create_groupings([{'courseid':raw_input(),'name':'Python Grouping', 'description':'Test grouping created with Python library'}]))

def test_create_groups(test):
    if test == '0':
    # Create a group in a course manually
        print 'Required parameters: Course ID'
        show(t.create_groups([{'courseid':raw_input(),'name':'Python Group', 'description':'Test group created with Python library'}]))

def test_delete_group_members(test):
    if test == '0':
    # Remove a user from a group manually
        print 'Required parameters: Group ID, User ID'
        show(t.delete_group_members([{'groupid':raw_input(), 'userid':raw_input()}]))

def test_delete_groupings(test):
    if test == '0':
    # Remove a grouping manually
        print 'Required parameters: Grouping ID'
        show(t.delete_groupings([raw_input()]))

def test_delete_groups(test):
    if test == '0':
    # Remove a group manually
        print 'Required parameters: Group ID'
        show(t.delete_groups([raw_input()]))
        
def test_get_course_groupings(test):
    if test == '0':
        # Get groupings from a course manually
        print 'Required parameters: Course ID'
        show(t.get_course_groupings(raw_input()))
        
def test_get_course_groups(test):
    if test == '0':
    # Remove a group manually
        print 'Required parameters: Course ID'
        show(t.get_course_groups(raw_input()))

def test_get_group_members(test):
    if test == '0':
    # Get members of a group manually
        print 'Required parameters: Group ID'
        show(t.get_group_members([raw_input()]))

def test_get_groupings(test):
    if test == '0':
    # Get a grouping's details manually
        print 'Required parameters: Grouping ID'
        show(t.get_groupings([raw_input()]))

def test_get_groups(test):
    if test == '0':
    # Get a group's details manually
        print 'Required parameters: Group ID'
        show(t.get_groups([raw_input()]))

if __name__ == '__main__':
    t = MoodLib(info['web'], 'e1a3bfc5a6066730ce75e83fd0b0e47f') # manager
    #t = MoodLib(info['web'], 'f03f665848ef2a85e3aee8a1db198ac0') # student
    #t = MoodLib(info['web'], '', 'student1', 'StudentP@ss1', info['service'])
    #est_add_group_members(raw_input())
    #test_assign_grouping(raw_input())
    #test_create_groupings(raw_input())
    #test_create_groups(raw_input())
    #test_delete_group_members(raw_input())
    #test_delete_groupings(raw_input())
    #test_get_course_groupings(raw_input())
    #est_get_course_groups(raw_input())
    #test_delete_groupings(raw_input())
    #test_get_course_groupings(raw_input())
    #test_get_course_groups(raw_input())
    #test_get_group_members(raw_input())
    #test_get_groupings(raw_input())
    #test_get_groups(raw_input())