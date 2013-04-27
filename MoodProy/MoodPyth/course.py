''' Course class module '''
from MoodPyth import MoodClass
import urllib

class Course(MoodClass):
    '''
    Class with Moodle web services functions that work with courses and categories
    '''
    def course_contents(self, courseid, options=''):
        ''' Get course contents. (options parameter for future uses) '''
        try:
            courseid = int(courseid)
            function = 'core_course_get_contents'
            param = urllib.urlencode({'courseid': courseid})
            return self.connect(function, param)
        except ValueError:
            raise TypeError('courseid must be an integer or a string only with numbers')

    def get_courses(self, courses=''):
        ''' Return course details, all courses details returned if no param specified. '''
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
        ''' Create new courses. '''
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
        ''' Deletes all specified courses. '''
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
        ''' Update courses. '''
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
        ''' Duplicate an existing course (creating a new one) without user data. '''
        function = 'core_course_duplicate_course'
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
        param = urllib.urlencode({'courseid': courseid,'fullname':fullname,'shortname':shortname,'categoryid':categoryid,'visible':visible})
        if(options!='' and type(options)==type([])):
            num = 0
            for option in options:
                param += self.add_optParameters(option, 'options', num, ['name','value'])
                num += 1
        return self.connect(function, param)
        
    
    def import_course(self, importfrom, importto, deletecontent=0, options=''):
        ''' Import course data from a course into another course. Does not include any user data. '''
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
        ''' Return category details. All categories details returned if no parameters specified '''
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

    def create_categories(self,categories):
        ''' Create course categories '''
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
        ''' Update categories. '''
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
        ''' Delete course categories. '''
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
        ''' Deletes all specified module instances. '''
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
        
