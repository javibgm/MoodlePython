from MoodProy import *

class assign(MoodClass):
    def get_submissions(self):
    # Returns the submissions for assignments
        function = 'mod_assign_get_submissions'
    
    def get_grades(self, assignmid):
    # Get grades from an assigment
        if (not (type(int(assignmid)) == int)):
            print 'Incorrect input: course ID must be an integer'
            return None
        function="mod_assign_get_grades"
        param = urllib.urlencode({'assignmentids[0]': assignmid})
        return self.connect(function, param)
    
    def get_assigments(self, courseids='', capabilities=''):
    # Get users enrrolled in a course with the specified capabilities
        function="mod_assign_get_assignments"
        param = []
        param = urllib.urlencode({})
        if (courseids!=''):
            param.append(('courseids[0]', courseids))
        if (capabilities!=''):
            param.append(('capabilities[0]', capabilities))
        param = urllib.urlencode(param)
        return self.connect(function, param)
