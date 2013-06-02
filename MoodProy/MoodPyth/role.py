''' Role class module '''
from MoodPyth import MoodClass

class Role(MoodClass):
    '''
    Class with Moodle web services functions that work with roles
    '''
    def assign_roles(self, assignments):
        ''' Manual role assignments to users.
        @param assignments: 1 or more role assignments:
            - roleid (int)   - Role to assign to the user
            - userid (int)   - The user that is going to be assigned
            - contextid (int)   - The context to assign the user role in.
            Remember that contextid only can be one of the contexts where the role specified by roleid is able to be assigned.
            For example, to assign a role that only can be assigned in a course, the contextid must be a course context
        @type assignments: List of Dictionaries
        @raise TypeError: if assignments input parameter type is not a list or is an empty list.
        '''
        if type(assignments)!=type([]) or assignments==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "roleid", "userid" and "contextid"')
        function = 'core_role_assign_roles'
        param = ''
        num=0
        reqParameters = ['roleid', 'userid', 'contextid']
        for assignment in assignments:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(assignment, 'assignments', num, reqParameters)
            num += 1
        return self.connect(function, param)
        
    
    def unassign_roles(self, unassignments):
        ''' Unassign roles from users.
        @param unassignments: 1 or more role unassignments:
            - roleid (int)   - Role to unassign to the user
            - userid (int)   - The user that is going to be unassigned
            - contextid (int)   - The context to unassign the user role in. Contextid = 1 is system context, the rest of contextids depend of the Moodle site.
            Remember that contextid only can be one of the contexts where the role specified by roleid is able to be assigned.
            For example, to unassign a role that only can be assigned in a course, the contextid must be a course context
        @type unassignments: List of Dictionaries
        @raise TypeError: if unassignments input parameter type is not a list or is an empty list.
        '''
        if type(unassignments)!=type([]) or unassignments==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "roleid", "userid" and "contextid"')
        function = 'core_role_unassign_roles'
        param = ''
        num=0
        reqParameters = ['roleid', 'userid', 'contextid']
        for unassignment in unassignments:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(unassignment, 'unassignments', num, reqParameters)
            num += 1
        return self.connect(function, param)