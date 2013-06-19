'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.auxiliar import show
from config import info,users

def test_block_contacts(test):
    if test == '0':
    # Block a contact manually
        print 'Required parameters: User ID'
        show(t.block_contacts([raw_input()]))

def test_create_contacts(test):
    if test == '0':
    # Add a contact to your contacts list manually
        print 'Required parameters: User ID'
        show(t.create_contacts([raw_input()]))

def test_delete_contacts(test):
    if test == '0':
    # Delete a contact from your contacts list manually
        print 'Required parameters: User ID'
        show(t.delete_contacts([raw_input()]))

def test_get_contacts():
    show(t.get_contacts())

def test_search_contacts(test):
    if test == '0':
    # Search contacts manually
        print 'Required parameters: Search string'
        show(t.search_contacts(raw_input()))

def test_send_instant_messages(test):
    if test == '0':
    # Send a message to a user manually
        print 'Required parameters: User ID, text message'
        show(t.send_instant_messages([{'touserid':raw_input(),
                                       'text':raw_input()}]))

def test_unblock_contacts(test):
    if test == '0':
    # Unlock a contact manually
        print 'Required parameters: User ID'
        show(t.unblock_contacts([raw_input()]))

if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    #test_block_contacts(raw_input())
    #test_create_contacts(raw_input())
    #test_delete_contacts(raw_input())
    #test_get_contacts()
    #test_search_contacts(raw_input())
    #test_send_instant_messages(raw_input())
    #test_unblock_contacts(raw_input())