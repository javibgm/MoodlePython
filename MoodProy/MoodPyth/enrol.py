''' Enroll class module '''
from MoodPyth import MoodClass
import urllib

class Enrol(MoodClass):
    '''
    Class with Moodle web services functions that work with enrollments.
    '''
    def get_enrolled_users(self, courseid, options=''):
        ''' Get users enrolled in a course. 
        @param courseid: course identifier to get its enrolled users.
        @type courseid: Integer
        @param options:  List of enrollment options to filter users:
            - name (string)  - the option name. Expected names (with their possible values formats) are:
                - "withcapability" (string) return only users with this capability.
                    - This option requires 'moodle/role:review' on the course context.
                - "groupid"  (int)  return only users in this group id.
                    - This option requires 'moodle/site:accessallgroups' on the course context.
                - "onlyactive"  (int)  return only users with active enrollments and matching time restrictions.
                    - This option requires 'moodle/course:enrolreview' on the course context.
                - "userfields" ('string, string, ...') return only the values of these user fields.
                - "limitfrom"  (int)  sql limit from.
                - "limitnumber"  (int)  maximum number of returned users.
            - value (string)  - the value to match.
        Enrollment options example: [{'key':'withcapability','value':'moodle/role:review'},{'key':'groupid','value':'1'}]. Gets enrolled users which have moodle/role:review capability and belong to group 1
        @type options: List of Dictionaries
        @return: List of Dictionary. List of enrolled users in courseid course and that match with enrollment options filters:
            - id (int)   - ID of the user
            - username (string) Optional - Username policy is defined in Moodle security config
            - firstname (string) Optional - The first name(s) of the user
            - lastname (string) Optional - The family name of the user
            - fullname (string)  - The fullname of the user
            - email (string) Optional - An email address - allow email as root@localhost
            - address (string) Optional - Postal address
            - phone1 (string) Optional - Phone 1
            - phone2 (string) Optional - Phone 2
            - icq (string) Optional - icq number
            - skype (string) Optional - skype id
            - yahoo (string) Optional - yahoo id
            - aim (string) Optional - aim id
            - msn (string) Optional - msn number
            - department (string) Optional - department
            - institution (string) Optional - institution
            - idnumber (string) Optional - An arbitrary ID code number perhaps from the institution
            - interests (string) Optional - user interests (separated by commas)
            - firstaccess (int)  Optional - first access to the site (0 if never)
            - lastaccess (int)  Optional - last access to the site (0 if never)
            - description (string) Optional - User profile description
            - descriptionformat (int)  Optional - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - city (string) Optional - Home city of the user
            - url (string) Optional - URL of the user
            - country (string) Optional - Home country code of the user, such as AU or CZ
            - profileimageurlsmall (string) Optional - User image profile URL - small version
            - profileimageurl (string) Optional - User image profile URL - big version
            - customfields (List of Dictionary)  Optional - List of user custom fields (also known as user profile fields):
                - type (string)  - The type of the custom field - text field, checkbox...
                - value (string)  - The value of the custom field
                - name (string)  - The name of the custom field
                - shortname (string)  - The shortname of the custom field - to be able to build the field class in the code
            - groups (List of Dictionary)  Optional - list of user groups which user belongs:
                - id (int)   - group id
                - name (string)  - group name
                - description (string)  - group description
                - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - roles (List of Dictionary)  Optional - user roles list:
                - roleid (int)   - role id
                - name (string)  - role name
                - shortname (string)  - role shortname
                - sortorder (int)   - role sortorder
            - preferences (List of Dictionary)  Optional -  user preferences list:
                - name (string)  - The name of the preferences
                - value (string)  - The value of the custom field
            - enrolledcourses   Optional - list of courses where the user is enrolled (limited by which courses the user is able to see)
                - id (int)   - Id of the course
                - fullname (string)  - Fullname of the course
                - shortname (string)  - Shortname of the course
        @raise TypeError: if courseid input parameter is not an integer.
        '''
        try:
            courseid = int(courseid)
        except ValueError:
            raise TypeError('courseid must be an integer or a string only with numbers')
        function = "core_enrol_get_enrolled_users"
        param = urllib.urlencode({'courseid':courseid})
        num=0
        for option in options:
            param += self.add_optParameters(option, 'options', num, ['name','value'])
            num += 1
        return self.connect(function, param)

    def get_enrolled_users_with_capability(self, coursecapabilities, options=''):
        ''' For each course and capability specified, return a list of the users that are enrolled in that course and have that capability. 
        @param coursecapabilities: dictionaries with a course identifier and capabilities to get the enrolled users in that course with those capabilities:
            - courseid (int)   - Course ID number in the Moodle course table
            - capabilities (List of string) - Capability names, such as "mod/forum:viewdiscussion"
        @type coursecapabilities: List of Dictionary
        @param options:  List of enrollment options to filter users:
            - name (string)  - the option name. Expected names (with their possible values formats) are:
                - "groupid"  (int)  return only users in this group id.
                    - Requires 'moodle/site:accessallgroups' .
                - "onlyactive"  (int)  only users with active enrolments.
                    - Requires 'moodle/course:enrolreview' .
                - "userfields" ('string, string, ...') return only the values of these user fields.
                - "limitfrom"  (int)  sql limit from.
                - "limitnumber"  (int)  max number of users per course and capability.
            - value (string)  - the value to match.
        @type options: List of Dictionaries
        @return: List of Dictionary. Dictionaries with a specified course, a specified capability and a users list:
            - id (int)   - ID of the user
            - username (string) Optional - Username policy is defined in Moodle security config
            - firstname (string) Optional - The first name(s) of the user
            - lastname (string) Optional - The family name of the user
            - fullname (string)  - The fullname of the user
            - email (string) Optional - An email address - allow email as root@localhost
            - address (string) Optional - Postal address
            - phone1 (string) Optional - Phone 1
            - phone2 (string) Optional - Phone 2
            - icq (string) Optional - icq number
            - skype (string) Optional - skype id
            - yahoo (string) Optional - yahoo id
            - aim (string) Optional - aim id
            - msn (string) Optional - msn number
            - department (string) Optional - department
            - institution (string) Optional - institution
            - idnumber (string) Optional - An arbitrary ID code number perhaps from the institution
            - interests (string) Optional - user interests (separated by commas)
            - firstaccess (int)  Optional - first access to the site (0 if never)
            - lastaccess (int)  Optional - last access to the site (0 if never)
            - description (string) Optional - User profile description
            - descriptionformat (int)  Optional - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - city (string) Optional - Home city of the user
            - url (string) Optional - URL of the user
            - country (string) Optional - Home country code of the user, such as AU or CZ
            - profileimageurlsmall (string) Optional - User image profile URL - small version
            - profileimageurl (string) Optional - User image profile URL - big version
            - customfields (List of Dictionary)  Optional - List of user custom fields (also known as user profile fields):
                - type (string)  - The type of the custom field - text field, checkbox...
                - value (string)  - The value of the custom field
                - name (string)  - The name of the custom field
                - shortname (string)  - The shortname of the custom field - to be able to build the field class in the code
            - groups (List of Dictionary)  Optional - list of user groups which user belongs:
                - id (int)   - group id
                - name (string)  - group name
                - description (string)  - group description
                - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - roles (List of Dictionary)  Optional - user roles list:
                - roleid (int)   - role id
                - name (string)  - role name
                - shortname (string)  - role shortname
                - sortorder (int)   - role sortorder
            - preferences (List of Dictionary)  Optional -  user preferences list:
                - name (string)  - The name of the preferences
                - value (string)  - The value of the custom field
            - enrolledcourses (List of Dictionary)  Optional - list of courses where the user is enrolled (limited by which courses the user is able to see)
                - id (int)   - Id of the course
                - fullname (string)  - Fullname of the course
                - shortname (string)  - Shortname of the course
        @raise TypeError: if coursecapabilities input parameter type is not a list or is an empty list. Also if coursecapabilities contained dictionaries do not have the courseid and capabilities keys.
        '''
        function = 'core_enrol_get_enrolled_users_with_capability'
        if type(coursecapabilities)!=type([]) or coursecapabilities==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "courseid" and "capabilities"')
        param = ''
        num=0
        try:
            for coursecapability in coursecapabilities:
                if num!=0:
                    param += '&'
                param += self.add_reqParameters(coursecapability, 'coursecapabilities', num, ['courseid']) + '&'
                numcapab=0
                for capability in coursecapability['capabilities']:
                    if numcapab!=0:
                        param += '&'
                    param += self.add_reqParameters(capability, 'coursecapabilities['+str(num)+'][capabilities]', numcapab)
                    numcapab += 1
                num += 1
        except KeyError:
            raise TypeError('Input must be a list of dictionaries with the keys "courseid" and "capabilities"')
        num=0
        for option in options:
            param += self.add_optParameters(option, 'options', num, ['name','value'])
            num += 1
        return self.connect(function, param)

    def get_users_courses(self, userid):
        ''' Get the list of courses where a user is enrolled in.
        @param userid: User identifier.
        @type userid: Integer
        @return: List of Dictionary. Courses list:
            - id (int)   - id of course
            - shortname (string)  - short name of course
            - fullname (string)  - long name of course
            - enrolledusercount (int)   - Number of enrolled users in this course
            - idnumber (string)  - id number of course
            - visible (int)   - 1 means visible, 0 means hidden course
        @raise TypeError: if userid input parameter is not an integer.
        '''
        try:
            userid = int(userid)
        except ValueError:
            raise TypeError('userid must be an integer or a string with only numbers')
        function = 'core_enrol_get_users_courses'
        param = urllib.urlencode({'userid': userid})
        return self.connect(function, param)

    def manual_enrol_users(self, enrollist):
        ''' Enrol users manually.
        @param enrollist: 1 or more enrollments of user into course with a specific role:
            - roleid (int)   - Role to assign to the user
            - userid (int)   - The user that is going to be enrolled
            - courseid (int)   - The course to enrol the user role in
            - timestart (int)  Optional - Timestamp when the enrolment start
            - timeend (int)  Optional - Timestamp when the enrolment end
            - suspend (int)  Optional - set to 1 to suspend the enrolment
        @type enrollist: List of Dictionaries
        @raise TypeError: if enrollist input parameter type is not a list or is an empty list.
        '''
        function = 'enrol_manual_enrol_users'
        if type(enrollist)!=type([]) or enrollist==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "roleid", "userid" and "courseid"')
        param = ''
        num=0
        reqParameters = ['roleid', 'userid', 'courseid']
        optParameters = ['timestart', 'timeend', 'suspend']
        for enrol in enrollist:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(enrol, 'enrolments', num, reqParameters)
            param += self.add_optParameters(enrol, 'enrolments', num, optParameters)
            num += 1
        return self.connect(function, param)
