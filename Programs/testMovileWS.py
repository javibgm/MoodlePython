#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service functions test
# Javier Benito García-Mochales

import MoodLib

"""
user="admin"
pasw="AdminP@ss1"

user="manager1"
pasw="ManagerP@ss1"

user="student1"
pasw="StudentP@ss1"
"""

info = {
    'web': 'adry3000.dyndns.org',
    'user': 'student1',
    'pasw': 'StudentP@ss1',
    'token': '',
    'service': 'moodle_mobile_app'
}

if __name__ == "__main__":
    """
    Programa principal
    """
    #m = MoodLib.MoodLib(info['web'],'badbc023c9e4e6a048098a89e1485f66')
    m = MoodLib.MoodLib(info['web'])
    m.create_token(info['user'],info['pasw'],info['service'])
    print m.get_token()
    function = ''
    while(function!='0'):
        print 'Select operation: 2 course contents/ 8 get component strings/ 0(exit)'
        function = raw_input()
        result = None
        if function=="0":
            m.close
            result = "Exiting..."
        elif function == "2":
            print "Input course ID: "
            result = m.course_contents(raw_input())
        elif function == "8":
            print "Input: component"
            result = m.get_component_strings(raw_input())
        else:
            print "Incorrect input, gettin all courses"
            result = m.get_courses()
        if function !="0":
            print MoodLib.show(result,0)
