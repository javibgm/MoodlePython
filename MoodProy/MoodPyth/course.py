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
            if num!=0:
                param += '&'
            param += self.add_reqParameters(course, 'options[ids]', num)
            num += 1
        return self.connect(function, param)
    
    def create_courses(self,array):
    # Create new courses
        function = 'core_course_create_courses'
        param = ''
        num=0
        reqParameters = ['fullname', 'shortname','categoryid']
        optParameters = ['idnumber','summary', 'summaryformat', 'format', 'showgrades', 'newsitems', 'startdate', 'numsections', 'maxbytes']
        optParameters += ['showreports', 'visible', 'hiddensections', 'groupmode', 'groupmodeforce', 'defaultgroupingid', 'enablecompletion']
        optParameters += ['completionstartonenrol', 'completionnotify', 'lang', 'forcetheme']
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "fullname", shortname" and ""categoryid"')
        for courses in array:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(courses, 'courses', num, reqParameters)
            param += self.add_optParameters(courses, 'courses', num, optParameters)
            if 'courseformatoptions' in courses:
                numformat = 0
                for cfoptions in courses['courseformatoptions']:
                    param += self.add_optParameters(cfoptions,'courses['+str(num)+'][courseformatoptions]',numformat,['name','value'])
                    numformat += 1
            num += 1
        return self.connect(function, param)

    def delete_courses(self, array):
    # Deletes all specified courses
        function = 'core_course_delete_courses'
        param = ''
        num=0
        reqParameters = ['courseids']
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "fullname", shortname" and ""categoryid"')
        for courseids in array:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(courseids, 'courseids', num)
            num += 1
        return self.connect(function, param)

    def update_courses(self, array):
    # Update courses
        function = 'core_course_update_courses'
        param = ''
        num=0
        reqParameters = ['id']
        optParameters = ['fullname', 'shortname','categoryid','idnumber','summary', 'summaryformat', 'format', 'showgrades']
        optParameters += ['newsitems', 'startdate', 'numsections', 'maxbytes']
        optParameters += ['showreports', 'visible', 'hiddensections', 'groupmode', 'groupmodeforce', 'defaultgroupingid', 'enablecompletion']
        optParameters += ['completionstartonenrol', 'completionnotify', 'lang', 'forcetheme']
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "fullname", shortname" and ""categoryid"')
        for courses in array:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(courses, 'courses', num, reqParameters)
            param += self.add_optParameters(courses, 'courses', num, optParameters)
            if 'courseformatoptions' in courses:
                numformat = 0
                for cfoptions in courses['courseformatoptions']:
                    param += self.add_optParameters(cfoptions,'courses['+str(num)+'][courseformatoptions]',numformat,['name','value'])
                    numformat += 1
            num += 1
        return self.connect(function, param)
    
    def duplicate_course(self):
    # Duplicate an existing course (creating a new one) without user data
        function = 'core_course_duplicate_course'
    
    def import_course(self):
    # Import course data from a course into another course. Does not include any user data.
        function = 'core_course_import_course'

    def get_categories(self, array='', addsubcategories=1):
    # Return category details. All categories details returned if no parameters specified 
    # list=[{'key':'value'},{...},...]
        ''' key = "id"(int) | "name"(string) | "parent"(int) | "idnumber"(string) | "visible" (int) | "theme" (string)'''
        function = 'core_course_get_categories'
        param = ''
        num=0
        reqParameters = ['key', 'value']
        if type(array)!=type([]) and array!='':
            raise TypeError('Input must be a list of dictionaries with {key:value} structure')
        for criteria in array:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(criteria, 'criteria', num, reqParameters)
            num += 1
        if addsubcategories==0:
            param += '&' + urllib.urlencode({'addsubcategories': str(addsubcategories)})
        return self.connect(function, param)

    def create_categories(self,array):
    # Create course categories
        ''' name = string, parent = int | idnumber = string | description = string | descriptionformat = int | theme = string'''
        function = 'core_course_create_categories'
        param = ''
        num=0
        reqParameters = ['name']
        optParameters = ['parent','idnumber','description','descriptionformat','theme']
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "name"')
        for categories in array:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(categories, 'categories', num, reqParameters)
            param += self.add_optParameters(categories, 'categories', num, optParameters)
            num += 1
        return self.connect(function, param)

    def update_categories(self):
    # Update categories
        function = 'core_course_update_categories'

    def delete_categories(self):
    # Delete course categories
        function = 'core_course_delete_categories'

    def delete_modules(self):
    # Deletes all specified module instances
        function = 'core_course_delete_modules'
