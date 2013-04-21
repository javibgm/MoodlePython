from MoodPyth import MoodClass
import urllib

class assign(MoodClass):
    def get_assigments(self, courseids='', capabilities=''):
    # Returns the courses and assignments for the users capability
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
    # Returns grades from the assignment
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
    # Returns the submissions for assignments
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