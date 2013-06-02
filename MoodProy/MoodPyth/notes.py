''' Notes class module '''
from MoodPyth import MoodClass

class Notes(MoodClass):
    '''
    Class with Moodle web services functions that work with notes
    '''
    def create_notes(self, notes):
        ''' Create notes about some users.
        @param notes: 1 or more notes to create:
            - userid (int)   - id of the user the note is about
            - publishstate (string)   - where this note is shown. Possible values are: 'personal', 'course' or 'site'
            - courseid (int)   - course id of the note (in Moodle a note can only be created into a course, even for site and personal notes)
            - text (string)   - the text of the message. Can be normal text or HTML code
            - format (int)  Default to "1" - text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - clientnoteid (string)  Optional - your own client id for the note. If this id is provided, the fail message id will be returned to you
        @type notes: List of Dictionary
        @return: List of Dictionary. Notes id if they have been successfully created and errors if have happened:
            - clientnoteid (string)  Optional - your own id for the note
            - noteid (int)   - test this to know if it success: id of the created note when successed, -1 when failed
            - errormessage (string)  Optional - error message - if failed
        @raise TypeError: if notes input parameter type is not a list or is an empty list.
        '''
        if type(notes)!=type([]) or notes==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "userid", "publishstate", "courseid" and "text"')
        function = 'core_notes_create_notes'
        param = ''
        num=0
        reqParameters = ['userid','publishstate','courseid','text']
        optParameters = ['format','clientnoteid']
        for note in notes:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(note, 'notes', num, reqParameters)
            param += self.add_optParameters(note, 'notes', num, optParameters)
            num += 1
        return self.connect(function, param)
        
    def delete_notes(self, notes):
        ''' Delete notes about users.
        @param notes: 1 or more note Ids to be deleted.
        @type notes: List of Integer
        @return: List of Dictionary. Warnings if happened.
            - item (string)  Optional - item is always 'note'
            - itemid (int)  Optional - When errorcode is savedfailed the note could not be modified.When errorcode is badparam, an incorrect parameter was provided.When errorcode is badid, the note does not exist
            - warningcode (string)   - errorcode can be badparam (incorrect parameter), savedfailed (could not be modified), or badid (note does not exist)
            - message (string)   - untranslated English message to explain the warning
        @raise TypeError: if notes input parameter type is not a list or is an empty list.
        @bug: always return an invalidparameter exception -> fix: in moodle/notes/externallib.php:
        
        line 229: $params = self::validate_parameters(self::delete_notes_parameters(), $notes);
        
        changed to: $params = self::validate_parameters(self::delete_notes_parameters(), array('notes'=>$notes));
        '''
        if type(notes)!=type([]) or notes==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 note id')
        function = 'core_notes_delete_notes'
        param = ''
        num=0
        for note in notes:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(note, 'notes', num)
            num += 1
        return self.connect(function, param)
    
    def get_notes(self, notes):
        ''' Get notes about users.
        @param notes: 1 or more note Ids to get information about them.
        @type notes: List of Integer
        @return: Dictionary. Notes and Warnings if happened.
            - notes (List of Dictionary) - list of notes:
                - noteid (int)  Optional - id of the note
                - userid (int)  Optional - id of the user the note is about
                - publishstate (string)  Optional - where this note is shown. Possible values are: 'personal', 'course' or 'site'
                - courseid (int)  Optional - course id of the note
                - text (string)  Optional - the text of the message - text or HTML
                - format (int)  Optional - text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - warnings (List of Dictionary) Optional - list of warnings if happened
                - item (string)  Optional - item is always 'note'
                - itemid (int)  Optional - When errorcode is savedfailed the note could not be modified.When errorcode is badparam, an incorrect parameter was provided.When errorcode is badid, the note does not exist
                - warningcode (string)   - errorcode can be badparam (incorrect parameter), savedfailed (could not be modified), or badid (note does not exist)
                - message (string)   - untranslated English message to explain the warning
        @raise TypeError: if notes input parameter type is not a list or is an empty list.
        @bug: always return an invalidparameter exception -> fix: in moodle/notes/externallib.php:
        
        line 295: $params = self::validate_parameters(self::get_notes_parameters(), $notes);
        
        changed to: $params = self::validate_parameters(self::get_notes_parameters(), array('notes'=>$notes));
        @bug: if you try to get a non-existing note, it will return an exception (Invalid response value detected),
        but it should return a warning in the response data structure 
        '''
        if type(notes)!=type([]) or notes==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 note id')
        function = 'core_notes_get_notes'
        param = ''
        num=0
        for note in notes:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(note, 'notes', num)
            num += 1
        return self.connect(function, param)
    
    def update_notes(self, notes=[]):
        ''' Update notes about users.
        @param notes: 0 or more notes to update.
            - id (int)   - id of the note
            - publishstate (string)   - where this note is shown. Possible values are: 'personal', 'course' or 'site'
            - text (string)   - the text of the message - text or HTML
            - format (int)  Default to "1" - text format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @type notes: List of Dictionary
        @return: List of Dictionary. Warnings if happened.
            - item (string)  Optional - item is always 'note'
            - itemid (int)  Optional - When errorcode is savedfailed the note could not be modified.When errorcode is badparam, an incorrect parameter was provided.When errorcode is badid, the note does not exist
            - warningcode (string)   - errorcode can be badparam (incorrect parameter), savedfailed (could not be modified), or badid (note does not exist)
            - message (string)   - untranslated English message to explain the warning
        @raise TypeError: if notes input parameter type is not a list.
        '''
        if type(notes)!=type([]):
            raise TypeError('Input must be a list of notes')
        function = 'core_notes_update_notes'
        param = ''
        num=0
        reqParameters = ['id','publishstate','text']
        optParameters = ['format']
        for note in notes:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(note, 'notes', num, reqParameters)
            param += self.add_optParameters(note, 'notes', num, optParameters)
            num += 1
        return self.connect(function, param)
