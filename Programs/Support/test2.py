#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service test functionality with personal Moodle
# Javier Benito García-Mochales

import sys, urllib, httplib, ast

web = "adry3000.dyndns.org"

user="admin"
pasw="AdminP@ss1"
service="moodle_mobile_app"
function="core_course_get_contents"
param = urllib.urlencode({'courseid': '2'})

if __name__ == "__main__":
    """
    Programa principal
    """
    url="/moodle/login/token.php?username=" + user + "&password=" + pasw + "&service=" + service
    conn = httplib.HTTPConnection(web,80)
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

    
