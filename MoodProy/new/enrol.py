from MoodProy import *

class enrol(MoodClass):
    def get_enrolled_users_with_capability(self):
    # For each course and capability specified, return a list of the users that are enrolled in the course and have that capability
        function = 'core_enrol_get_enrolled_users_with_capability'
	
	def enrolled_users(self, param):
    # Get users enrolled in a course
        function="core_enrol_get_enrolled_users"
        if param == '':
            print 'Incorrect input parameters'
            return None
        else:
            param = urllib.urlencode({'courseid': param})
        return self.connect(function, param)

    def get_users_courses(self):
    # Get the list of courses where a user is enrolled in
        function = 'core_enrol_get_users_courses'
    
    def manual_enrol_users(self):
    # Manual enrol users
        function = 'enrol_manual_enrol_users'
