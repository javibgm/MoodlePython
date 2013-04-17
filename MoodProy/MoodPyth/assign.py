from MoodPyth import MoodClass

class assign(MoodClass):
    def get_assigments(self, array=''):
    # Returns the courses and assignments for the users capability
        function="mod_assign_get_assignments"
        param = ''
        num=0
        if type(array)!=type([]) and array!='':
            raise TypeError('Input must be a list of integers with, at least, 1 course id')
        for course in array:
            if num!=0:
                param += '&'
            try:
                course = int(course)
                param += self.add_reqParameters(course, 'courseids', num)
            except ValueError:
                param += self.add_reqParameters(course, 'capabilities', num)
            num += 1
        return self.connect(function, param)
    
    def get_grades(self, assignmid):
    # Returns grades from the assignment
        function="mod_assign_get_grades"
    
    def get_submissions(self):
    # Returns the submissions for assignments
        function = 'mod_assign_get_submissions'
    

    '''
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
    '''