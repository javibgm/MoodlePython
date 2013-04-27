''' Group class module '''
from MoodPyth import MoodClass
import urllib

class group(MoodClass):
    '''
    Class with Moodle web services functions that work with groups
    '''
    def add_group_members(self, members):
        ''' Adds group members. '''
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
        ''' Assing groups from groupings. '''
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
        ''' Creates new groupings. '''
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
        ''' Creates new groups. '''
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

    def delete_group_members(self,members):
        ''' Deletes group members. '''
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
        ''' Deletes all specified groupings. '''
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
        ''' Deletes all specified groups. '''
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
        ''' Returns all groupings in specified course. '''
        try:
            courseid = int(courseid)
            function = 'core_group_get_course_groupings'
            param = urllib.urlencode({'courseid': courseid})
            return self.connect(function, param)
        except ValueError:
            raise TypeError('courseid must be an integer or a string only with numbers')
    
    def get_course_groups(self, courseid):
        ''' Returns all groups in specified course. '''
        try:
            courseid = int(courseid)
            function = 'core_group_get_course_groups'
            param = urllib.urlencode({'courseid': courseid})
            return self.connect(function, param)
        except ValueError:
            raise TypeError('courseid must be an integer or a string only with numbers')
    
    def get_group_members(self, groupids):
        ''' Returns group members. '''
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
        ''' Returns groupings details. '''
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
        ''' Returns group details. '''
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
    
    def unassign_grouping(self):
        ''' Unassing groups from groupings. '''
        function = 'core_group_unassign_grouping'

    def update_groupings(self):
        ''' Updates existing groupings. '''
        function = 'core_group_update_groupings'