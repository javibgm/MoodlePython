from MoodPyth import MoodClass
from MoodPyth.assign import assign
from MoodPyth.calendar import calendar
from MoodPyth.course import course
from MoodPyth.enrol import enrol
from MoodPyth.files import files
from MoodPyth.forum import forum
from MoodPyth.group import group
import urllib

class MoodLib(MoodClass, course, assign, calendar, enrol, files, forum, group):
    def get_site_info(self):
    # Get general info about Moodle site
        function="core_webservice_get_site_info"
        return self.connect(function, urllib.urlencode({}))
