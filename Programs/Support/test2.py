#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service test functionality with personal Moodle
# Javier Benito García-Mochales

import sys, urllib, httplib, ast
from config import info

service="moodle_mobile_app"
function="core_course_get_contents"
param = urllib.urlencode({'courseid': '2'})

if __name__ == "__main__":
    """
    Programa principal
    """
    url="/moodle/login/token.php?username=" + info['user'] + "&password=" + info['pasw'] + "&service=" + service
    conn = httplib.HTTPConnection(info['web'],80)
    conn.request('GET',url)
    response = conn.getresponse()
    token = ast.literal_eval(response.read())['token']
    print 'token: ' + token
    
    url = '/moodle/webservice/rest/server.php?wstoken='+token+"&wsfunction="+function+"&moodlewsrestformat=json"
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}
    conn.request('POST', url, param, headers)
    response = conn.getresponse()
    source = response.read()
    
    print response.status, response.reason
    print source
    
    conn.close()

    
