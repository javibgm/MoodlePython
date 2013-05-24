''' Files class module '''
from MoodPyth.course import Course
import urllib, urllib2, json, pycurl

class Files(Course):
    '''
    Class with Moodle web services functions that work with files.
    '''
    def get_files(self, contextid, component, filearea, itemid, filepath, filename, modified=''):
        ''' Browse moodle files. Do not download any content. 
        @param contextid: context identifier.
        @type contextid: Integer.
        @param component: component.
        @type component: String.
        @param filearea: file area. 
        @type filearea: String.
        @param itemid: item identifier.
        @type itemid: Integer.
        @param filepath: file path.
        @type filepath: String.
        @param filename: file name.
        @type filename: String.
        @param modified: timestamp to return files changed after this time (Default to "").
        @type modified: Integer. '''
        function="core_files_get_files"
        param = urllib.urlencode({'contextid': contextid, 'component':component, 'filearea':filearea, 'itemid':itemid, 'filepath':filepath, 'filename':filename})
        if modified!='':
            param += '&' + urllib.urlencode({'modified':modified})
        return self.connect(function, param)

    def upload_file(self, contextid, component, filearea, itemid, filepath, filename, filecontent):
        ''' Upload a file to moodle. 
        @param contextid: context identifier.
        @type contextid: Integer.
        @param component: component.
        @type component: String.
        @param filearea: file area. 
        @type filearea: String.
        @param itemid: item identifier.
        @type itemid: Integer.
        @param filepath: file path.
        @type filepath: String.
        @param filename: file name.
        @type filename: String.
        @param filecontent: file content.
        @type filecontent: String. '''
        function = 'core_files_upload'
        param = urllib.urlencode({'contextid': contextid, 'component':component, 'filearea':filearea,
                                  'itemid':itemid, 'filepath':filepath, 'filename':filename, 'filecontent':filecontent})
        return self.connect(function, param)

    def upload_file2(self, path, moodlepath):
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
        #use requests library
    
    def down_file(self, courseid):
        ''' Downloads course's resources via console. Shows course's resources and downloads the selected file. '''
        def show_course_contents(res):
            ''' Auxiliar function to download files. Shows course contents and returns resource items in a dictionary. '''
            # The dicctionary has this structure:
            # Dic = {index : [filename, fileurl]}
            files = {}
            index = 1
            for area in res:
                print area['name']
                for dic in area['modules']:
                    print '  Name: ' + dic['name'] + '\tid: ' + str(dic['id']) + '\tmodname: ' + str(dic['modname'])
                    try:
                        for content in dic['contents']:
                            if str(content['type'])=='file':
                                print (str(index) + '.' + str(content['filename']) + ': ' + str(content['fileurl']) +
                                '\t Type: ' + str(content['type']))
                                files[str(index)] = [str(content['filename']), str(content['fileurl']).split('?')[0]]
                                index = index + 1
                            else:
                                print ('   ' + str(content['filename']) + ': ' + str(content['fileurl']) +
                                '\t Type: ' + str(content['type']))
                    except KeyError:
                        None
            return files
        files = show_course_contents(self.course_contents(courseid))
        print 'Input: file index'
        fileindex = raw_input()
        try:
            print 'Selected file: ' + files[fileindex][0]
            f = open(files[fileindex][0], 'w')
            url = files[fileindex][1] + '?token=' + self.token
            print url
            response = urllib2.urlopen(url)
            f.write(response.read())
            f.close()
            print response.getcode()
        except KeyError:
            print 'File not found. Operation cancelled.'
