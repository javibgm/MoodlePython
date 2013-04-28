''' Enroll class module '''
from MoodPyth import MoodClass
import urllib

class Enrol(MoodClass):
    '''
    Class with Moodle web services functions that work with enrollments.
    '''
    def enrolled_users(self, courseid, options=''):
        ''' Get users enrolled in a course. 
        @param courseid: course identifier to get its enrolled users.
        @type courseid: Integer.
        @param options:  Enrollment options to filter users.
        Required keys: 'name','value'.
        
        The 'name' value is the option name. Expected names (value format) are:
            -  "withcapability" (string) return only users with this capability.
                - This option requires 'moodle/role:review' on the course context.
            - "groupid" (integer) return only users in this group id.
                - This option requires 'moodle/site:accessallgroups' on the course context.
            - "onlyactive" (integer) return only users with active enrolments and matching time restrictions.
                - This option requires 'moodle/course:enrolreview' on the course context.
            - "userfields" ('string, string, ...') return only the values of these user fields.
            - "limitfrom" (integer) sql limit from.
            - "limitnumber" (integer) maximum number of returned users.
        The 'value' key value is a string with the value to match.
        @type options: List of Dictionaries. '''
        function = "core_enrol_get_enrolled_users"
        if type(courseid)!=type('a') and type(courseid)!=type(0):
            raise TypeError('Input must be a an integer')
        param = urllib.urlencode({'courseid':courseid})
        num=0
        for option in options:
            param += self.add_optParameters(option, 'options', num, ['name','value'])
            num += 1
        return self.connect(function, param)

    def get_enrolled_users_with_capability(self, coursecapabilities, options=''):
        ''' For each course and capability specified, return a list of the users that are enrolled in the course and have that capability. 
        @param coursecapabilities: course identifier and capabilities to get the enrolled users in that course with those capabilities.
        @type coursecapabilities: Dictionary. 
        @param options:  Enrollment options to filter users.
        Required keys: 'name','value'.
        
        The 'name' value is the option name. Expected names (value format) are:
            - "groupid" (integer) return only users in this group id.
                - Requires 'moodle/site:accessallgroups' .
            - "onlyactive" (integer) only users with active enrolments.
                - Requires 'moodle/course:enrolreview' .
            - "userfields" ('string, string, ...') return only the values of these user fields.
            - "limitfrom" (integer) sql limit from.
            - "limitnumber" (integer) max number of users per course and capability.
        The 'value' key value is a string with the value to match.
        @type options: List of Dictionaries. '''
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
        @type userid: Integer. '''
        try:
            userid = int(userid)
            function = 'core_enrol_get_users_courses'
            param = urllib.urlencode({'userid': userid})
            return self.connect(function, param)
        except ValueError:
            raise TypeError('userid must be an integer or a string with only numbers')

    def manual_enrol_users(self, enrollist):
        ''' Enrol users manually.
        @param enrollist: 1 or more enrollments of user into course with a specific role.
        @type enrollist: List of Dictionaries. '''
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