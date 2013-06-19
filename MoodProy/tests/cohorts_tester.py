'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import show
from config import info,users

def test_add_cohort_members(test):
    if test == '0':
    #  Adds a user to a cohort manually
        print 'Required parameters: cohorttype("id" or "idnumber"), cohortvalue, usertype("id" or "username"), uservalue'
        show(t.add_cohort_members([{'cohorttype':
                                        {'type':raw_input(),
                                         'value':raw_input()},
                                    'usertype':
                                        {'type':raw_input(),
                                         'value':raw_input()}}
                                   ]))
    elif test == '1':
    # Add a member using user and cohort IDs
        show(t.add_cohort_members([{'cohorttype':
                                        {'type':'id',
                                         'value':'1'},
                                    'usertype':
                                        {'type':'id',
                                         'value':'3'}
                                    }]))
    elif test == '2':
    # Add a member using username and cohort idnumber
        show(t.add_cohort_members([{'cohorttype':
                                        {'type':'idnumber',
                                         'value':'35'},
                                    'usertype':
                                        {'type':'username',
                                         'value':'student1'}
                                    }]))
    elif test == '3':
    # Get a warning because cohort specified do not exist
        show(t.add_cohort_members([{'cohorttype':
                                        {'type':'id',
                                         'value':'1100'},
                                    'usertype':
                                        {'type':'id',
                                         'value':'3'}
                                    }]))

def test_create_cohorts(test):
    if test == '0':
    #  Create 1 cohort manually
        print 'Required parameters: type("id", "idnumber" or "system"), value, name, idnumber'
        show(t.create_cohorts([{'type':raw_input(),
                                'value':raw_input(),
                                'name':raw_input(),
                                'idnumber':raw_input()}]))
    elif test == '1':
    # Create 1 cohort
        show(t.create_cohorts([{'type':'id',
                                'value':'1',
                                'name':'Python Cohort',
                                'idnumber':'35',
                                'description':'This cohort has been created with the MoodLib python library.'}]))

def test_delete_cohort_members():
    print 'Required parameters: cohortid, userid'
    show(t.delete_cohort_members([{'cohortid':raw_input(),
                                   'userid':raw_input()}]))

def test_delete_cohorts():
    print 'Required parameters: cohort id to delete'
    show(t.delete_cohorts([raw_input()]))
    
def test_get_cohort_members():
    print 'Required parameters: cohort id to get its members'
    show(t.get_cohort_members([raw_input()]))
    
def test_get_cohorts():
    print 'Required parameters: cohort id to get its details'
    show(t.get_cohorts([raw_input()]))
    
def test_update_cohorts(test):
    if test == '0':
    #  Create 1 cohort manually
        print 'Required parameters: "id", type("id", "idnumber" or "system"), value, name, idnumber'
        show(t.update_cohorts([{'type':raw_input(),
                                'value':raw_input(),
                                'name':raw_input(),
                                'idnumber':raw_input()}]))
    elif test == '1':
    # Update 1 cohort
        show(t.update_cohorts([{'id':4,
                                'type':'id',
                                'value':'1',
                                'name':'Python Cohort',
                                'idnumber':'35',
                                'description':'This cohort has been created with the MoodLib python library.'}]))
    elif test == '2':
    # Update 1 cohort
        show(t.update_cohorts([{'id':4,
                                'type':'id',
                                'value':'2',
                                'name':'Python Cohort Changed',
                                'idnumber':'36',
                                'description':'This cohort has been changed with the MoodLib python library.'}]))
    elif test == '3':
    # Update 1 cohort
        show(t.update_cohorts([{'id':1,
                                'type':'system',
                                'value':'1',
                                'name':'Cohort1',
                                'idnumber':''}]))
    # Error
    elif test == '4':
        show(t.update_cohorts([{'id':4,
                                'type':'id',
                                'value':'1',
                                'idnumber':'36'}]))

if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    #test_create_cohorts(raw_input())
    #test_add_cohort_members(raw_input())
    #test_delete_cohort_members()
    #test_delete_cohorts()
    #test_get_cohort_members()
    #test_get_cohorts()
    #test_update_cohorts(raw_input())