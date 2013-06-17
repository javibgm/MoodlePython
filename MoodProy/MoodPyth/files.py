''' Files class module '''
from MoodPyth import MoodClass
import urllib

class Files(MoodClass):
    '''
    Class with Moodle web services functions that work with files.
    '''
    def get_files(self, contextid, component, filearea, itemid, filepath, filename, modified=''):
        ''' Browse moodle files. Do not download any content. 
        @param contextid: context identifier.
        @type contextid: Integer
        @param component: component.
        @type component: String
        @param filearea: file area. 
        @type filearea: String
        @param itemid: item identifier.
        @type itemid: Integer
        @param filepath: file path.
        @type filepath: String
        @param filename: file name.
        @type filename: String
        @param modified: timestamp to return files changed after this time (Default to "").
        @type modified: Integer
        '''
        function="core_files_get_files"
        param = urllib.urlencode({'contextid': contextid, 'component':component, 'filearea':filearea, 'itemid':itemid, 'filepath':filepath, 'filename':filename})
        if modified!='':
            param += '&' + urllib.urlencode({'modified':modified})
        return self.connect(function, param)

    def upload_file(self, path, moodlepath):
        ''' Uploads a file to the user's private files area.
        @param path: file path to be uploaded.
        @type path: Integer
        @param moodlepath: moodle private files area path. It must start and end with the "/" character.
        @type moodlepath: Integer
        @raise IOError: if file specified in path parameter do not exists or cannot be readable.
        '''
        import requests
        url = self.conn + '/moodle/webservice/upload.php' + '?' + urllib.urlencode({'token':self.token,'filepath':moodlepath})
        files = {'file': open(path, 'rb')}
        response = requests.post(url, files=files).json()
        print response
        try:
            raise ValueError('Moodle exception: moodlefilesexception\n Message: ' + response['error'])
        except (TypeError, KeyError):
            pass
        return response
    
    def download_file(self, relativepath):
        ''' Download a file using its URL with web services.
        @param relativepath: file URL to be downloaded.
        @type relativepath: String
        @raise IOError: if file specified in path parameter do not exists or cannot be readable.
        '''
        import requests
        url = self.conn + '/moodle/webservice/pluginfile.php' + relativepath + '?' + urllib.urlencode({'token':self.token})
        #files = {'file': open(path, 'rb')}
        response = requests.post(url).text
        print response
        try:
            raise ValueError('Moodle exception: moodlefilesexception\n Message: ' + response['error'])
        except (TypeError, KeyError):
            pass
        return response