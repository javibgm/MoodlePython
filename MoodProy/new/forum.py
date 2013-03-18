from MoodProy import *

class forum(MoodClass):
    def get_forums_by_courses(self):
    # Returns a list of forum instances in a provided set of courses, if no courses are provided then all the forum instances the user has access to will be returned
        function = 'mod_forum_get_forums_by_courses'

    def get_forum_discussions(self):
    # Returns a list of forum discussions contained within a given set of forums
        function = 'mod_forum_get_forum_discussions'

