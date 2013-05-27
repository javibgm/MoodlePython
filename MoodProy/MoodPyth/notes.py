from MoodPyth import MoodClass

class Notes(MoodClass):
    def create_notes(self, notes):
        ''' Create notes
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
        
    def delete_notes(self):
    # Delete notes
        function = 'core_notes_delete_notes'
    
    def get_notes(self):
    # Get notes
        function = 'core_notes_get_notes'
    
    def update_notes(self):
    # Update notes
        function = 'core_notes_update_notes'
