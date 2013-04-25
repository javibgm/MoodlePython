# MoodPyth 
# 
# Copyright (C) 2013 Edward Loper 
# Author: Javier Benito Garcia-Mochales <javibgm@hotmail.com>
# URL: <https://github.com/javibgm/MoodlePython> 
  
'''
Moodle Web Service Python library. This library contains
functions to use each one of Moodle version 2.5 web services 
functions. The library is separated in modules and these contains
classes with some web services functions depending of its functionality
(course module contains Course class and do course functions: create courses
delete courses, etc)
All classes inherits from MoodClass and MoodLib class inherit from all classes
so every function of the library can be used from MoodLib.
'''
import sys, urllib, urllib2, json

class MoodClass():
    '''
    Main Moodle python class. It contains common functions
    used in all subclasses like do a request to Moodle or
    do strings with Moodle's request format. It also has a
    function to get the authorization token of a specified
    user and password to the specified web service.
    '''
    def create_token(self, user='', pasw='', service=''):
        '''
        Ask to Moodle the token of the user to the specified
        web service and set its value to the token variable.
        
        @return: User's token of the Moodle's web service.
        @raise ValueError: if any of the parameters provided are
        incorrect or does not exists in Moodle's site.
        @param user: Moodle's user name
        @type user: String
        @param pasw: Moodle's user password
        @type pasw: String
        @param service: the Moodle's web service to use
        @type service: String
        '''
        if(user=='' or pasw=='' or service==''):
            raise ValueError('Parameters necesary: user, password, service_short_name')
        url= self.conn + "/moodle/login/token.php?username=" + user + "&password=" + pasw + "&service=" + service
        response = urllib2.urlopen(url)
        response = json.load(response)
        try:
            self.token = response['token']
        except KeyError:
            print 'Connection response: ' + str(response)
            raise ValueError('Incorrect parameters: usename, password or service_short_name')
        return self.token

    def __init__(self, web, token='', user='', pasw='', service=''):
        ''' Creates the connection with Moodle.
        
        You can directly set your token with the 'token' parameter
        (use __init__('webURL','tokenvalue')) or give user name,
        password and web service to obtain the token from Moodle
        (use __init__('webURL', user='username',pasw='password',
        service='webservice')).
        
        @param web: Moodle's site URL
        @type web: String 
        @param token: Moodle's web service token
        @type token: String
        @param user: Moodle's user name
        @type user: String
        @param pasw: Moodle's user password
        @type pasw: String
        @param service: the Moodle's web service to use
        @type service: String '''
        self.conn = web #: URL where moodle's site is
        self.token = token #: User's token of a web service
        if (self.token==''):
            self.token = self.create_token(user, pasw, service)

    def set_token(self, token):
        ''' Sets the token value '''
        self.token = token

    def get_token(self):
        ''' Returns the token value.
        @return: token value. '''
        return self.token

    def connect(self, function, param):
        '''
        POST to Moodle the function and parameters specified
        and returns the response in JSON format.
         @return: Moodle's answer in JSON format.
         @raise ValueError: if an error happens and Moodle can not
         process the petition. The problem is specified in the exception  
         '''
        url = self.conn + '/moodle/webservice/rest/server.php?wstoken='+self.token+"&wsfunction="+function+"&moodlewsrestformat=json"
        req = urllib2.Request(url, param)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        req.add_header("Accept", "application/json")
        response = urllib2.urlopen(req)
        source = json.load(response)
        print response.getcode()
        try:
            raise ValueError('Moodle exception:' + source['errorcode'] + '\n Message: ' + source['message'])
        except (TypeError, KeyError):
            pass
        return source
    
    def check_reqParameters(self, item, paramnames):
        ''' 
        Auxiliary function: checks if all required parameters
        are in the dictionary and prints missing parameters
        
        @return: True if all paramnames are in item. False otherwise.
        @param paramnames: required parameters
        @type paramnames: List of String
        @param item: parameters values
        @type item: Dictionary
        '''
        check = True
        notfound = ''
        for paramname in paramnames:
            check = check and (paramname in item)
            if not (paramname in item):
                notfound += paramname + ' '
        if (not check):
            print 'Required parameters not found: ' + notfound
        return check
    
    def add_reqParameters(self, item, itemname, num, paramnames=''):
        '''
        Auxiliary function: adds required function parameters.
        Moodle's requests have usually this structure:
        
        course[0][id]=3 --> itemname[num][paramname]=item[paramname]
        
        This function gets the parameters from inputs and 
        returns a string with all parameters formatted like this.
        If no paramnames value is provided a string with format
        course[0]=3 is returned.
        
        @raise TypeError: if a required parameter from paramnames
        is not in item dictionary.
        @return: Moodle's request string with provided parameters
        @param item: parameters values with paramnames keys
        @type item: Dictionary or String
        @param itemname: common parameter name
        @type itemname: String
        @param num: request number
        @type num: Integer
        @param paramnames: list of parameters names(Strings)
        @type paramnames: List of String or None
        '''
        param = ''
        paramnum = 0
        try:
            if(paramnames!=''):        # if we have more than 1 required parameter in a dictionary
                for paramname in paramnames:    # this generate this string structure: itemname[num][paramname]=item[paramname]
                    if paramnum != 0:   # add a & if is not the first parameter
                        param += '&'
                    param += urllib.urlencode({itemname + '['+str(num)+'][' + paramname + ']': item[paramname]})
                    paramnum += 1
            elif (paramnames==''):  # this generate this string structure: itemname[num]=item
                param = urllib.urlencode({itemname + '['+str(num)+']': item})
        except:
            raise TypeError('Invalid function parameters')
        return param
    
    def add_optParameters(self, item, itemname, num, paramnames=''):
        ''' 
        Auxiliary function: adds optional function parameters.
        This function gets the parameters from inputs and 
        returns a string with all parameters formatted as a
        Moodle request. This only returns those parameters with
        a value in the item parameter.
        If no paramnames value is provided a string with format
        course[0]=3 is returned.
        
        @return: Moodle's request string with provided parameters
        @param item: parameters values with paramnames keys
        @type item: Dictionary or String
        @param itemname: common parameter name
        @type itemname: String
        @param num: request number
        @type num: Integer
        @param paramnames: list of parameters names(Strings)
        @type paramnames: List of String or None
        '''
        def add_optParameter(self, item, itemname, num, paramname=''):
            param = ''
            if((paramname in item) and (paramname!='')):
                param = '&' + urllib.urlencode({itemname + '['+str(num)+'][' + paramname + ']': item[paramname]})
            elif ((paramname in item) and (paramname=='')):
                param = '&' + urllib.urlencode({itemname + '['+str(num)+']': item})
            return param
        param = ''
        for paramname in paramnames:
            param += self.add_optParameter(item, itemname, num, paramname)
        return param