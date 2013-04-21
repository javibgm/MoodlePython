'''
Created on 24/03/2013

@author: javi
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import info, show

def test_get_files(test):
    if test == '0':
    # Manually get 1 file
        print 'Parameters: contextid, component, filearea, itemid, filepath, filename'
        show(t.get_files(raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input()))
    elif test == '1':
        show(t.get_files(45, 'assignsubmission_file', 'submission_files', 1, '/', ''))
    # Errors
    elif test == '2':
        show(t.get_files(45, 'assignsubmission_file', 'submission_files', 1, '/'))
    elif test == '3':
        show(t.get_files('', 'assignsubmission_file', 'submission_files', 1, '/', ''))
    elif test == '4':
        show(t.get_files(45, 'assignsubmission_file', 'submission_files', 'a', '/', ''))
        

def test_upload_file(test):
    if test == '1':
        show(t.upload_file(5, 'user', 'private', 0, '/', 'FileUploaded', 'FileUploaded'))

def test_down_file():
    print 'Course ID to download file:'
    t.down_file(raw_input())
    
if __name__ == '__main__':
    t = MoodLib(info['web'], 'e1a3bfc5a6066730ce75e83fd0b0e47f') # manager
    # t = MoodLib(info['web'], 'f03f665848ef2a85e3aee8a1db198ac0') # student
    # t = MoodLib(info['web'], '', 'student1', 'StudentP@ss1', info['service'])
    # test_get_files(raw_input())
    test_upload_file(raw_input())
    # test_down_file()