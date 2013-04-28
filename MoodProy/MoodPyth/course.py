''' Course class module '''
from MoodPyth import MoodClass
import urllib

class Course(MoodClass):
    '''
    Class with Moodle web services functions that work with courses and categories
    '''
    def course_contents(self, courseid, options=''):
        ''' Get course contents (options parameter for future uses).
        @param courseid: Course identifier.
        @type courseid: Integer. '''
        try:
            courseid = int(courseid)
            function = 'core_course_get_contents'
            param = urllib.urlencode({'courseid': courseid})
            return self.connect(function, param)
        except ValueError:
            raise TypeError('courseid must be an integer or a string only with numbers')

    def get_courses(self, courses=''):
        ''' Return course details, all courses details returned if no parameters specified. 
        @param courses: 0 or more course identifiers.
        @type courses: List of Integers.'''
        if type(courses)!=type([]) and courses!='':
            raise TypeError('Input must be a list of courses')
        function="core_course_get_courses"
        param = ''
        num=0
        for course in courses:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(course, 'options[ids]', num)
            num += 1
        return self.connect(function, param)
    
    def create_courses(self,courses):
        ''' Create new courses.
        @param courses: 1 or more courses.
        @type courses: List of Dictionaries.'''
        if type(courses)!=type([]) or courses==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "fullname", shortname" and ""categoryid"')
        function = 'core_course_create_courses'
        param = ''
        num=0
        reqParameters = ['fullname', 'shortname','categoryid']
        optParameters = ['idnumber','summary', 'summaryformat', 'format', 'showgrades', 'newsitems', 'startdate', 'numsections', 'maxbytes']
        optParameters += ['showreports', 'visible', 'hiddensections', 'groupmode', 'groupmodeforce', 'defaultgroupingid', 'enablecompletion']
        optParameters += ['completionstartonenrol', 'completionnotify', 'lang', 'forcetheme']
        for course in courses:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(course, 'courses', num, reqParameters)
            param += self.add_optParameters(course, 'courses', num, optParameters)
            if 'courseformatoptions' in course:
                numformat = 0
                for cfoptions in course['courseformatoptions']:
                    param += self.add_optParameters(cfoptions,'courses['+str(num)+'][courseformatoptions]',numformat,['name','value'])
                    numformat += 1
            num += 1
        return self.connect(function, param)

    def delete_courses(self, courses):
        ''' Deletes all specified courses.
        @param courses: 1 or more course identifiers.
        @type courses: List of Integers.'''
        if type(courses)!=type([]) or courses==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 course id')
        function = 'core_course_delete_courses'
        param = ''
        num=0
        for courseids in courses:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(courseids, 'courseids', num)
            num += 1
        return self.connect(function, param)

    def update_courses(self, courses):
        ''' Update courses. 
        @param courses: 1 or more courses.
        @type courses: List of Dictionaries.'''
        if type(courses)!=type([]) or courses==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "id"')
        function = 'core_course_update_courses'
        param = ''
        num=0
        reqParameters = ['id']
        optParameters = ['fullname', 'shortname','categoryid','idnumber','summary', 'summaryformat', 'format', 'showgrades']
        optParameters += ['newsitems', 'startdate', 'numsections', 'maxbytes']
        optParameters += ['showreports', 'visible', 'hiddensections', 'groupmode', 'groupmodeforce', 'defaultgroupingid', 'enablecompletion']
        optParameters += ['completionstartonenrol', 'completionnotify', 'lang', 'forcetheme']
        for course in courses:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(course, 'courses', num, reqParameters)
            param += self.add_optParameters(course, 'courses', num, optParameters)
            if 'courseformatoptions' in course:
                numformat = 0
                for cfoptions in course['courseformatoptions']:
                    param += self.add_optParameters(cfoptions,'courses['+str(num)+'][courseformatoptions]',numformat,['name','value'])
                    numformat += 1
            num += 1
        return self.connect(function, param)
    
    def duplicate_course(self, courseid, fullname, shortname, categoryid, visible=1,options=''):
        ''' Duplicate an existing course (creating a new one) without user data.
        @param courseid: course to duplicate id.
        @type courseid: Integer.
        @param fullname: duplicated course full name.
        @type fullname: String.
        @param shortname: duplicated course short name.
        @type shortname: String.
        @param categoryid: duplicated course category parent identifier.
        @type categoryid: Integre
        @param visible: duplicated course visible, default to yes(1).
        @type visible: Integer 0(No) or 1(Yes)
        @param options: duplicating options. Required keys: 'key','value'.
        
        The 'key' value is the backup option name. Expected keys (value format) are:
            - "activities" (int) Include course activites (default to 1 that is equal to yes).
            - "blocks" (int) Include course blocks (default to 1 that is equal to yes).
            - "filters" (int) Include course filters  (default to 1 that is equal to yes).
            - "users" (int) Include users (default to 0 that is equal to no).
            - "role_assignments" (int) Include role assignments  (default to 0 that is equal to no).
            - "comments" (int) Include user comments  (default to 0 that is equal to no).
            - "completion_information" (int) Include user course completion information  (default to 0 that is equal to no).
            - "logs" (int) Include course logs  (default to 0 that is equal to no).
            - "histories" (int) Include histories  (default to 0 that is equal to no).
        The 'value' key value is a string with the value for the option 1 (yes) or 0 (no).
        @type options: List of Dictionaries. '''
        try:
            courseid = int(courseid)
        except ValueError:
            raise TypeError('courseid must be an integer or a string only with numbers')
        if (type(fullname)!=str):
            raise TypeError('fullname must be a string')
        if (type(shortname)!=str):
            raise TypeError('shortname must be a string')
        try:
            categoryid = int(categoryid)
        except ValueError:
            raise TypeError('categoryid must be an integer or a string only with numbers')
        function = 'core_course_duplicate_course'
        param = urllib.urlencode({'courseid': courseid,'fullname':fullname,'shortname':shortname,'categoryid':categoryid,'visible':visible})
        if(options!='' and type(options)==type([])):
            num = 0
            for option in options:
                param += self.add_optParameters(option, 'options', num, ['name','value'])
                num += 1
        return self.connect(function, param)
        
    
    def import_course(self, importfrom, importto, deletecontent=0, options=''):
        ''' Import course data from a course into another course. Does not include any user data. 
        @param importfrom: the identifier of the course we are importing from.
        @type importfrom: Integer.  
        @param importto: the identifier of the course we are importing to.
        @type importto: Integer.  
        @param deletecontent: whether to delete the course content where we are importing to (default to 0 = No).
        @type deletecontent: Integer 1 (yes) or 0 (no).
        @param options: Importing options. Required keys: 'key','value'.
        
        The 'key' value is the backup option name. Expected keys (value format) are:
            - "activities" (int) Include course activites (default to 1 that is equal to yes).
            - "blocks" (int) Include course blocks (default to 1 that is equal to yes).
            - "filters" (int) Include course filters  (default to 1 that is equal to yes).
        The 'value' key value is a string with the value for the option 1 (yes) or 0 (no).
        @type options: List of Dictionaries.'''
        function = 'core_course_import_course'
        try:
            importfrom = int(importfrom)
            importto = int(importto)
        except ValueError:
            raise TypeError('importfrom and importto must be integers or strings only with numbers')
        param = urllib.urlencode({'importfrom': importfrom,'importto':importto,'deletecontent':deletecontent})
        if(options!='' and type(options)==type([])):
            num = 0
            for option in options:
                param += self.add_optParameters(option, 'options', num, ['name','value'])
                num += 1
        return self.connect(function, param)
        

    def get_categories(self, criteria='', addsubcategories=1):
        ''' Return category details. All categories details returned if no parameters specified.
        @param criteria: Criteria to filter categories. Required keys: 'key','value'.
        
        The 'key' value is the category column to search. Expected keys (value format) are:
            - "id" (int) the category id.
            - "name" (string) the category name.
            - "parent" (int) the parent category id.
            - "idnumber" (string) category idnumber - user must have 'moodle/category:manage' to search on idnumber.
            - "visible" (int) whether the returned categories must be visible or hidden. If the key is not passed, then the function return all categories that the user can see.
                - user must have 'moodle/category:manage' or 'moodle/category:viewhiddencategories' to search on visible
            - "theme" (string) only return the categories having this theme
                - user must have 'moodle/category:manage' to search on theme
        The 'value' key value is a string with the value to match.
        @type criteria: List of Dictionaries.
        @param addsubcategories: return the sub categories infos (1 - default) otherwise only the category info (0).
        @type addsubcategories: Integer 1 (yes) or 0 (no). '''
        # list=[{'key':'value'},{...},...]
        # key = "id"(int) | "name"(string) | "parent"(int) | "idnumber"(string) | "visible" (int) | "theme" (string)'''
        if type(criteria)!=type([]) and criteria!='':
            raise TypeError('Input must be a list of dictionaries with {key:value} structure')
        function = 'core_course_get_categories'
        param = ''
        num=0
        reqParameters = ['key', 'value']
        for criterion in criteria:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(criterion, 'criteria', num, reqParameters)
            num += 1
        if addsubcategories==0:
            param += '&' + urllib.urlencode({'addsubcategories': str(addsubcategories)})
        return self.connect(function, param)

    def create_categories(self, categories):
        ''' Create course categories. 
        @param categories: 1 or more categories.
        @type categories: List of Dictionaries.'''
        # name = string, parent = int | idnumber = string | description = string | descriptionformat = int | theme = string'''
        if type(categories)!=type([]) or categories==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "name"')
        function = 'core_course_create_categories'
        param = ''
        num=0
        reqParameters = ['name']
        optParameters = ['parent','idnumber','description','descriptionformat','theme']
        for category in categories:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(category, 'categories', num, reqParameters)
            param += self.add_optParameters(category, 'categories', num, optParameters)
            num += 1
        return self.connect(function, param)

    def update_categories(self, categories):
        ''' Update categories. 
        @param categories: 1 or more categories.
        @type categories: List of Dictionaries. '''
        if type(categories)!=type([]) or categories==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "id"')
        function = 'core_course_update_categories'
        param = ''
        num=0
        reqParameters = ['id']
        optParameters = ['name','parent','idnumber','description','descriptionformat','theme']
        for category in categories:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(category, 'categories', num, reqParameters)
            param += self.add_optParameters(category, 'categories', num, optParameters)
            num += 1
        return self.connect(function, param)

    def delete_categories(self, categories):
        ''' Delete course categories. 
        @param categories: 1 or more categories.
        @type categories: List of Dictionaries.'''
        if type(categories)!=type([]) or categories==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "id"')
        function = 'core_course_delete_categories'
        param = ''
        num=0
        reqParameters = ['id']
        optParameters = ['newparent','recursive']
        for category in categories:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(category, 'categories', num, reqParameters)
            param += self.add_optParameters(category, 'categories', num, optParameters)
            num += 1
        return self.connect(function, param)

    def delete_modules(self, modules):
        ''' Deletes all specified module instances. 
        @param modules: 1 or more module identifiers.
        @type modules: List of Integers.'''
        if type(modules)!=type([]) or modules==[]:
            raise TypeError('Input must be a list of integers')
        function = 'core_course_delete_modules'
        param = ''
        num=0
        for cmids in modules:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(cmids, 'cmids', num)
            num += 1
        return self.connect(function, param)
        
