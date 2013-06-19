#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service test functionality with Moodle Demonstration Official Site
# Javier Benito García-Mochales

import sys, urllib, httplib, ast

web = "demo.moodle.net"

user="admin"
pasw="demo"
service="moodle_mobile_app"
function="core_course_get_contents"
param = urllib.urlencode({'courseid': '625'})

if __name__ == "__main__":
    """
    Programa principal
    """
    url="/login/token.php?username=" + user + "&password=" + pasw + "&service=" + service
    conn = httplib.HTTPConnection(web,80)
    conn.request('GET',url)
    response = conn.getresponse()
    token = ast.literal_eval(response.read())['token']
    print 'token: ' + token 
    
    url = '/webservice/rest/server.php?wstoken='+token+"&wsfunction="+function+"&moodlewsrestformat=json"
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}
    conn.request('POST', url, param, headers)
    response = conn.getresponse()
    source = response.read()
    
    print response.status, response.reason
    print source
    
    conn.close()

    
