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
            raise TypeError('courseid must be an integer or a string with only numbers')

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
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 course id')
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
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "id"')
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
    
    def duplicate_course(self, courseid, fullname, shortname, categoryid, visible=1,options=''):
    # Duplicate an existing course (creating a new one) without user data
        function = 'core_course_duplicate_course'
        try:
            courseid = int(courseid)
        except ValueError:
            raise TypeError('courseid must be an integer or a string with only numbers')
        if (type(fullname)!=str):
            raise TypeError('fullname must be a string')
        if (type(shortname)!=str):
            raise TypeError('shortname must be a string')
        try:
            categoryid = int(categoryid)
        except ValueError:
            raise TypeError('categoryid must be an integer or a string with only numbers')
        param = urllib.urlencode({'courseid': courseid,'fullname':fullname,'shortname':shortname,'categoryid':categoryid,'visible':visible})
        if(options!='' and type(options)==type([])):
            num = 0
            for option in options:
                param += self.add_optParameters(option, 'options', num, ['name','value'])
                num += 1
        return self.connect(function, param)
        
    
    def import_course(self, importfrom, importto, deletecontent=0, options=''):
    # Import course data from a course into another course. Does not include any user data.
        function = 'core_course_import_course'
        try:
            importfrom = int(importfrom)
            importto = int(importto)
        except ValueError:
            raise TypeError('importfrom and importto must be integers or strings with only numbers')
        param = urllib.urlencode({'importfrom': importfrom,'importto':importto,'deletecontent':deletecontent})
        if(options!='' and type(options)==type([])):
            num = 0
            for option in options:
                param += self.add_optParameters(option, 'options', num, ['name','value'])
                num += 1
        return self.connect(function, param)
        

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

    def update_categories(self, array):
    # Update categories
        function = 'core_course_update_categories'
        param = ''
        num=0
        reqParameters = ['id']
        optParameters = ['name','parent','idnumber','description','descriptionformat','theme']
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "id"')
        for categories in array:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(categories, 'categories', num, reqParameters)
            param += self.add_optParameters(categories, 'categories', num, optParameters)
            num += 1
        return self.connect(function, param)

    def delete_categories(self, array):
    # Delete course categories
        function = 'core_course_delete_categories'
        param = ''
        num=0
        reqParameters = ['id']
        optParameters = ['newparent','recursive']
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "id"')
        for categories in array:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(categories, 'categories', num, reqParameters)
            param += self.add_optParameters(categories, 'categories', num, optParameters)
            num += 1
        return self.connect(function, param)

    def delete_modules(self, array):
    # Deletes all specified module instances
        function = 'core_course_delete_modules'
        param = ''
        num=0
        if type(array)!=type([]) or array==[]:
            raise TypeError('Input must be a list of integers')
        for cmids in array:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(cmids, 'cmids', num)
            num += 1
        return self.connect(function, param)
        
