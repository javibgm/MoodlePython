'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.auxiliar import show
from config import info,users

def test_create_notes(test):
    if test == '0':
        # Create a note manually
        print "Required parameters: userid, publishstate('personal', 'course' or 'site'), courseid and text"
        show(t.create_notes([{'userid': raw_input(),
                              'publishstate': raw_input(),
                              'courseid': raw_input(),
                              'text': raw_input()}]))
    elif test == '1':
        # Create a personal note
        show(t.create_notes([{'userid': '3',
                              'publishstate':'personal' ,
                              'courseid': '2',
                              'text': 'Python library test note'}]))
    elif test == '2':
        # Create a site note
        show(t.create_notes([{'userid': '3',
                              'publishstate':'site',
                              'courseid': '2',
                              'text': 'Python library test note'}]))
    # Errors
    elif test == '3':
        # Create a site note without course id
        show(t.create_notes([{'userid': '3',
                              'publishstate':'site' ,
                              'text': 'Python library test note'}]))
        
def test_delete_notes():
    # Delete a note manually
    print "Required parameters: note id"
    show(t.delete_notes([raw_input()]))
    
def test_get_notes():
    # Get a note manually
    print "Required parameters: note id"
    show(t.get_notes([raw_input()]))

def test_update_notes(test):
    if test == '0':
        # Update a note manually
        print "Required parameters: note id, publishstate('personal', 'course' or 'site') and text"
        show(t.update_notes([{'id': raw_input(),
                              'publishstate': raw_input(),
                              'text': raw_input()}]))
    elif test == '1':
        # Update a personal note
        show(t.update_notes([{'id': 1,
                              'publishstate': 'personal',
                              'text': 'Python note changed'}]))
    elif test == '2':
        # Update a personal note to a course
        show(t.update_notes([{'id': 1,
                              'publishstate': 'course',
                              'text': 'Python note changed to a course note'}]))


if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    #test_create_notes(raw_input())
    #test_get_notes()
    #test_update_notes(raw_input())
    #test_delete_notes()