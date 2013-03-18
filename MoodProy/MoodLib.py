"""
    'user': 'admin',
    'pasw': 'AdminP@ss1',
    
    'user': 'manager1',
    'pasw': 'ManagerP@ss1',

    'user': 'student1',
    'pasw': 'StudentP@ss1',
"""
from MoodProy import *
from MoodProy.course import *

info = {
    'web': 'http://adry3000.dyndns.org',
    'user': 'admin',
    'pasw': 'AdminP@ss1',
    'service': 'ext_ser'
}

class MoodLib(MoodClass, course):
    def get_site_info(self):
    # Get general info about Moodle site
        function="core_webservice_get_site_info"
        return self.connect(function, urllib.urlencode({}))
