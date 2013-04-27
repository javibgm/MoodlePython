'''
Assignment class module
'''
from MoodPyth import MoodClass
import urllib

class assign(MoodClass):
    '''
    Class with Moodle web services functions that work with assignments
    '''
    def get_assigments(self, courseids='', capabilities=''):
        ''' Returns the courses and assignments for the users capability.
        If no courseids and capabilities are specified, it will be searched in all courses where user is enrolled
        @return: A dictionary with:
            - courses List of dictionary - list of courses:
                - id int   - course id
                - fullname string   - course full name
                - shortname string   - course short name
                - timemodified int   - last time modified
                - assignments List of dictionary - assignment information:
                    - id int   - assignment id
                    - course int   - course id
                    - name string   - assignment name
                    - nosubmissions int   - no submissions
                    - submissiondrafts int   - submissions drafts
                    - sendnotifications int   - send notifications
                    - sendlatenotifications int   - send notifications
                    - duedate int   - assignment due date
                    - allowsubmissionsfromdate int   - allow submissions from date
                    - grade int   - grade type
                    - timemodified int   - last time assignment was modified
                    - completionsubmit int   - if enabled, set activity as complete following submission
                    - cutoffdate int   - date after which submission is not accepted without an extension
                    - teamsubmission int   - if enabled, students submit as a team
                    - requireallteammemberssubmit int   - if enabled, all team members must submit
                    - teamsubmissiongroupingid int   - the grouping id for the team submission groups
                    - blindmarking int   - if enabled, hide identities until reveal identities actioned
                    - revealidentities int   - show identities for a blind marking assignment
                    - requiresubmissionstatement int   - student must accept submission statement
                    - configs List of dictionary - configuration settings:
                            - id int   - assign_plugin_config id
                            - assignment int   - assignment id
                            - plugin string   - plugin
                            - subtype string   - subtype
                            - name string   - name
                            - value string   - value
            - warnings List of dictionary Optional - list of warnings:
                - item string  Optional - item can be 'course' (errorcode 1 or 2) or 'module' (errorcode 1)
                - itemid int  Optional - When item is a course then itemid is a course id. When the item is a module then itemid is a module id
                - warningcode string   - errorcode can be 1 (no access rights) or 2 (not enrolled or no permissions)
                - message string   - untranslated english message to explain the warning
        @param courseids: 0 or more course ids
        @type courseids: List of Integer
        @param capabilities: capabilities used to filter courses 
        @type capabilities: List of String
        '''
        function="mod_assign_get_assignments"
        param = ''
        num=0
        if (type(courseids)!=type([]) and courseids!='') or (type(capabilities)!=type([]) and capabilities!=''):
            raise TypeError('Input must be a list of courseIDs(integers) and a list of capabilities(strings)')
        for course in courseids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(course, 'courseids', num)
            num += 1
        num=0
        for capability in capabilities:
            param += '&' + self.add_reqParameters(capability, 'capabilities', num)
            num += 1
        return self.connect(function, param)
    
    def get_grades(self, assignmentids, since=0):
        ''' Returns grades from the assignment
        @return: A dictionary with:
            - assignments List of dictionary - list of assignment grade information:
                - assignmentid int   - assignment id
                - grades List of dictionary  - list of grades:
                    - id int   - grade id
                    - userid int   - student id
                    - timecreated int   - grade creation time
                    - timemodified int   - grade last modified time
                    - grader int   - grader
                    - grade string   - grade
                    - locked int   - locked
                    - mailed int   - mailed
            - warnings List of dictionary Optional - list of warnings:
                - item string  Optional - item is always 'assignment'
                - itemid int  Optional - when errorcode is 3 then itemid is an assignment id. When errorcode is 1, itemid is a course module id
                - warningcode string   - errorcode can be 3 (no grades found) or 1 (no permission to get grades)
                - message string   - untranslated english message to explain the warning
        @param assignmentids: assignment ids
        @type assignmentids: List of Integer
        @param since: timestamp, only return records where timemodified >= since
        @type since: Integer'''
        function="mod_assign_get_grades"
        param = ''
        num=0
        if type(assignmentids)!=type([]) or assignmentids==[]:
            raise TypeError('Input must be a list of 1 or more integers')
        for assignid in assignmentids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(assignid, 'assignmentids', num)
            num += 1
        if since!=0:
            param += '&' + urllib.urlencode({'since': since})
        return self.connect(function, param)
    
    def get_submissions(self, assignmentids, status='', since=0, before=0):
        ''' Returns the submissions for assignment
        @return: A dictionary with:
            - assignments List of dictionary  - assignment submissions:
                - assignmentid int   - assignment id
                - submissions List of dictionary - list of submissions:
                    - id int   - submission id
                    - userid int   - student id
                    - timecreated int   - submission creation time
                    - timemodified int   - submission last modified time
                    - status string   - submission status
                    - groupid int   - group id
                    - plugins List of dictionary Optional - plugins
                        - type string   - submission plugin type
                        - name string   - submission plugin name
                        - fileareas List of dictionary Optional - fileareas:
                            - area string   - file area
                            - files List of dictionary Optional - files
                                - filepath string   - file path
                        - editorfields List of dictionary Optional - editorfields:
                            - name string   - field name
                            - description string   - field description
                            - text string   - field value
                            - format int   - text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - warnings List of dictionary Optional - list of warnings:
                - item string  Optional - item
                - itemid int  Optional - item id
                - warningcode string   - the warning code can be used by the client app to implement specific behaviour
                - message string   - untranslated english message to explain the warning
        @param assignmentids: assignment ids
        @type assignmentids: List of Integer
        @param status: submission status
        @type status: String
        @param since: timestamp, only return records where timemodified >= since
        @type since: Integer
        @param before: timestamp, only return records where timemodified <= before
        @type before: Integer'''
        function = 'mod_assign_get_submissions'
        param = ''
        num=0
        if type(assignmentids)!=type([]) or assignmentids==[]:
            raise TypeError('Input must be a list of 1 or more integers')
        for assignid in assignmentids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(assignid, 'assignmentids', num)
            num += 1
        if status!='':
            param += '&' + urllib.urlencode({'status': status})
        if since!=0:
            param += '&' + urllib.urlencode({'since': since})
        if before!=0:
            param += '&' + urllib.urlencode({'before': before})
        return self.connect(function, param)