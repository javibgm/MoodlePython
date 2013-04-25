from MoodPyth import MoodClass
from MoodPyth.assign import assign
from MoodPyth.calendar import calendar
from MoodPyth.course import Course
from MoodPyth.enrol import enrol
from MoodPyth.files import files
from MoodPyth.forum import forum
from MoodPyth.group import group
import urllib

class MoodLib(MoodClass, Course, assign, calendar, enrol, files, forum, group):
    '''
    Basic Moodle python class.
    '''
    def get_site_info(self):
        '''
        Get general info about Moodle site
        @return: 
        '''
        function="core_webservice_get_site_info"
        return self.connect(function, urllib.urlencode({}))
