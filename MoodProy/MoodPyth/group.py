from MoodPyth import MoodClass

class group(MoodClass):
    def add_group_members(self, members):
    # Adds group members.
        if type(members)!=type([]) and members!='':
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
    # Assing groups from groupings
        if type(groupings)!=type([]) and groupings!='':
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
    
    def create_groupings(self):
    # Creates new groupings
        function = 'core_group_create_groupings'
        
    def create_groups(self):
    # Creates new groups.
        function = 'core_group_create_groups'
	
    def delete_group_members(self):
    # Deletes group members.
        function = 'core_group_delete_group_members'
        
    def delete_groupings(self):
    # Deletes all specified groupings.
        function = 'core_group_delete_groupings'
        
    def delete_groups(self):
    # Deletes all specified groups.
        function = 'core_group_delete_groups'
    
    def get_course_groupings(self):
    # Returns all groupings in specified course.
        function = 'core_group_get_course_groupings'
    
    def get_course_groups(self):
    # Returns all groups in specified course.
        function = 'core_group_get_course_groups'
    
    def get_group_members(self):
    # Returns group members.
        function = 'core_group_get_group_members'
    
    def get_groupings(self):
    # Returns groupings details.
        function = 'core_group_get_groupings'
    
    def get_groups(self):
    # Returns group details.
        function = 'core_group_get_groups'
    
    def unassign_grouping(self):
    # Unassing groups from groupings
        function = 'core_group_unassign_grouping'

    def update_groupings(self):
    # Updates existing groupings
        function = 'core_group_update_groupings'