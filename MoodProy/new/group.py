from MoodProy import *

class group(MoodClass):
    def create_groups(self):
    # Creates new groups.
        function = 'core_group_create_groups'
	
	def get_groups(self):
    # Returns group details.
        function = 'core_group_get_groups'
	
	def get_course_groups(self):
    # Returns all groups in specified course.
        function = 'core_group_get_course_groups'
	
	def delete_groups(self):
    # Deletes all specified groups.
        function = 'core_group_delete_groups'
	
	def get_group_members(self):
    # Returns group members.
        function = 'core_group_get_group_members'
	
	def add_group_members(self):
    # Adds group members.
        function = 'core_group_add_group_members'
	
	def delete_group_members(self):
    # Deletes group members.
        function = 'core_group_delete_group_members'
	
	def create_groupings(self):
    # Creates new groupings
        function = 'core_group_create_groupings'
	
	def update_groupings(self):
    # Updates existing groupings
        function = 'core_group_update_groupings'
	
	def get_groupings(self):
    # Returns groupings details.
        function = 'core_group_get_groupings'
	
	def get_course_groupings(self):
    # Returns all groupings in specified course.
        function = 'core_group_get_course_groupings'
	
	def delete_groupings(self):
    # Deletes all specified groupings.
        function = 'core_group_delete_groupings'
	
	def assign_grouping(self):
    # Assing groups from groupings
        function = 'core_group_assign_grouping'
	
	def unassign_grouping(self):
    # Unassing groups from groupings
        function = 'core_group_unassign_grouping'
