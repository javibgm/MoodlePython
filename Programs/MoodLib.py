#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service functions library
# Javier Benito García-Mochales

import sys, urllib, urllib2, json

def tabulate(tab):
# return the number of tabulations indicated in a string
    buf = ''
    for tab in range(tab):
        buf += "\t"
    return buf

def showt(data, tab):
# Prints JSON converted to python data tabulated
    buf = ''
    if (type(data)==type({})):
        buf += "{"
        for a in data.keys():
            buf += tabulate(tab)
            buf += str(a) + ": " + showt(data[a], tab+1)
        buf += "}"
    elif (type(data)==type([])):
        buf += "[\n"
        for a in data:
            buf += showt(a, tab)
        buf += tabulate(tab)
        buf += "]" + "\n"
    else:
        buf += str(data) + "\n"
    return buf

def show(data):
    return showt(data,0)

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
                print 'Connection response: ' + str(response)
                raise ValueError('Invalid parameters: usename, password or service_short_name')
        return self.token

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

    def get_site_info(self):
    # Get general info about Moodle site
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
        array = ''
        num=0
        if param != '':
            for course in param:
                array += urllib.urlencode({'options[ids]['+str(num)+']': course}) + '&'
                num += 1
        return self.connect(function, array)
    
    def get_files(self, contextid='', component='', filearea='', itemid='', filepath='', filename=''):
    # Browse moodle files
        """
        if (contextid=='' or component=='' or filearea=='' or itemid=='' or filepath=='' or filename==''):
            print 'Incorrect input parameters'
            return None
        """
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
    # Get users enrolled in a course
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
        param = []
        param = urllib.urlencode({})
        if (courseids!=''):
            param.append(('courseids[0]', courseids))
        if (capabilities!=''):
            param.append(('capabilities[0]', capabilities))
        param = urllib.urlencode(param)
        return self.connect(function, param)
    
    def get_component_strings(self, component=''):
    # 
        function="core_get_component_strings"
        param = urllib.urlencode({'component': component})
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
    # Show course resources and download the selected file
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
    
    def assign_get_grades(self, assignmid):
    # Get grades from an assigment
        if (not (type(int(assignmid)) == int)):
            print 'Incorrect input: course ID must be an integer'
            return None
        function="mod_assign_get_grades"
        param = urllib.urlencode({'assignmentids[0]': assignmid})
        return self.connect(function, param)
    
    def get_submmited_files(self):
    # Developing.....
        url = "http://adry3000.dyndns.org/moodle/webservice/pluginfile.php/45/assignsubmission_file/submission_files/1/Student%201%20File" + '?token=' + self.token
