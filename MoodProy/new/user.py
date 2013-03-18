from MoodProy import *

class user(MoodClass):

    def get_users_by_id(self, param):
    # Get users by id
        function = 'core_user_get_users_by_id'
        if param == '':
            print 'Incorrect input parameters'
            return None
        else:
            param = urllib.urlencode({'userids[0]': param})
        return self.connect(function, param)
    
    def create_users(self):
    # Create users.
        function = 'core_user_create_users'
	
	def get_course_user_profiles(self):
    # Get course user profiles (each of the profils matching a course id and a user id)
        function = 'core_user_get_course_user_profiles'
	
	def delete_users(self):
    # Delete users
        function = 'core_user_delete_users'
	
	def update_users(self):
    # Update users
        function = 'core_user_update_users'
	
	def get_enrolled_users_with_capability(self):
    # For each course and capability specified, return a list of the users that are enrolled in the course and have that capability
        function = 'core_enrol_get_enrolled_users_with_capability'
	
	def get_enrolled_users(self):
    # Get enrolled users by course id.
        function = 'core_enrol_get_enrolled_users'
	
	def get_users_courses(self):
    # Get the list of courses where a user is enrolled in
        function = 'core_enrol_get_users_courses'
    
    def get_users(self):
    # search for users matching the parameters
        function = 'core_user_get_users'
	
	def users_by_field(self):
    # Retrieve users information for a specified unique field - If you want to do a user search, use core_user_get_users()
        function = 'core_user_get_users_by_field'
