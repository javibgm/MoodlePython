from MoodPyth import MoodClass
from MoodPyth.course import course
import urllib

class MoodLib(MoodClass, course):
    def get_site_info(self):
    # Get general info about Moodle site
        function="core_webservice_get_site_info"
        return self.connect(function, urllib.urlencode({}))
