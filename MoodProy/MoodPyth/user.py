######################## BEGIN LICENSE BLOCK ########################
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with MoodPyth.  If not, see <http://www.gnu.org/licenses/>.
######################### END LICENSE BLOCK #########################
''' User class module '''
from MoodPyth import MoodClass
import urllib

class User(MoodClass):
    '''
    Class with Moodle web services functions that works with users.
    '''
    def create_users(self, users):
        ''' Create users.
        @param users: 1 or more users to create:
            - username (string)   - Username policy is defined in Moodle security config.
            - password (string)   - Plain text password consisting of any characters
            - firstname (string)   - The first name(s) of the user
            - lastname (string)   - The family name of the user
            - email (string)   - A valid and unique email address
            - auth (string)  Default to "manual" - Auth plugins include manual, ldap, imap, etc
            - idnumber (string)  Default to "" - An arbitrary ID code number perhaps from the institution
            - lang (string)  Default to "en" - Language code such as "en", must exist on server
            - theme (string)  Optional - Theme name such as "standard", must exist on server
            - timezone (string)  Optional - Timezone code such as Australia/Perth, or 99 for default
            - mailformat (int)  Optional - Mail format code is 0 for plain text, 1 for HTML etc
            - description (string)  Optional - User profile description, no HTML
            - city (string)  Optional - Home city of the user
            - country (string)  Optional - Home country code of the user, such as AU or CZ
            - preferences (List of Dictionary) Optional - User preferences
                - type (string)   - The name of the preference
                - value (string)   - The value of the preference
            - customfields (List of Dictionary) Optional - User custom fields (also known as user profil fields)
                - type (string)   - The name of the custom field
                - value (string)   - The value of the custom field
        @type users: List of Dictionary
        @return: List of Dictionary. List of users ids and usernames of created users:
            - id (int)   - user id
            - username (string)   - user name
        @raise TypeError: if users input parameter type is not a list or is an empty list.
        '''
        if type(users)!=type([]) or users==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "username","password","firstname","lastname" and "email"')
        function = 'core_user_create_users'
        param = ''
        num=0
        reqParameters = ["username","password","firstname","lastname", "email"]
        optParameters = ['auth','idnumber', 'lang', 'theme', 'timezone', 'mailformat', 'description', 'city', 'country']
        for user in users:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(user, 'users', num, reqParameters)
            param += self.add_optParameters(user, 'users', num, optParameters)
            if 'preferences' in user:
                numformat = 0
                for preferences in user['preferences']:
                    param += self.add_optParameters(preferences,'users['+str(num)+'][preferences]',numformat,['type','value'])
                    numformat += 1
            if 'customfields' in user:
                numformat = 0
                for customfields in user['customfields']:
                    param += self.add_optParameters(customfields,'users['+str(num)+'][customfields]',numformat,['type','value'])
                    numformat += 1
            num += 1
        return self.connect(function, param)
       
    
    def get_course_user_profiles(self, userlist):
        ''' Get course user profiles (each of the profiles matching a course id and a user id)
        @param userlist: 1 or more user identifiers with course identifiers.
            - userid (int)   - userid
            - courseid (int)   - courseid
        @type userlist: List of Dictionary
        @return: List of Dictionary. List of user's profiles:
            - id (int)   - ID of the user
            - username (string)  Optional - The username
            - firstname (string)  Optional - The first name(s) of the user
            - lastname (string)  Optional - The family name of the user
            - fullname (string)   - The fullname of the user
            - email (string)  Optional - An email address - allow email as root@localhost
            - address (string)  Optional - Postal address
            - phone1 (string)  Optional - Phone 1
            - phone2 (string)  Optional - Phone 2
            - icq (string)  Optional - icq number
            - skype (string)  Optional - skype id
            - yahoo (string)  Optional - yahoo id
            - aim (string)  Optional - aim id
            - msn (string)  Optional - msn number
            - department (string)  Optional - department
            - institution (string)  Optional - institution
            - idnumber (string)  Optional - An arbitrary ID code number perhaps from the institution
            - interests (string)  Optional - user interests (separated by commas)
            - firstaccess (int)  Optional - first access to the site (0 if never)
            - lastaccess (int)  Optional - last access to the site (0 if never)
            - auth (string)  Optional - Auth plugins include manual, ldap, imap, etc
            - confirmed (int)  Optional - Active user: 1 if confirmed, 0 otherwise
            - lang (string)  Optional - Language code such as "en", must exist on server
            - theme (string)  Optional - Theme name such as "standard", must exist on server
            - timezone (string)  Optional - Timezone code such as Australia/Perth, or 99 for default
            - mailformat (int)  Optional - Mail format code is 0 for plain text, 1 for HTML etc
            - description (string)  Optional - User profile description
            - descriptionformat (int)  Optional - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - city (string)  Optional - Home city of the user
            - url (string)  Optional - URL of the user
            - country (string)  Optional - Home country code of the user, such as AU or CZ
            - profileimageurlsmall (string)   - User image profile URL - small version
            - profileimageurl (string)   - User image profile URL - big version
            - customfields (List of Dictionary) Optional - User custom fields (also known as user profile fields):
                - type (string)   - The type of the custom field - text field, checkbox...
                - value (string)   - The value of the custom field
                - name (string)   - The name of the custom field
                - shortname (string)   - The shortname of the custom field - to be able to build the field class in the code
            - preferences (List of Dictionary) Optional - Users preferences:
                - name (string)   - The name of the preferences
                - value (string)   - The value of the custom field
            - groups (List of Dictionary) Optional - user groups:
                - id (int)   - group id
                - name (string)   - group name
                - description (string)   - group description
                - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - roles (List of Dictionary) Optional - user roles:
                - roleid (int)   - role id
                - name (string)   - role name
                - shortname (string)   - role shortname
                - sortorder (int)   - role sortorder
            - enrolledcourses (List of Dictionary) Optional - Courses where the user is enrolled - limited by which courses the user is able to see:
                - id (int)   - Id of the course
                - fullname (string)   - Fullname of the course
                - shortname (string)   - Shortname of the course
        @raise TypeError: if userlist input parameter type is not a list or is an empty list.
        '''
        if type(userlist)!=type([]) or userlist==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 dictionary with the keys "userid" and "courseid"')
        function = 'core_user_get_course_user_profiles'
        param = ''
        num=0
        reqParameters = ["userid","courseid"]
        for user in userlist:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(user, 'userlist', num, reqParameters)
            num += 1
        return self.connect(function, param)
    
    def delete_users(self, userids):
        ''' Deletes all specified users.
        @param userids: 1 or more user identifiers.
        @type userids: List of Integer
        @raise TypeError: if userids input parameter type is not a list or is an empty list.
        '''
        if type(userids)!=type([]) or userids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 user id')
        function = 'core_user_delete_users'
        param = ''
        num=0
        for userid in userids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(userid, 'userids', num)
            num += 1
        return self.connect(function, param)
    
    def update_users(self, users):
        ''' Update users.
        @param users: 1 or more users to update:
            - id (int)   - ID of the user
            - username (string)  Optional - Username policy is defined in Moodle security config.
            - password (string)  Optional - Plain text password consisting of any characters
            - firstname (string)  Optional - The first name(s) of the user
            - lastname (string)  Optional - The family name of the user
            - email (string)  Optional - A valid and unique email address
            - auth (string)  Optional - Auth plugins include manual, ldap, imap, etc
            - idnumber (string)  Optional - An arbitrary ID code number perhaps from the institution
            - lang (string)  Optional - Language code such as "en", must exist on server
            - theme (string)  Optional - Theme name such as "standard", must exist on server
            - timezone (string)  Optional - Timezone code such as Australia/Perth, or 99 for default
            - mailformat (int)  Optional - Mail format code is 0 for plain text, 1 for HTML etc
            - description (string)  Optional - User profile description, no HTML
            - city (string)  Optional - Home city of the user
            - country (string)  Optional - Home country code of the user, such as AU or CZ
            - customfields (List of Dictionary) Optional - User custom fields (also known as user profil fields)
                - type (string)   - The name of the custom field
                - value (string)   - The value of the custom field
            - preferences (List of Dictionary) Optional - User preferences
                - type (string)   - The name of the preference
                - value (string)   - The value of the preference
        @type users: List of Dictionary
        @raise TypeError: if users input parameter type is not a list or is an empty list.
        '''
        if type(users)!=type([]) or users==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "id"')
        function = 'core_user_update_users'
        param = ''
        num=0
        reqParameters = ["id"]
        optParameters = ["username","password","firstname","lastname", "email"]
        optParameters += ['auth','idnumber', 'lang', 'theme', 'timezone', 'mailformat', 'description', 'city', 'country']
        for user in users:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(user, 'users', num, reqParameters)
            param += self.add_optParameters(user, 'users', num, optParameters)
            if 'preferences' in user:
                numformat = 0
                for preferences in user['preferences']:
                    param += self.add_optParameters(preferences,'users['+str(num)+'][preferences]',numformat,['type','value'])
                    numformat += 1
            if 'customfields' in user:
                numformat = 0
                for customfields in user['customfields']:
                    param += self.add_optParameters(customfields,'users['+str(num)+'][customfields]',numformat,['type','value'])
                    numformat += 1
            num += 1
        return self.connect(function, param)
    
    def get_users(self, criteria):
        ''' Search for users matching the parameters.
        @param criteria: List of users parameters to search. The dictionaries have a key/value structure:
            - key (string)   - the user column to search, expected keys (value format) are:
                - "id" (int) - matching user id,
                - "lastname" (string) - user last name (Note: you can use % for searching but it may be considerably slower!),
                - "firstname" (string) - user first name (Note: you can use % for searching but it may be considerably slower!),
                - "idnumber" (string) - matching user idnumber,
                - "username" (string) - matching user username,
                - "email" (string) - user email (Note: you can use % for searching but it may be considerably slower!),
                - "auth" (string) - matching user auth plugin
            - value (string)   - the value to search.
        The key/value pairs to be considered in user search. Values can not be empty.
        Specify different keys only once (fullname => 'user1', auth => 'manual', ...), key occurences are forbidden.
        The search is executed with AND operator on the criterias. Invalid criterias (keys) are ignored,
        the search is still executed on the valid criterias.
        You can search without criteria, but the function is not designed for it.
        Using % on searching criteria let you search users with any characters where % is placed on the string. Example:
            - key=firstname, value=a => users whose firstname is an 'a'.
            - key=firstname, value=a% => users whose firstname starts with an 'a'.
            - key=firstname, value=%a% => users whose firstname contains an 'a'.
        It could very slow or timeout. The function is designed to search some specific users.
        @type criteria: List of Dictionary
        @return: Dictionary. List of users that match with the searching criteria and occurred warnings:
            - users (List of Dictionary) - Users searched information:
                - id (int)   - ID of the user
                - username (string)  Optional - The username
                - firstname (string)  Optional - The first name(s) of the user
                - lastname (string)  Optional - The family name of the user
                - fullname (string)   - The fullname of the user
                - email (string)  Optional - An email address - allow email as root@localhost
                - address (string)  Optional - Postal address
                - phone1 (string)  Optional - Phone 1
                - phone2 (string)  Optional - Phone 2
                - icq (string)  Optional - icq number
                - skype (string)  Optional - skype id
                - yahoo (string)  Optional - yahoo id
                - aim (string)  Optional - aim id
                - msn (string)  Optional - msn number
                - department (string)  Optional - department
                - institution (string)  Optional - institution
                - idnumber (string)  Optional - An arbitrary ID code number perhaps from the institution
                - interests (string)  Optional - user interests (separated by commas)
                - firstaccess (int)  Optional - first access to the site (0 if never)
                - lastaccess (int)  Optional - last access to the site (0 if never)
                - auth (string)  Optional - Auth plugins include manual, ldap, imap, etc
                - confirmed (int)  Optional - Active user: 1 if confirmed, 0 otherwise
                - lang (string)  Optional - Language code such as "en", must exist on server
                - theme (string)  Optional - Theme name such as "standard", must exist on server
                - timezone (string)  Optional - Timezone code such as Australia/Perth, or 99 for default
                - mailformat (int)  Optional - Mail format code is 0 for plain text, 1 for HTML etc
                - description (string)  Optional - User profile description
                - descriptionformat (int)  Optional - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
                - city (string)  Optional - Home city of the user
                - url (string)  Optional - URL of the user
                - country (string)  Optional - Home country code of the user, such as AU or CZ
                - profileimageurlsmall (string)   - User image profile URL - small version
                - profileimageurl (string)   - User image profile URL - big version
                - customfields (List of Dictionary) Optional - User custom fields (also known as user profile fields):
                    - type (string)   - The type of the custom field - text field, checkbox...
                    - value (string)   - The value of the custom field
                    - name (string)   - The name of the custom field
                    - shortname (string)   - The shortname of the custom field - to be able to build the field class in the code
                - preferences (List of Dictionary) Optional - Users preferences:
                    - name (string)   - The name of the preferences
                    - value (string)   - The value of the custom field
            - warnings (List of Dictionary) Optional - list of occurred warnings
                - item (string)  Optional - always set to 'key'
                - itemid (int)  Optional - faulty key name
                - warningcode (string)   - the warning code can be used by the client app to implement specific behaviour
                - message (string)   - untranslated english message to explain the warning
        @raise TypeError: if criteria input parameter type is not a list or is an empty list.
        '''
        if type(criteria)!=type([]) or criteria==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "key" and "value"')
        function = 'core_user_get_users'
        param = ''
        num=0
        reqParameters = ['key', 'value']
        for critery in criteria:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(critery, 'criteria', num, reqParameters)
            num += 1
        return self.connect(function, param)
    
    def get_users_by_field(self, field, values):
        ''' Retrieve users information for a specified unique field - If you want to do a user search, use get_users()
        @param field: the search field can be 'id' or 'idnumber' or 'username' or 'email'
        @type field: String
        @param values: List of values to match with in the specified field
        @type values: List of String
        @return: List of Dictionary. List of retrieved users:
            - id (int)   - ID of the user
            - username (string)  Optional - The username
            - firstname (string)  Optional - The first name(s) of the user
            - lastname (string)  Optional - The family name of the user
            - fullname (string)   - The fullname of the user
            - email (string)  Optional - An email address - allow email as root@localhost
            - address (string)  Optional - Postal address
            - phone1 (string)  Optional - Phone 1
            - phone2 (string)  Optional - Phone 2
            - icq (string)  Optional - icq number
            - skype (string)  Optional - skype id
            - yahoo (string)  Optional - yahoo id
            - aim (string)  Optional - aim id
            - msn (string)  Optional - msn number
            - department (string)  Optional - department
            - institution (string)  Optional - institution
            - idnumber (string)  Optional - An arbitrary ID code number perhaps from the institution
            - interests (string)  Optional - user interests (separated by commas)
            - firstaccess (int)  Optional - first access to the site (0 if never)
            - lastaccess (int)  Optional - last access to the site (0 if never)
            - auth (string)  Optional - Auth plugins include manual, ldap, imap, etc
            - confirmed (int)  Optional - Active user: 1 if confirmed, 0 otherwise
            - lang (string)  Optional - Language code such as "en", must exist on server
            - theme (string)  Optional - Theme name such as "standard", must exist on server
            - timezone (string)  Optional - Timezone code such as Australia/Perth, or 99 for default
            - mailformat (int)  Optional - Mail format code is 0 for plain text, 1 for HTML etc
            - description (string)  Optional - User profile description
            - descriptionformat (int)  Optional - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - city (string)  Optional - Home city of the user
            - url (string)  Optional - URL of the user
            - country (string)  Optional - Home country code of the user, such as AU or CZ
            - profileimageurlsmall (string)   - User image profile URL - small version
            - profileimageurl (string)   - User image profile URL - big version
            - customfields (List of Dictionary) Optional - User custom fields (also known as user profile fields)
                - type (string)   - The type of the custom field - text field, checkbox...
                - value (string)   - The value of the custom field
                - name (string)   - The name of the custom field
                - shortname (string)   - The shortname of the custom field - to be able to build the field class in the code
            - preferences (List of Dictionary) Optional - Users preferences
                - name (string)   - The name of the preferences
                - value (string)   - The value of the custom field
        @raise TypeError: if field input parameter type is not a (string) or is an empty (string) and if values input paramater type is not a list or is an empty list.
        '''
        if type(field)!=type('a') or field=='':
            raise TypeError('field parameter must be a non-empty string')
        if  type(values)!=type([]) or values==[]:
            raise TypeError('values parameter must be a list of (string) with, at least, 1 string')
        function = 'core_user_get_users_by_field'
        param = urllib.urlencode({'field': field})
        num=0
        for value in values:
            param += '&' + self.add_reqParameters(value, 'values', num)
            num += 1
        return self.connect(function, param)
