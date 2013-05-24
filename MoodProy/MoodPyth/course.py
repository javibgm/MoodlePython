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
        @type courseid: Integer
        @param options: 0 or more user course options (Not used yet, might be used in later version):
            - name (string) - option name
            - value (string) - the value of the option, this param is personally validated in the external function
        @type options: List of Dictionary
        @return: List of Dictionary - list of sections:
            - id int - Section ID
            - name (string) - Section name
            - visible int  Optional - is the section visible
            - summary (string) - Section description
            - summaryformat int - summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - modules List of Dictionary - list of activities
                - id int - activity id
                - url (string)  Optional - activity url
                - name (string) - activity module name
                - description (string)  Optional - activity description
                - visible int  Optional - module visibility (1:visible, 0: not visible)
                - modicon (string) - activity icon url
                - modname (string) - activity module type
                - modplural (string) - activity module plural name
                - availablefrom int  Optional - module availability start date
                - availableuntil int  Optional - module availability en date
                - indent int - number of indentation in the site
                - contents List of Dictionary - list of contents
                    - type (string) - a file or a folder or external link
                    - filename (string) - filename
                    - filepath (string) - filepath
                    - filesize int - filesize
                    - fileurl (string)  Optional - downloadable file url
                    - content (string)  Optional - Raw content, will be used when type is content
                    - timecreated int - Time created
                    - timemodified int - Time modified
                    - sortorder int - Content sort order
                    - userid int - User who added this content to Moodle
                    - author (string) - Content owner
                    - license (string) - Content license
        '''
        try:
            courseid = int(courseid)
        except TypeError:
            raise TypeError('courseid must be an integer or a string only with numbers')
        function = 'core_course_get_contents'
        param = urllib.urlencode({'courseid': courseid})
        num=0
        optParameters = ['name','value']
        for option in options:
            param += self.add_optParameters(option, 'options', num, optParameters)
            num += 1
        return self.connect(function, param)

    def get_courses(self, courses=''):
        ''' Return course details, all courses details returned if no parameters specified. 
        @param courses: 0 or more course identifiers.
        @type courses: List of Integer
        @return: List of Dictionary - list of courses:
            - id int   - course id
            - shortname (string)   - course short name
            - categoryid int   - category id
            - categorysortorder int  Optional - sort order into the category
            - fullname (string)   - course's full name
            - idnumber (string)  Optional - id number
            - summary (string)   - summary
            - summaryformat int   - summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - format (string)   - course format: weeks, topics, social, site,..
            - showgrades int  Optional - 1 if grades are shown, otherwise 0
            - newsitems int  Optional - number of recent items appearing on the course page
            - startdate int   - timestamp when the course start
            - numsections int  Optional - (Deprecated, use courseformatoptions) number of weeks/topics
            - maxbytes int  Optional - largest size of file that can be uploaded into the course
            - showreports int  Optional - are activity report shown (yes = 1, no =0)
            - visible int  Optional - 1: available to student, 0:not available
            - hiddensections int  Optional - (deprecated, use courseformatoptions) How the hidden sections in the course are displayed to students
            - groupmode int  Optional - no group, separate, visible
            - groupmodeforce int  Optional - force to use group mode (1: yes, 0: no)
            - defaultgroupingid int  Optional - default grouping id
            - timecreated int  Optional - timestamp when the course have been created
            - timemodified int  Optional - timestamp when the course have been modified
            - enablecompletion int  Optional - Enabled, control via completion and activity settings. Disabled, not shown in activity settings.
            - completionnotify int  Optional - Notify users when they complete this course (1: yes 0: no)
            - lang (string)  Optional - forced course language
            - forcetheme (string)  Optional - name of the course's forced theme (if allowcoursethemes option is enabled)
            - courseformatoptions List of Dictionary Optional - additional options for particular course format
                - name (string)   - course format option name
                - value (string)   - course format option value
        '''
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
        @param courses: 1 or more courses to create:
            - fullname (string)    - course's full name
            - shortname (string)    - course short name
            - categoryid int    - category identifier
            - idnumber (string)  Optional  - id number
            - summary (string)  Optional  - summary
            - summaryformat int  Default to "1"  - summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - format (string)  Default to "weeks"  - course format: weeks, topics, social, site,..
            - showgrades int  Default to "1"  - 1 if grades are shown, otherwise 0
            - newsitems int  Default to "5"  - number of recent items appearing on the course page
            - startdate int  Optional  - timestamp when the course start
            - numsections int  Optional  - (deprecated, use courseformatoptions) number of weeks/topics
            - maxbytes int  Default to "2097152"  - largest size of file that can be uploaded into the course
            - showreports int  Default to "0"  - are activity reports shown (yes = 1, no =0)
            - visible int  Optional - 1: visible for students, 0:not visible for students
            - hiddensections int  Optional  - (deprecated, use courseformatoptions) How the hidden sections in the course are displayed to students
            - groupmode int  Default to "0"  - no group, separate, visible
            - groupmodeforce int  Default to "0"  - force to use group mode (1: yes, 0: no)
            - defaultgroupingid int  Default to "0"  - default grouping id
            - enablecompletion int  Optional  - Enabled, control via completion and activity settings. Disabled, not shown in activity settings.
            - completionnotify int  Optional  - Notify users when they complete this course (1: yes 0: no)
            - lang (string)  Optional  - forced course language
            - forcetheme (string)  Optional  - name of the course's forced theme (if allowcoursethemes option is enabled)
            - courseformatoptions  Optional  - additional options for particular course format
                - name (string)    - course format option name
                - value (string)    - course format option value
        @type courses: List of Dictionaries
        @return: List of Dictionary - List of courses created:
            - id int  - course id
            - shortname (string)   - course's short name
        '''
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
        @type courses: List of Integer '''
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
        @param courses: 1 or more courses to update:
            - id int   - ID of the course
            - fullname (string)  Optional  - course's full name
            - shortname (string)  Optional  - course short name
            - categoryid int  Optional  - category identifier
            - idnumber (string)  Optional  - id number
            - summary (string)  Optional  - summary
            - summaryformat int  Optional  - summary format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - format (string)  Optional  - course format: weeks, topics, social, site,..
            - showgrades int  Optional  - 1 if grades are shown, otherwise 0
            - newsitems int  Optional  - number of recent items appearing on the course page
            - startdate int  Optional  - timestamp when the course start
            - numsections int  Optional  - (deprecated, use courseformatoptions) number of weeks/topics
            - maxbytes int  Optional  - largest size of file that can be uploaded into the course
            - showreports int  Optional  - are activity reports shown (yes = 1, no =0)
            - visible int  Optional - 1: visible for students, 0:not visible for students
            - hiddensections int  Optional  - (deprecated, use courseformatoptions) How the hidden sections in the course are displayed to students
            - groupmode int  Optional  - no group, separate, visible
            - groupmodeforce int  Optional  - force to use group mode (1: yes, 0: no)
            - defaultgroupingid int  Optional  - default grouping id
            - enablecompletion int  Optional  - Enabled, control via completion and activity settings. Disabled, not shown in activity settings.
            - completionnotify int  Optional  - Notify users when they complete this course (1: yes 0: no)
            - lang (string)  Optional  - forced course language
            - forcetheme (string)  Optional  - name of the course's forced theme (if allowcoursethemes option is enabled)
            - courseformatoptions  Optional  - additional options for particular course format
                - name (string)    - course format option name
                - value (string)    - course format option value
        @type courses: List of Dictionaries
        @return: A dictionary with a list of possible warnings for each course updated:
            - warnings List of Dictionary  Optional - list of warnings
                - item (string)  Optional  - item
                - itemid int  Optional  - item id
                - warningcode (string)   - the warning code can be used by the client app to implement specific behaviour
                - message (string)   - untranslated english message to explain the warning
        '''
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
        @type courseid: Integer
        @param fullname: duplicated course full name.
        @type fullname: String
        @param shortname: duplicated course short name.
        @type shortname: String
        @param categoryid: duplicated course category parent identifier.
        @type categoryid: Integer
        @param visible: duplicated course visible, default to yes (0(No) or 1(Yes)).
        @type visible: Integer
        @param options: list of duplicating options:
            - name  (string)   - the backup option name. Expected names (with their possible values formats) are:
                - "activities"  int  - Include course activites (default to 1 that is equal to yes).
                - "blocks"  int  - Include course blocks (default to 1 that is equal to yes).
                - "filters"  int  - Include course filters  (default to 1 that is equal to yes).
                - "users"  int  - Include users (default to 0 that is equal to no).
                - "role_assignments"  int  - Include role assignments  (default to 0 that is equal to no).
                - "comments"  int  - Include user comments  (default to 0 that is equal to no).
                - "completion_information"  int  - Include user course completion information  (default to 0 that is equal to no).
                - "logs"  int  - Include course logs  (default to 0 that is equal to no).
                - "histories"  int  - Include histories  (default to 0 that is equal to no).
            - value (string)   - the value for the option 1 (yes) or 0 (no)
        @type options: List of Dictionaries
        @return: A dictionary with the course copy id and shortname:
            - id int   - course id
            - shortname (string)   - short name '''
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
        @type importfrom: Integer
        @param importto: the identifier of the course we are importing to.
        @type importto: Integer
        @param deletecontent: whether to delete the course content where we are importing to (default to No) (1 (yes) or 0 (no)).
        @type deletecontent: Integer
        @param options: list of importing options:
            - name  (string)   - the backup option name. Expected names (with their possible values formats) are:
                - "activities"  int  Include course activites (default to 1 that is equal to yes).
                - "blocks"  int  Include course blocks (default to 1 that is equal to yes).
                - "filters"  int  Include course filters  (default to 1 that is equal to yes).
            - value (string)   - the value for the option 1 (yes) or 0 (no)
        @type options: List of Dictionaries'''
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
        @param criteria: List of criteria to filter the categories:
            - key  (string)   - the category column to search. Expected keys (with their possible values formats) are:
                - "id"  int  the category id.
                - "name" (string) the category name.
                - "parent"  int  the parent category id.
                - "idnumber" (string) category idnumber
                    - user must have 'moodle/category:manage' to search on idnumber.
                - "visible"  int  whether the returned categories must be visible or hidden. If the key is not passed, then the function return all categories that the user can see.
                    - user must have 'moodle/category:manage' or 'moodle/category:viewhiddencategories' to search on visible
                - "theme" (string) only return the categories having this theme
                    - user must have 'moodle/category:manage' to search on theme
            - value (string)   - the value to match.
        Criteria example: [{'key':'parent','value':'0'},{'key':'visible','value':'1'}]. Gets visible categories with parents' ID = 0
        @type criteria: List of Dictionary
        @param addsubcategories: return the sub categories infos (1 - default) otherwise only the category info (0).
        @type addsubcategories: Integer
        @return: List of Dictionary - Categories list:
            - id int   - category id
            - name (string)   - category name
            - idnumber (string)  Optional - category id number
            - description (string)   - category description
            - descriptionformat int   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - parent int   - parent category id
            - sortorder int   - category sorting order
            - coursecount int   - number of courses in this category
            - visible int  Optional - 1: visible, 0: not visible
            - visibleold int  Optional - visibility independent of parent categories, 1: visible, 0:not visible
            - timemodified int  Optional - timestamp
            - depth int   - category depth
            - path (string)   - category path
            - theme (string)  Optional - category theme
        '''
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
        @param categories: 1 or more categories to create:
            - name (string)   - new category name
            - parent int  Default to "0" - the parent category id inside which the new category will be created. Set to 0 for a root category
            - idnumber (string)  Optional - the new category idnumber
            - description (string)  Optional - the new category description
            - descriptionformat int  Default to "1" - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - theme (string)  Optional - the new category theme. This option must be enabled on Moodle
        @type categories: List of Dictionaries
        @return: List of Dictionary. List of categories created:
            - id int   //new category id
            - name (string)   //new category name
        '''
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
        @param categories: 1 or more categories to update:
            - id int   - category id to update
            - name (string)  Optional - category name
            - idnumber (string)  Optional - category id number
            - parent int  Optional - parent category id
            - description (string)  Optional - category description
            - descriptionformat int  Default to "1" - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - theme (string)  Optional - the category theme. This option must be enabled on moodle
        @type categories: List of Dictionaries '''
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
        @param categories: 1 or more categories to delete:
            - id int   - category id to delete
            - newparent int  Optional - the parent category to move the contents to, if specified
            - recursive int  Default to "0" - 1: recursively delete all contents inside this category, 0 (default): move contents to newparent or current parent category (except if parent is root)
        @type categories: List of Dictionaries '''
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
        @type modules: List of Integer '''
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
        
