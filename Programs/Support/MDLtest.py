#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Test of MDL python library use
# https://github.com/zikzakmedia/python-moodle

from moodle import MDL

server = {
    'protocol': 'rest',
    'uri': 'http://demo.moodle.net',
    'token': 'bb03e754ce64098d6896e9318d956bdc',
}

mdl = MDL()
# xmlrpc Connection
#print mdl.conn_rest(server,'moodle_course_get_courses')

"""
Get courses
"""
print mdl.get_courses(server)
