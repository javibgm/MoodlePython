'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.auxiliar import show
from config import info,users

def test_get_files(test):
    if test == '0':
    # Manually get 1 file
        print 'Parameters: contextid, component, filearea, itemid, filepath, filename'
        show(t.get_files(raw_input(), raw_input(), raw_input(), raw_input(), raw_input(), raw_input()))
    elif test == '1':
        show(t.get_files(45,
                         'assignsubmission_file',
                         'submission_files',
                         1,
                         '/',
                         ''))
    # Errors
    elif test == '2':
        show(t.get_files(45, 'assignsubmission_file', 'submission_files', 1, '/'))
    elif test == '3':
        show(t.get_files('', 'assignsubmission_file', 'submission_files', 1, '/', ''))
    elif test == '4':
        show(t.get_files(45, 'assignsubmission_file', 'submission_files', 'a', '/', ''))
        

def test_upload_file():
    # Manually upload the specified file to the main private area folder
    print 'Parameter: file path to upload'
    show(t.upload_file(raw_input(),'1/Testfiles/'))

def test_download_file():
    f = open('TestDownloadFile', 'w')
    f.write(t.download_file('http://adry3000.dyndns.org/moodle/webservice/pluginfile.php' +
                        '/44/mod_resource/content/1/File1?forcedownload=1'))
    # URL obtained from the get contents function in the course module
    f.close()
    
if __name__ == '__main__':
    t = MoodLib(info['web'], users['student']['token'])
    #test_get_files(raw_input())
    #test_upload_file()
    test_download_file()