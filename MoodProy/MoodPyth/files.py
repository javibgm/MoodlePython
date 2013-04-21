from MoodPyth.course import course
import urllib, urllib2

class files(course):
    def get_files(self, contextid, component, filearea, itemid, filepath, filename, modified=''):
    # Browse moodle files
        function="core_files_get_files"
        param = urllib.urlencode({'contextid': contextid, 'component':component, 'filearea':filearea, 'itemid':itemid, 'filepath':filepath, 'filename':filename})
        if modified!='':
            param += '&' + urllib.urlencode({'modified':modified})
        return self.connect(function, param)

    def upload_file(self, contextid, component, filearea, itemid, filepath, filename, filecontent):
    # Upload a file to moodle
        function = 'core_files_upload'
        param = urllib.urlencode({'contextid': contextid, 'component':component, 'filearea':filearea,
                                  'itemid':itemid, 'filepath':filepath, 'filename':filename, 'filecontent':filecontent})
        print param
        return self.connect(function, param)

    def show_course_contents(self, res):
    # Shows course contents and returns resource items in a dictionary
    # The dicctionary has this structure:
    # Dic = {index : [filename, fileurl]}
        files = {}
        index = 1
        for area in res:
            print area['name']
            for dic in area['modules']:
                """
                print str(index) + '.Name: ' + dic['name'] + '\tid: ' + str(dic['id']) + '\tmodname: ' + str(dic['modname'])
                files[str(index)] = [str(dic['name']), str(dic['url'])]
                index = index + 1
                """
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
                    # print 'No contents'
                    None
        return files
    
    def down_file(self, courseid):
    # Shows course's resources and downloads the selected file
        files = self.show_course_contents(self.course_contents(courseid))
        print 'Input: file index'
        fileindex = raw_input()
        try:
            print 'Archivo seleccionado: ' + files[fileindex][0]
            f = open(files[fileindex][0], 'w')
            url = files[fileindex][1] + '?token=' + self.token
            print url
            response = urllib2.urlopen(url)
            f.write(response.read())
            f.close()
            print response.getcode()
        except KeyError:
            print 'File not found. Operation cancelled.'
    
