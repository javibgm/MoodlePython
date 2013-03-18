from MoodProy import *

class course(MoodClass):
    def course_contents(self, courseid, options=''):
    # Get course contents (options parameter for future uses)
        try:
            courseid = int(courseid)
            function = 'core_course_get_contents'
            param = urllib.urlencode({'courseid': courseid})
            return self.connect(function, param)
        except ValueError:
            raise ValueError('courseid must be an integer or a string with only numbers')

    def get_courses(self, param=''):
    # Return course details, all courses details returned if no param specified
        function="core_course_get_courses"
        array = ''
        num=0
        if type(param)!=type([]) and param!='':
            raise TypeError('Input must be a list of courses')
        for course in param:
            array += urllib.urlencode({'options[ids]['+str(num)+']': course}) + '&'
            num += 1
        return self.connect(function, array)
    
    def create_courses(self):
    # Create new courses
        function = 'core_course_create_courses'

    def delete_courses(self):
    # Deletes all specified courses
        function = 'core_course_delete_courses'

    def update_courses(self):
    # Update courses
        function = 'core_course_update_courses'
    
    def duplicate_course(self):
    # Duplicate an existing course (creating a new one) without user data
        function = 'core_course_duplicate_course'

    def get_categories(self):
    # Return category details
        function = 'core_course_get_categories'

    def create_categories(self):
    # Create course categories
        function = 'core_course_create_categories'

    def update_categories(self):
    # Update categories
        function = 'core_course_update_categories'

    def delete_categories(self):
    # Delete course categories
        function = 'core_course_delete_categories'

    def import_course(self):
    # Import course data from a course into another course. Does not include any user data.
        function = 'core_course_import_course'

    def delete_modules(self):
    # Deletes all specified module instances
        function = 'core_course_delete_modules'
