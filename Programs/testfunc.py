#!/usr/bin/python
# -*- coding: UTF-8 -*-

# External web service functions test
# Authon: Javier Benito García-Mochales

import MoodLib as MoodLib
import MoodLib as Moodaux
from config import info

class tester:
    def __init__(self):
        #m = MoodLib.MoodLib(info['web'], '', '', '')
        self.m = MoodLib.MoodLib(info['web'], info['user'], info['pasw'], info['service'])
        print self.m.get_token()
    
    def functions(self):
        print "Available functions:"
        print " get_site_info(): Get general info about Moodle site"
        print " course_contents(ID: int): Get contents of one course"
        print " get_courses(IDS: [int]): Return course details, all courses details returned if no IDs specified"
    
    def get_site_info(self):
        Moodaux.show(self.m.get_site_info())

    def course_contents(self, ID):
        Moodaux.show(self.m.course_contents(ID))
    
    def get_courses(self, IDs):
        Moodaux.show(self.m.get_courses(IDs))
    
    def get_files(self):
        print "Input: context id, component, file area, item id, file path, file name"
        Moodaux.show(self.m.get_files(raw_input(),raw_input(),raw_input(),raw_input(),raw_input(),raw_input()))
    
    def get_user(self):
        print "Input user ID: "
        Moodaux.show(self.m.get_users_by_id(raw_input()))
    
    def enrolled_users(self):
        print "Input course ID: "
        Moodaux.show(self.m.enrolled_users(raw_input()))
    
    def get_assigments(self):
        print "Input: course ID, capabilities"
        Moodaux.show(self.m.get_assigments(raw_input(), raw_input()))
    
    def get_component_strings(self):
        print "Input: component"
        Moodaux.show(self.m.get_component_strings(raw_input()))
    
    def down_file(self):
        print "Input: course ID"
        Moodaux.show(self.m.down_file(raw_input()))
    
    def assign_get_grades(self):
        print "Input assigment ID: "
        Moodaux.show(self.m.get_grades(raw_input()))
    

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
            result = m.get_users_by_id(raw_input())
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
            result = m.get_grades(raw_input())
        else:
            print "Incorrect input, gettin all courses"
            result = m.get_courses()
        if function !="0":
            print Moodaux.show(result)
