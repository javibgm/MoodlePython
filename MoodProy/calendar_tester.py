'''
Created on 24/03/2013

@author: javi
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import info, show


def test_create_calendar_events(test):
    if test == '0':
    #  Create 1 event manually for the user
        print 'Event name to create:'
        show(t.create_calendar_events([{'name':raw_input()}]))
    elif test == '1':
    # Create 1 event with all parameters for a course
        show(t.create_calendar_events([{'name':'Python advanced event',
                                        'description':'Event created with Moodle python library',
                                        'format':'0',
                                        'courseid':'2',
                                        'groupid':'0',
                                        'repeats':'3',
                                        'eventtype':'course',
                                        'timestart':'1367532868',
                                        'timeduration':'240',
                                        'visible':'1',
                                        'sequence':'1'}]))
    elif test == '2':
    # Create 1 event with all parameters for the entire site (courseid=1)
        show(t.create_calendar_events([{'name':'Python event: closing site',
                                        'description':'This moodle site will be close for maintenance operations',
                                        'courseid':'1',
                                        'repeats':'2',
                                        'eventtype':'site',
                                        'timeduration':60*60*24,
                                        'visible':'1'}]))
    # Warnings: execute test 2 or 3 with student user
    # Errors
    elif test == '3':
        show(t.create_calendar_events({'name':'Python advanced'}))
    elif test == '4':
        show(t.create_calendar_events([{'name':'Python event: error',
                                        'repeats':'a'}]))
    elif test == '5':
        show(t.create_calendar_events([{'name':'Python event: error',
                                        'timestart':'a'}]))
    elif test == '6':
        show(t.create_calendar_events([{'name':'Python event: error',
                                        'timeduration':'a'}]))
    elif test == '7':
        show(t.create_calendar_events([{'name':'Python event: error',
                                        'visible':'a'}]))

def test_delete_calendar_events(test):
    if test == '0':
    # Manually delete 1 event
        print 'Event ID to delete:'
        show(t.delete_calendar_events([{'eventid':raw_input(),'repeat':0}]))
    elif test == '1':
    # Manually delete 1 event series
        print 'Event ID to delete with series(repeated event):'
        show(t.delete_calendar_events([{'eventid':raw_input(),'repeat':1}]))
    # Errors:
    #  try to delete a global event with student user
    elif test == '2':
        show(t.delete_calendar_events([1]))
    elif test == '3':
        show(t.delete_calendar_events([{'eventid':1}]))
    elif test == '4':
        show(t.delete_calendar_events([{'eventid':1,'repeat':2}]))
    elif test == '5':
        show(t.delete_calendar_events([{'eventid':-1,'repeat':0}]))

def test_get_calendar_events(test):
    if test == '0':
    # Manually show 1 event
        print 'Event ID to search:'
        show(t.get_calendar_events([raw_input()],userevents=0,siteevents=0))
    elif test == '1':
    # Manually show events from 1 course
        print 'Course ID to search events:'
        show(t.get_calendar_events(courseids=[raw_input()],userevents=0,siteevents=0))
    elif test == '2':
    # Manually show events from 1 group
        print 'Group ID to search events:'
        show(t.get_calendar_events(groupids=[raw_input()],userevents=0,siteevents=0))
    elif test == '3':
    # Get user events (only those created with MoodLib)
        show(t.get_calendar_events(siteevents=0))
    elif test == '4':
    # Get global site events (only those created with MoodLib)
        show(t.get_calendar_events(userevents=0))
    elif test == '5':
    # Get user and global events in a time range even if are hidden
        timestr = t.get_calendar_events()['events'][0]['timestart']
        timend = int(t.get_calendar_events()['events'][0]['timestart'])+10000
        show(t.get_calendar_events(timestart=timestr,timeend=timend, ignorehidden=0))
    # Errors
    elif test == '6':
        show(t.get_calendar_events(['a']))
    elif test == '7':
        show(t.get_calendar_events(courseids=['a']))
    elif test == '8':
        show(t.get_calendar_events(groupids=['a']))
    elif test == '9':
        show(t.get_calendar_events(timestart='a'))
    elif test == '10':
        show(t.get_calendar_events(timeend='a'))
    
if __name__ == '__main__':
    # t = MoodLib(info['web'], 'e1a3bfc5a6066730ce75e83fd0b0e47f') # manager
    t = MoodLib(info['web'], 'f03f665848ef2a85e3aee8a1db198ac0') # student
    # t = MoodLib(info['web'], '', 'student1', 'StudentP@ss1', info['service'])
    # test_create_calendar_events(raw_input())
    # test_delete_calendar_events(raw_input())
    # test_get_calendar_events(raw_input())