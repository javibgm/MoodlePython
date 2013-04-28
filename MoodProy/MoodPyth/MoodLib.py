''' Moodle Library functions class module '''
from MoodPyth import MoodClass
from MoodPyth.assign import Assign
from MoodPyth.calendar import Calendar
from MoodPyth.course import Course
from MoodPyth.enrol import Enrol
from MoodPyth.files import Files
from MoodPyth.forum import Forum
from MoodPyth.group import Group
from MoodPyth.message import Message

class MoodLib(MoodClass, Assign, Calendar, Course, Enrol, Files, Forum, Group, Message):
    '''
    Basic Moodle python class. This class inherits from all other classes in order to have all their methods so it can execute every Moodle function. 
    '''
    def get_site_info(self):
        '''
        Get general info about Moodle site
        @return: Dictionary.
        '''
        function="core_webservice_get_site_info"
        return self.connect(function, '')
