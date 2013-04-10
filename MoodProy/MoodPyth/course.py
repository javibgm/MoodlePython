from MoodPyth import MoodClass
import urllib

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

    def get_courses(self, courses=''):
    # Return course details, all courses details returned if no param specified
        function="core_course_get_courses"
        param = ''
        num=0
        if type(courses)!=type([]) and courses!='':
            raise TypeError('Input must be a list of courses')
        for course in courses:
            param += urllib.urlencode({'options[ids]['+str(num)+']': course}) + '&'
            num += 1
        return self.connect(function, param)
    
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

    def get_categories(self, array=''):
    # Return category details. All categories details returned if no parameters specified 
    # list=[{'key':'value'},{...},...]
        ''' key = "id" (int) the category id
                "name" (string) the category name
                "parent" (int) the parent category id
                "idnumber" (string) category idnumber - user must have 'moodle/category:manage' to search on idnumber
                "visible" (int) whether the returned categories must be visible or hidden. If the key is not passed, then the function return all categories that the user can see. - user must have 'moodle/category:manage' or 'moodle/category:viewhiddencategories' to search on visible
                "theme" (string) only return the categories having this theme - user must have 'moodle/category:manage' to search on theme
        '''
        function = 'core_course_get_categories'
        param = ''
        num=0
        if type(array)!=type([]) and array!='':
            raise TypeError('Input must be a list of dictionaries with {key:value} structure')
        for criteria in array:
            param += urllib.urlencode({'criteria['+str(num)+'][key]': criteria['key'], 'criteria['+str(num)+'][value]': criteria['value']}) + '&'
            num += 1
        return self.connect(function, param)

    def create_categories(self,array):
    # Create course categories
        ''' name string   //new category name
            parent int  Default to "0" //the parent category id inside which the new category will be created - set to 0 for a root category
            idnumber string  Optional //the new category idnumber
            description string  Optional //the new category description
            descriptionformat int  Default to "1" //description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            theme string  Optional //the new category theme. This option must be enabled on moodle '''
        function = 'core_course_create_categories'
        param = ''
        num=0
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "name"')
        for categories in array:
            param += urllib.urlencode({'categories['+str(num)+'][name]': categories['name']}) + '&'
            if('parent' in categories):
                param += urllib.urlencode({'categories['+str(num)+'][parent]': categories['parent']}) + '&'
            if('idnumber' in categories):
                param += urllib.urlencode({'categories['+str(num)+'][idnumber]': categories['idnumber']}) + '&'
            if('description' in categories):
                param += urllib.urlencode({'categories['+str(num)+'][description]': categories['description']}) + '&'
            if('descriptionformat' in categories):
                param += urllib.urlencode({'categories['+str(num)+'][descriptionformat]': categories['descriptionformat']}) + '&'
            if('theme' in categories):
                param += urllib.urlencode({'categories['+str(num)+'][theme]': categories['theme']}) + '&'
            num += 1
        return self.connect(function, param)

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
