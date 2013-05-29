from MoodPyth import MoodClass
import urllib

class User(MoodClass):
    def get_users_by_id(self):
    # Get users by id
        function = 'core_user_get_users_by_id'
    
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
    
    def get_users(self):
    # search for users matching the parameters
        function = 'core_user_get_users'
    
    def get_users_by_field(self):
    # Retrieve users information for a specified unique field - If you want to do a user search, use core_user_get_users()
        function = 'core_user_get_users_by_field'
