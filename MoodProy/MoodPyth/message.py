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
''' Message class module '''
from MoodPyth import MoodClass
import urllib

class Message(MoodClass):
    '''
    Class with Moodle web services functions that work with messages
    '''
    def block_contacts(self, userids):
        ''' Block contacts.
        @param userids: 1 or more user identifiers to be blocked.
        @type userids: List of Integer
        @return: List of Dictionary. List of warnings that occurred:
            - item string  Optional //item
            - itemid int  Optional //item id
            - warningcode string   //the warning code can be used by the client app to implement specific behaviour
            - message string   //untranslated english message to explain the warning
        @raise TypeError: if userids input parameter type is not a list or is an empty list.
        '''
        if type(userids)!=type([]) or userids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 user id')
        function = 'core_message_block_contacts'
        param = ''
        num=0
        for userid in userids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(userid, 'userids', num)
            num += 1
        return self.connect(function, param)
    
    def create_contacts(self, userids):
        ''' Add contacts to the contact list.
        @param userids: 1 or more user identifiers to add at your contacts list.
        @type userids: List of Integer
        @return: List of Dictionary. List of warnings that occurred:
            - item string  Optional //item
            - itemid int  Optional //item id
            - warningcode string   //the warning code can be used by the client app to implement specific behaviour
            - message string   //untranslated english message to explain the warning
        @raise TypeError: if userids input parameter type is not a list or is an empty list.
        '''
        if type(userids)!=type([]) or userids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 user id')
        function = 'core_message_create_contacts'
        param = ''
        num=0
        for userid in userids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(userid, 'userids', num)
            num += 1
        return self.connect(function, param)
    
    def delete_contacts(self, userids):
        ''' Remove contacts from the contact list. 
        @param userids: 1 or more user identifiers to delete from your contacts list.
        @type userids: List of Integer
        @raise TypeError: if userids input parameter type is not a list or is an empty list.
        '''
        if type(userids)!=type([]) or userids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 user id')
        function = 'core_message_delete_contacts'
        param = ''
        num=0
        for userid in userids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(userid, 'userids', num)
            num += 1
        return self.connect(function, param)
    
    def get_contacts(self):
        ''' Retrieve your contact list. 
        @return: A Dictionary with 3 lists: "online" users, "offline" users and "strangers" users (users that are not in the user's contact list but have sent a message):
            - online (List of Dictionary)  //List of online contacts
                - id int   //User ID
                - fullname string   //User full name
                - profileimageurl string  Optional //User picture URL
                - profileimageurlsmall string  Optional //Small user picture URL
                - unread int   //Unread message count
            - offline (List of Dictionary)  //List of offline contacts
                - id int   //User ID
                - fullname string   //User full name
                - profileimageurl string  Optional //User picture URL
                - profileimageurlsmall string  Optional //Small user picture URL
                - unread int   //Unread message count
            - strangers (List of Dictionary)  //List of users that are not in the user's contact list but have sent a message
                - id int   //User ID
                - fullname string   //User full name
                - profileimageurl string  Optional //User picture URL
                - profileimageurlsmall string  Optional //Small user picture URL
                - unread int   //Unread message count
        '''
        function = 'core_message_get_contacts'
        return self.connect(function, '')
    
    def search_contacts(self, searchtext, onlymycourses=0):
        ''' Search for contacts. 
        @param searchtext: search text string, user's fullname has to match to be found.
        @type searchtext: String.
        @param onlymycourses: Limit search to the user's courses (Default to 0): 1 (yes) or 0 (no)
        @type onlymycourses: Integer.
        @return: List of Dictionary. List of contacts:
            - id int   //User ID
            - fullname string   //User full name
            - profileimageurl string  Optional //User picture URL
            - profileimageurlsmall string  Optional //Small user picture URL
        @bug: if some name matches with the search string throws a HTTP Error 500: Internal Server Error -> fix:
        
        In moodle/message/externallib.php in function search_contacts add this sentence at the beginning:
        
        require_once($CFG->dirroot . '/user/lib.php');
        '''
        function = 'core_message_search_contacts'
        param = urllib.urlencode({'searchtext': searchtext, 'onlymycourses': onlymycourses})
        return self.connect(function, param)

    def send_instant_messages(self, messages):
        ''' Send instant messages.
        @param messages: 1 or more messages and destination user identifiers:
            - touserid int   //id of the user to send the private message
            - text string   //the text of the message
            - textformat int  Default to "1" //text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - clientmsgid string  Optional //your own client id for the message. If this id is provided, the fail message id will be returned to you
        @type messages: List of Dictionary
        @return: List of Dictionary. List of message identifiers with their errors if they happen:
            - msgid int   //test this to know if it succeeds:  id of the created message if it succeeded, -1 when failed
            - clientmsgid string  Optional //your own id for the message
            - errormessage string  Optional //error message - if it failed
        @raise TypeError: if messages input parameter type is not a list or is an empty list.
        '''
        if type(messages)!=type([]) or messages==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "touserid" and "text"')
        function = 'core_message_send_instant_messages'
        param = ''
        num=0
        reqParameters = ['touserid','text']
        optParameters = ['textformat','clientmsgid']
        for message in messages:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(message, 'messages', num, reqParameters)
            param += self.add_optParameters(message, 'messages', num, optParameters)
            num += 1
        return self.connect(function, param)
    
    def unblock_contacts(self, userids):
        ''' Unblock contacts.
        @param userids: 1 or more user identifiers to unblock from your contacts list.
        @type userids: List of Integer
        @raise TypeError: if userids input parameter type is not a list or is an empty list.
        '''
        if type(userids)!=type([]) or userids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 user id')
        function = 'core_message_unblock_contacts'
        param = ''
        num=0
        for userid in userids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(userid, 'userids', num)
            num += 1
        return self.connect(function, param)
    