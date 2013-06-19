#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service functions test
# Javier Benito García-Mochales

import MoodLib
from config import info

service='moodle_mobile_app'

if __name__ == "__main__":
    """
    Programa principal
    """
    m = MoodLib.MoodLib(info['web'], info['user'], info['pasw'], service)
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
            print MoodLib.show(result)
