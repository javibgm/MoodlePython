#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service functions test
# Javier Benito García-Mochales

import sys, urllib, urllib2, json

def tabulate(tab):
# return the number of tabulations indicated in a string
    buf = ''
    for tab in range(tab):
        buf += "\t"
    return buf

def show(data, tab):
# Prints JSON converted to python data tabulated
    buf = ''
    if (type(data)==type({})):
        for a in data.keys():
            buf += tabulate(tab)
            buf += str(a) + ": " + show(data[a], tab+1)
    elif (type(data)==type([])):
        buf += "[\n"
        for a in data:
            buf += show(a, tab)
        buf += tabulate(tab)
        buf += "]" + "\n"
    else:
        buf += str(data) + "\n"
    return buf

class MoodLib:
    def create_token(self, user='', pasw='', service=''):
    # Returns your token, locally or asking to moodle and
    # save it in the token variable
        if (self.token == ''):
            if(user=='' or pasw=='' or service==''):
                raise ValueError('Not token found, parameters necesary: user, password, service_short_name')
            url= self.conn + "/moodle/login/token.php?username=" + user + "&password=" + pasw + "&service=" + service
            response = urllib2.urlopen(url)
            response = json.load(response)
            try:
                self.token = response['token']
            except KeyError:
                raise ValueError('Invalid parameters: usename, password or service_short_name')
        return self.token

    """
    def __init__(self, web, token='', user='', pasw='', service=''):
    # Creates the connection with Moodle
        self.conn = httplib.HTTPConnection(web,80)
        self.token = token
        if (self.token==''):
            self.create_token(user, pasw, service)
        else:
            self.token = token
    """
    def __init__(self, web, user='', pasw='', service=''):
    # Creates the connection with Moodle
        self.conn = web
        self.token = ''
        self.token = self.create_token(user, pasw, service)

    def setoken(self, token):
    # Sets the value of the token
        self.token = token

    def get_token(self):
    # Return token's value
        return self.token

    def connect(self, function, param):
    # POST to Moodle the function and parameters specified
        url = self.conn + '/moodle/webservice/rest/server.php?wstoken='+self.token+"&wsfunction="+function+"&moodlewsrestformat=json"
        req = urllib2.Request(url, param)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        req.add_header("Accept", "application/json")
        response = urllib2.urlopen(req)
        source = json.load(response)
        print response.getcode()
        return source
    
    def close(self):
    # Close the connection with Moodle
        self.conn.close()

    def get_site_info(self):
    # Get generl info about Moodle site
        function="core_webservice_get_site_info"
        return self.connect(function, urllib.urlencode({}))

    def course_contents(self, courseid):
    # Get course contents
        if (not (type(int(courseid)) == int)):
            print 'Incorrect input: course ID must be an integer'
            return None
        function="core_course_get_contents"
        param = urllib.urlencode({'courseid': courseid})
        return self.connect(function, param)

    def get_courses(self, param=''):
    # Return course details, all courses details returned if no param specified
        function="core_course_get_courses"
        if param == '':
            param = {}
        else:
            param = urllib.urlencode({'options[ids][0]': param})
        return self.connect(function, param)
    
    def get_files(self, contextid='', component='', filearea='', itemid='', filepath='', filename=''):
    # Browse moodle files
        if (contextid=='' or component=='' or filearea=='' or itemid=='' or filepath=='' or filename==''):
            print 'Incorrect input parameters'
            return None
        function="core_files_get_files"
        param = urllib.urlencode({'contextid': contextid, 'component':component, 'filearea':filearea, 'itemid':itemid, 'filepath':filepath, 'filename':filename})
        return self.connect(function, param)

    def get_user(self, param):
    # Get users by id
        function="core_user_get_users_by_id"
        if param == '':
            print 'Incorrect input parameters'
            return None
        else:
            param = urllib.urlencode({'userids[0]': param})
        return self.connect(function, param)
    
    def enrolled_users(self, param):
    # Get users enrrolled in a course
        function="core_enrol_get_enrolled_users"
        if param == '':
            print 'Incorrect input parameters'
            return None
        else:
            param = urllib.urlencode({'courseid': param})
        return self.connect(function, param)
    
    
    def get_assigments(self, courseids='', capabilities=''):
    # Get users enrrolled in a course with the specified capabilities
        function="mod_assign_get_assignments"
        param = urllib.urlencode({'courseids[0]': courseids, 'capabilities[0]':capabilities})
        return self.connect(function, param)
    
    def get_component_strings(self, component=''):
    # 
        function="core_get_component_strings"
        param = urllib.urlencode({'component': component})
        return self.connect(function, param)
    
    def show_course_contents(self, res):
    # Shows course contents and returns them in a dictionary
    # The dicctionary has this structure:
    # Dic = {index : [filename, fileurl]}
        files = {}
        index = 1
        for area in res:
            print area['name']
            for dic in area['modules']:
                print str(index) + '.Name: ' + dic['name'] + '\tid: ' + str(dic['id']) + '\tmodname: ' + str(dic['modname'])
                files[str(index)] = [str(dic['name']), str(dic['url'])]
                index = index + 1
                try:
                    for content in dic['contents']:
                        print (str(index) + '. ' + str(content['filename']) + ': ' + str(content['fileurl']) +
                        '\t Type: ' + str(content['type']))
                        files[str(index)] = [str(content['filename']), str(content['fileurl']).split('?')[0]]
                        index = index + 1
                except KeyError:
                    # print 'No contents'
                    None
        return files
    
    def down_file(self, courseid):
    # Show course resources and download the selected files
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
