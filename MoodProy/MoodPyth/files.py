######################## BEGIN LICENSE BLOCK ########################
# This file is part of MoodPyth library.
#
# MoodPyth library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# MoodPyth library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with MoodPyth.  If not, see <http://www.gnu.org/licenses/>.
######################### END LICENSE BLOCK #########################
# Copyright 2013 Javier Benito Garcia-Mochales
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
        ''' Download a text plain file using its URL with web services.
        @param relativepath: file URL to be downloaded.
        @type relativepath: String
        @return: downloaded file data
        @raise ValueError: if URL specified has not the appropriate format to download a file.
        '''
        import requests
        try:
            url = self.conn + '/moodle/webservice/pluginfile.php' + relativepath.split('pluginfile.php')[1].split('?')[0] + '?' + urllib.urlencode({'token':self.token})
        except IndexError:
            raise TypeError('URL provided has not web services format')
        try:
            url = url + '&' + relativepath.split('?')[1]
        except IndexError:
            pass
        response = requests.post(url).content
        try:
            raise ValueError('Moodle exception: moodlefilesexception\n Message: ' + response['error'])
        except (TypeError, KeyError):
            pass
        return response
