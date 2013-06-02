''' Moodle Library functions class module '''
from MoodPyth import MoodClass
from MoodPyth.assign import Assign
from MoodPyth.calendar import Calendar
from MoodPyth.cohort import Cohort
from MoodPyth.course import Course
from MoodPyth.enrol import Enrol
from MoodPyth.external import External
from MoodPyth.files import Files
from MoodPyth.forum import Forum
from MoodPyth.grade import Grade
from MoodPyth.group import Group
from MoodPyth.message import Message
from MoodPyth.notes import Notes
from MoodPyth.role import Role
from MoodPyth.user import User

class MoodLib(MoodClass, Assign, Calendar, Cohort, Course, Enrol, External, Files, Forum, Grade, Group, Message, Notes, Role, User):
    '''
    Basic Moodle python class. This class inherits from all other classes in order to have all their methods so it can execute every Moodle function. It also have functions related with web services. 
    '''
    def get_site_info(self):
        '''
        Get general info about Moodle site
        @return: Dictionary. Moodle site information:
            - sitename (string)   - site name
            - username (string)   - username
            - firstname (string)   - first name
            - lastname (string)   - last name
            - fullname (string)   - user full name
            - lang (string)   - user language
            - userid (int)   - user id
            - siteurl (string)   - site url
            - userpictureurl (string)   - the user profile picture.
            Warning: this url is the public URL that only works when forcelogin is set to NO and guestaccess is set to YES.
            In order to retrieve user profile pictures independently of the Moodle config, replace "pluginfile.php" by
            "webservice/pluginfile.php?token=WSTOKEN&file="
            Of course the user can only see profile picture depending
            on his/her permissions. Moreover it is recommended to use HTTPS too.
            functions (List of Dictionary) - functions that are available
                - name (string)   - function name
                - version (string)   - The version number of the component to which the function belongs
            - downloadfiles (int)  Optional - 1 if users are allowed to download files, 0 if not
            - release (string)  Optional - Moodle release number
            - version (string)  Optional - Moodle version number
            - mobilecssurl (string)  Optional - Mobile custom CSS theme
        '''
        function="core_webservice_get_site_info"
        return self.connect(function, '')