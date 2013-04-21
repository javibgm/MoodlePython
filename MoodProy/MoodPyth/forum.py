
from MoodPyth import MoodClass

class forum(MoodClass):
    def get_forum_discussions(self, forumids):
    # Returns a list of forum discussions contained within a given set of forums
        if type(forumids)!=type([]) or forumids==[]:
            raise TypeError('Input must be a list of forum IDs (integers)')
        function = 'mod_forum_get_forum_discussions'
        param = ''
        num=0
        for forumid in forumids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(forumid, 'forumids', num)
            num += 1
        return self.connect(function, param)

    def get_forums_by_courses(self, courseids=''):
    # Returns a list of forum instances in a provided set of courses, if no courses are provided then all the forum instances the user has access to will be returned
        if type(courseids)!=type([]) and courseids!='':
            raise TypeError('Input must be a list of course IDs (integers)')
        function = 'mod_forum_get_forums_by_courses'
        param = ''
        num=0
        for courseid in courseids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(courseid, 'courseids', num)
            num += 1
        return self.connect(function, param)

