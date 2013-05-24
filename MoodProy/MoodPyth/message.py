''' Message class module '''
from MoodPyth import MoodClass
import urllib

class Message(MoodClass):
    '''
    Class with Moodle web services functions that work with messages
    '''
    def block_contacts(self, userids):
        ''' Block contacts.
        @return: List of warnings.
        @param userids: 1 or more user identifiers.
        @type userids: List of Integer '''
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
        @return: List of warnings.
        @param userids: 1 or more user identifiers.
        @type userids: List of Integer '''
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
        @param userids: 1 or more user identifiers.
        @type userids: List of Integer '''
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
        ''' Retrieve the contact list. 
        @return: Dictionary with 3 lists: "online" users, "offline" users and "strangers" users (users that are not in the user's contact list but have sent a message)'''
        function = 'core_message_get_contacts'
        return self.connect(function, '')
    
    def search_contacts(self, searchtext, onlymycourses=0):
        ''' Search for contacts. 
        @param searchtext: search text string, user's fullname has to match to be found.
        @type searchtext: String.
        @param onlymycourses: Limit search to the user's courses (Default to 0).
        @type onlymycourses: Integer 1 (yes) or 0 (no).
        @return: List of contacts.
        @bug: if some name matches with the search string throws a HTTP Error 500: Internal Server Error '''
        function = 'core_message_search_contacts'
        param = urllib.urlencode({'searchtext': searchtext, 'onlymycourses': onlymycourses})
        return self.connect(function, param)

    def send_instant_messages(self, messages):
        ''' Send instant messages.
        @param messages: 1 or more messages and destination user identifiers.
        @type messages: List of Dictionaries.
        @return: List of message identifiers with their errors if they happen. '''
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
        @param userids: 1 or more user identifiers.
        @type userids: List of Integer'''
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
    