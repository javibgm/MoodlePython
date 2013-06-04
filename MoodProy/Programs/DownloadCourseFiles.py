'''
Created on 01/06/2013
Copyright (C) 2013 MoodlePython Project
URL: <https://github.com/javibgm/MoodlePython> 
@author: Javier Benito Garcia-Mochales <javibgm@hotmail.com>
Downloads course's resources via console. Shows course's resources and downloads the selected file.
'''
from MoodPyth.MoodLib import MoodLib
from config import info,users
import urllib2

def show_course_contents(res):
    ''' Auxiliar function to download files. Shows course contents and returns resource items in a dictionary. '''
    # The dicctionary has this structure:
    # Dic = {index : [filename, fileurl]}
    files = {}
    index = 1
    for area in res: # for each area returned in the response
        print area['name']  # shows area name
        for dic in area['modules']: # for each module in the area
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
    
if __name__ == '__main__':
    t = MoodLib(info['web'], users['student']['token'])
    print 'Introduce the course ID to download files'
    courseid = raw_input()
    contents = t.course_contents(courseid) # get the contents form the selected course
    files = show_course_contents(contents) # show contents in console and save the downloadable files' names and URLs in an array
    print 'Input: file index'
    fileindex = raw_input()
    try:
        print 'Selected file: ' + files[fileindex][0]
        f = open(files[fileindex][0], 'w')
        url = files[fileindex][1] + '&token=' + t.get_token()
        print url
        response = urllib2.urlopen(url)
        f.write(response.read())
        f.close()
        print response.getcode()
    except KeyError:
        print 'File not found. Operation cancelled.'
