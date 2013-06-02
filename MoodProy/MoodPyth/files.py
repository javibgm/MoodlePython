''' Files class module '''
from MoodPyth import MoodClass
import urllib, urllib2

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
        ''' Uploads a file to the users private files area.
        @param path: file path to be uploaded.
        @type path: Integer
        @param moodlepath: moodle private files area path. It must start and end with the "/" character.
        @type moodlepath: Integer
        @raise IOError: if file specified in path parameter do not exists or cannot be readable.
        '''
        '''
        param = 'file_box='+'@'+path+'&'+urllib.urlencode({'filepath':moodlepath,'token':self.token})
        print url, param
        req = urllib2.Request(url, param)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        req.add_header("Accept", "application/json")
        response = urllib2.urlopen(req)
        source = json.load(response)
        try:
            raise ValueError('Moodle exception:' + source['errorcode'] + '\n Message: ' + source['message'])
        except (TypeError, KeyError):
            pass
        return source
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