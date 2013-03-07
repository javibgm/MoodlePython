#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service functions test
# Javier Benito García-Mochales

import MoodLib

"""
    'user': 'admin',
    'pasw': 'AdminP@ss1',
    
    'user': 'manager1',
    'pasw': 'ManagerP@ss1',

    'user': 'student1',
    'pasw': 'StudentP@ss1',
"""
info = {
    'web': 'http://adry3000.dyndns.org',
    'user': 'student1',
    'pasw': 'StudentP@ss1',
    'service': 'ext_ser'
}

if __name__ == "__main__":
    """
    Programa principal
    """
    #m = MoodLib.MoodLib(info['web'], '', '', '')
    m = MoodLib.MoodLib(info['web'], info['user'], info['pasw'], info['service'])
    print m.get_token()
    function = ''
    while(function!='0'):
        print 'Select operation: 1 site info / 2 course contents/ 3 get files/ 4 get courses/ 5 get user/ 6 enrolled users/ 7 get assigments/ 8 get component strings/ 9 download file / 10 mod_assign_get_grades / 0(exit)'
        function = raw_input()
        result = None
        if function=="0":
            m.close
            result = "Exiting..."
        elif function == "1":
            result = m.get_site_info()
        elif function == "2":
            print "Input course ID: "
            result = m.course_contents(raw_input())
        elif function == "3":
            print "Input: context id, component, file area, item id, file path, file name"
            result = m.get_files(raw_input(),raw_input(),raw_input(),raw_input(),raw_input(),raw_input())
        elif function == "4":
            print "Input course ID: "
            result = m.get_courses(raw_input())
        elif function == "5":
            print "Input user ID: "
            result = m.get_user(raw_input())
        elif function == "6":
            print "Input course ID: "
            result = m.enrolled_users(raw_input())
        elif function == "7":
            print "Input: course ID, capabilities"
            result = m.get_assigments(raw_input(), raw_input())
        elif function == "8":
            print "Input: component"
            result = m.get_component_strings(raw_input())
        elif function == "9":
            print "Input: course ID"
            result = m.down_file(raw_input())
        elif function == "10":
            print "Input assigment ID: "
            result = m.assign_get_grades(raw_input())
        else:
            print "Incorrect input, gettin all courses"
            result = m.get_courses()
        if function !="0":
            print MoodLib.show(result,0)
