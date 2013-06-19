######################## BEGIN LICENSE BLOCK ########################
# This file is part of MoodPyth library.
#
# MoodPyth library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# MoodPyth library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with MoodPyth.  If not, see <http://www.gnu.org/licenses/>.
######################### END LICENSE BLOCK #########################
# Copyright 2013 Javier Benito Garcia-Mochales
''' Group class module '''
from MoodPyth import MoodClass
import urllib

class Group(MoodClass):
    '''
    Class with Moodle web services functions that work with groups
    '''
    def add_group_members(self, members):
        ''' Adds group members. 
        @param members: group identifiers and user identifiers to add users to groups:
            - groupid (int)   - group record id
            - userid (int)   - user id
        @type members: List of Dictionaries
        @raise TypeError: if members input parameter type is not a list or is an empty list.
        '''
        if type(members)!=type([]) or members==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "groupid" and "userid"')
        function = 'core_group_add_group_members'
        param = ''
        num=0
        reqParameters = ['groupid', 'userid']
        for member in members:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(member, 'members', num, reqParameters)
            num += 1
        return self.connect(function, param)
        
    def assign_grouping(self, groupings):
        ''' Assing groups from groupings. 
        @param groupings: grouping identifiers and group identifiers to assign groups to groupings:
            - groupingid (int)   - grouping record id
            - groupid (int)   - group record id
        @type groupings: List of Dictionaries
        @raise TypeError: if groupings input parameter type is not a list or is an empty list.
        '''
        if type(groupings)!=type([]) or groupings==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "groupingid" and "groupid"')
        function = 'core_group_assign_grouping'
        param = ''
        num=0
        reqParameters = ['groupingid', 'groupid']
        for group in groupings:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(group, 'assignments', num, reqParameters)
            num += 1
        return self.connect(function, param)
    
    def create_groupings(self, groupings):
        ''' Creates new groupings. 
        @param groupings: 1 or more groupings. A grouping has a courseid, a name and a description:
            - courseid (int)   - id of course
            - name (string)   - multilang compatible name, course unique
            - description (string)   - grouping description text
            - descriptionformat (int)  Default to "1" - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @type groupings: List of Dictionaries
        @return: List of Dictionaries. List of grouping created:
            - id (int)   - grouping record id
            - courseid (int)   - id of course
            - name (string)   - multilang compatible name, course unique
            - description (string)   - grouping description text
            - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @raise TypeError: if groupings input parameter type is not a list or is an empty list.
        '''
        if type(groupings)!=type([]) or groupings==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "courseid", "name" and "description"')
        function = 'core_group_create_groupings'
        param = ''
        num=0
        reqParameters = ['courseid', 'name','description']
        optParameters = ['descriptionformat']
        for grouping in groupings:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(grouping, 'groupings', num, reqParameters)
            param += self.add_optParameters(grouping, 'groupings', num, optParameters)
            num += 1
        return self.connect(function, param)
        
    def create_groups(self, groups):
        ''' Creates new groups.
        @param groups: 1 or more groups. A group has a courseid, a name, a description and an enrolment key:
            - courseid (int)   - id of course
            - name (string)   - multilang compatible name, course unique
            - description (string)   - group description text
            - descriptionformat (int)  Default to "1" - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - enrolmentkey (string)  Optional - group enrol secret phrase
        @type groups: List of Dictionaries
        @return: List of Dictionaries. List of groups created:
            - id (int)   - grouping record id
            - courseid (int)   - id of course
            - name (string)   - multilang compatible name, course unique
            - description (string)   - grouping description text
            - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @raise TypeError: if groups input parameter type is not a list or is an empty list.
        '''
        if type(groups)!=type([]) or groups==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "courseid", "name" and "description"')
        function = 'core_group_create_groups'
        param = ''
        num=0
        reqParameters = ['courseid', 'name','description']
        optParameters = ['descriptionformat','enrolmentkey']
        for group in groups:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(group, 'groups', num, reqParameters)
            param += self.add_optParameters(group, 'groups', num, optParameters)
            num += 1
        return self.connect(function, param)

    def delete_group_members(self, members):
        ''' Deletes group members. 
        @param members: group identifiers and user identifiers to remove users from groups:
            - groupid (int)   - group record id
            - userid (int)   - user id
        @type members: List of Dictionaries
        @raise TypeError: if members input parameter type is not a list or is an empty list.
        '''
        if type(members)!=type([]) or members==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "groupid" and "userid"')
        function = 'core_group_delete_group_members'
        param = ''
        num=0
        reqParameters = ['groupid', 'userid']
        for member in members:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(member, 'members', num, reqParameters)
            num += 1
        return self.connect(function, param)

    def delete_groupings(self, groupingids):
        ''' Deletes all specified groupings. 
        @param groupingids: 1 or more grouping identifiers to delete.
        @type groupingids: List of Integer
        @raise TypeError: if groupingids input parameter type is not a list or is an empty list.
        '''
        if type(groupingids)!=type([]) or groupingids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 grouping id')
        function = 'core_group_delete_groupings'
        param = ''
        num=0
        for groupingid in groupingids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(groupingid, 'groupingids', num)
            num += 1
        return self.connect(function, param)

    def delete_groups(self, groupids):
        ''' Deletes all specified groups. 
        @param groupids: 1 or more group identifiers to delete. 
        @type groupids: List of Integer
        @raise TypeError: if groupids input parameter type is not a list or is an empty list.
        '''
        if type(groupids)!=type([]) or groupids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 group id')
        function = 'core_group_delete_groups'
        param = ''
        num=0
        for groupid in groupids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(groupid, 'groupids', num)
            num += 1
        return self.connect(function, param)

    def get_course_groupings(self, courseid):
        ''' Returns all groupings in specified course. 
        @param courseid: course identifier to get its groupings
        @type courseid: Integer
        @return: List of Dictionaries. List of groupings in the specified course:
            - id (int)   - grouping record id
            - courseid (int)   - id of course
            - name (string)   - multilang compatible name, course unique
            - description (string)   - grouping description text
            - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @raise TypeError: if courseid input parameter is not an integer.
        '''
        try:
            courseid = int(courseid)
        except ValueError:
            raise TypeError('courseid must be an integer or a string only with numbers')
        function = 'core_group_get_course_groupings'
        param = urllib.urlencode({'courseid': courseid})
        return self.connect(function, param)
    
    def get_course_groups(self, courseid):
        ''' Returns all groups in specified course. 
        @param courseid: course identifier to get its groups
        @type courseid: Integer
        @return: List of Dictionaries. List of groups in the specified course:
            - id (int)   - group record id
            - courseid (int)   - id of course
            - name (string)   - multilang compatible name, course unique
            - description (string)   - group description text
            - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - enrolmentkey (string)   - group enrol secret phrase
        @raise TypeError: if courseid input parameter is not an integer.
        '''
        try:
            courseid = int(courseid)
        except ValueError:
            raise TypeError('courseid must be an integer or a string only with numbers')
        function = 'core_group_get_course_groups'
        param = urllib.urlencode({'courseid': courseid})
        return self.connect(function, param)
    
    def get_group_members(self, groupids):
        ''' Returns group members.
        @param groupids: 1 or more group identifiers to get their members.
        @type groupids: List of Integer
        @return: List of Dictionaries. List of groupids with their members userids:
            - groupid (int)   - group record id
            - userids (List of Integer) - user id
        @raise TypeError: if groupids input parameter type is not a list or is an empty list.
        '''
        if type(groupids)!=type([]) or groupids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 group id')
        function = 'core_group_get_group_members'
        param = ''
        num=0
        for groupid in groupids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(groupid, 'groupids', num)
            num += 1
        return self.connect(function, param)
    
    def get_groupings(self, groupingids, returngroups=0):
        ''' Returns groupings details. 
        @param groupingids: 1 or more grouping identifiers.
        @type groupingids: List of Integer
        @param returngroups: return associated groups: 1 (yes) or 0 (no = Default).
        @type returngroups: Integer
        @return: List of Dictionaries. Groupings information:
            - id (int)   - grouping record id
            - courseid (int)   - id of course
            - name (string)   - multilang compatible name, course unique
            - description (string)   - grouping description text
            - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - groups (List of Dictionaries) Optional - optional groups:
                - id (int)   - group record id
                - courseid (int)   - id of course
                - name (string)   - multilang compatible name, course unique
                - description (string)   - group description text
                - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
                - enrolmentkey (string)   - group enrol secret phrase
        @raise TypeError: if groupingids input parameter type is not a list or is an empty list.
        '''
        if type(groupingids)!=type([]) or groupingids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 grouping id')
        function = 'core_group_get_groupings'
        param = ''
        num=0
        for groupingid in groupingids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(groupingid, 'groupingids', num)
            num += 1
        if returngroups==1:
            param += '&' + urllib.urlencode({'returngroups': returngroups})
        return self.connect(function, param)

    def get_groups(self, groupids):
        ''' Returns group details. 
        @param groupids: 1 or more group identifiers 
        @type groupids: List of Integer
        @return: List of Dictionaries. Groups information:
            - id (int)   - group record id
            - courseid (int)   - id of course
            - name (string)   - multilang compatible name, course unique
            - description (string)   - group description text
            - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - enrolmentkey (string)   - group enrol secret phrase
        @raise TypeError: if groupids input parameter type is not a list or is an empty list.
        '''
        if type(groupids)!=type([]) or groupids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 group id')
        function = 'core_group_get_groups'
        param = ''
        num=0
        for groupid in groupids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(groupid, 'groupids', num)
            num += 1
        return self.connect(function, param)
    
    def unassign_grouping(self, unassignments):
        ''' Unassing groups from groupings. 
        @param unassignments: grouping identifiers and group identifiers to unassign groups from groupings:
            - groupingid (int)   - grouping record id
            - groupid (int)   - group record id
        @type unassignments: List of Dictionaries
        @raise TypeError: if unassignments input parameter type is not a list or is an empty list.
        '''
        if type(unassignments)!=type([]) or unassignments==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "groupingid" and "groupid"')
        function = 'core_group_unassign_grouping'
        param = ''
        num=0
        reqParameters = ['groupingid', 'groupid']
        for unassignment in unassignments:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(unassignment, 'unassignments', num, reqParameters)
            num += 1
        return self.connect(function, param)

    def update_groupings(self, groupings):
        ''' Updates existing groupings.
        @param groupings: 1 or more groupings. A grouping has a courseid, a name and a description:
            - id (int)   - id of grouping
            - name (string)   - multilang compatible name, course unique
            - description (string)   - grouping description text
            - descriptionformat (int)  Default to "1" - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @type groupings: List of Dictionaries
        @raise TypeError: if groupings input parameter type is not a list or is an empty list.
        '''
        if type(groupings)!=type([]) or groupings==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "id", "name" and "description"')
        function = 'core_group_update_groupings'
        param = ''
        num=0
        reqParameters = ['id', 'name','description']
        optParameters = ['descriptionformat']
        for grouping in groupings:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(grouping, 'groupings', num, reqParameters)
            param += self.add_optParameters(grouping, 'groupings', num, optParameters)
            num += 1
        return self.connect(function, param)
