######################## BEGIN LICENSE BLOCK ########################
# This file is part of MoodPyth library.
#
# MoodPyth library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# MoodPyth library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with MoodPyth.  If not, see <http://www.gnu.org/licenses/>.
######################### END LICENSE BLOCK #########################
# Copyright 2013 Javier Benito Garcia-Mochales
''' Cohort class module '''
from MoodPyth import MoodClass
import urllib

class Cohort(MoodClass):
    '''
    Class with Moodle web services functions that work with cohorts
    '''
    def add_cohort_members(self, members):
        ''' Adds users to cohorts
        @param members: specifies for each cohort(determined by its id or its idnumber) what user (determined by its id or its username) add.
            - cohorttype (Dictionary) - specifies the cohort where to add
                - type (string) - The name of the cohort field specified. Possible values are:
                    - "id"  - Numeric value of the cohortid assigned automatically by moodle
                    - "idnumber"  - Alphanumeric value of idnumber assigned to the cohort manually
                - value (string)   - The value of the cohort filed specified by the 'type' parameter
            - usertype (Dictionary) - specifies the user to be added
                - type (string) - The name of the user field specified. It can be:
                    - "id"  - Numeric value of user's id
                    - "username"  - Alphanumeric value of username
                - value (string)  - The value of the cohort filed specified by the 'type' parameter
        @type members: List of Dictionary
        @return: Dictionary. Warnings about cohorts where users have been added:
            - warnings (List of Dictionary) Optional - possible happened warnings
                - item (string)  Optional - item
                - itemid (int)  Optional - item id
                - warningcode (string)   - the warning code can be used by the client app to implement specific behavior
                - message (string)   - untranslated English message to explain the warning
        @raise TypeError: if members input parameter type is not a list or is an empty list.
        '''
        if type(members)!=type([]) or members==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "cohorttype" and "usertype"')
        function = 'core_cohort_add_cohort_members'
        param = ''
        num=0
        for member in members:
            if num!=0:
                param += '&'
            param += urllib.urlencode({'members['+str(num)+'][cohorttype][type]': member['cohorttype']['type']}) + '&'
            param += urllib.urlencode({'members['+str(num)+'][cohorttype][value]': member['cohorttype']['value']}) + '&'
            param += urllib.urlencode({'members['+str(num)+'][usertype][type]': member['usertype']['type']}) + '&'
            param += urllib.urlencode({'members['+str(num)+'][usertype][value]': member['usertype']['value']}) + '&'
            num += 1
        return self.connect(function, param)
    
    def create_cohorts(self, cohorts):
        ''' Creates new cohorts.
        @param cohorts: 1 or more user cohorts to create.
            - type (string) - category type field name. Possible values are:
                - "id"  - numeric value of course category id
                - "idnumber" - alphanumeric value of idnumber course category
                - "system" - value ignored
            - value (string) - the value of the category type filed (this parameter is necessary even if you select the "system" cohort type)
            - name (string) - cohort name
            - idnumber (string) - cohort idnumber
            - description (string)  Optional - cohort description
            - descriptionformat (int)  Default to "1" - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @type cohorts: List of Dictionary
        @return: List of Dictionary -  created cohorts list:
            - id (int) - cohort id
            - name (string) - cohort name
            - idnumber (string) - cohort idnumber
            - description (string) - cohort description
            - descriptionformat (int) - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @raise TypeError: if cohorts input parameter type is not a list or is an empty list.
        '''
        if type(cohorts)!=type([]) or cohorts==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "type", "value", "name" and "idnumber"')
        function = 'core_cohort_create_cohorts'
        param = ''
        num=0
        reqParameters = ['name','idnumber']
        optParameters = ['description','descriptionformat']
        for cohort in cohorts:
            if num!=0:
                param += '&'
            param += urllib.urlencode({'cohorts['+str(num)+'][categorytype][type]': cohort['type']}) + '&'
            param += urllib.urlencode({'cohorts['+str(num)+'][categorytype][value]': cohort['value']}) + '&'
            param += self.add_reqParameters(cohort, 'cohorts', num, reqParameters)
            param += self.add_optParameters(cohort, 'cohorts', num, optParameters)
            num += 1
        return self.connect(function, param)
    
    def delete_cohort_members(self, members):
        ''' Deletes cohort members.
        @param members: cohort and user ids to unassign user from cohort.
            - cohortid (int)   - cohort record id
            - userid (int)   - user id
        @type members: List of Dictionary
        @raise TypeError: if members input parameter type is not a list or is an empty list.
        '''
        if type(members)!=type([]) or members==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "cohortid" and "userid"')
        function = 'core_cohort_delete_cohort_members'
        param = ''
        num=0
        reqParameters = ['cohortid','userid']
        for member in members:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(member, 'members', num, reqParameters)
            num += 1
        return self.connect(function, param)
    
    def delete_cohorts(self, cohortids):
        ''' Deletes all specified cohorts.
        @param cohortids: 1 or more of cohort ids to delete.
        @type cohortids: List of Integer
        @raise TypeError: if cohortids input parameter type is not a list or is an empty list.
        '''
        if type(cohortids)!=type([]) or cohortids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 cohort id')
        function = 'core_cohort_delete_cohorts'
        param = ''
        num=0
        for cohortid in cohortids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(cohortid, 'cohortids', num)
            num += 1
        return self.connect(function, param)
    
    def get_cohort_members(self, cohortids):
        ''' Returns cohort members.
        @param cohortids: 1 or more of cohort ids to get its members.
        @type cohortids: List of Integer
        @return: List of Dictionary. For each cohort, its ID and its members ID are returned:
            - cohortid (int)   - cohort record id
            - userids (List of Integer)  - users ids
        @raise TypeError: if cohortids input parameter type is not a list or is an empty list.
        '''
        if type(cohortids)!=type([]) or cohortids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 cohort id')
        function = 'core_cohort_get_cohort_members'
        param = ''
        num=0
        for cohortid in cohortids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(cohortid, 'cohortids', num)
            num += 1
        return self.connect(function, param)
    
    def get_cohorts(self, cohortids):
        ''' Returns cohort details.
        @param cohortids: 1 or more of cohort ids to get its details.
        @type cohortids: List of Integer
        @return: List of Dictionary. For each cohort, its details are returned:
            - id (double)   - ID of the cohort
            - name (string)   - cohort name
            - idnumber (string)   - cohort idnumber
            - description (string)   - cohort description
            - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @raise TypeError: if cohortids input parameter type is not a list or is an empty list.
        '''
        if type(cohortids)!=type([]) or cohortids==[]:
            raise TypeError('Input must be a list of integers with, at least, 1 cohort id')
        function = 'core_cohort_get_cohorts'
        param = ''
        num=0
        for cohortid in cohortids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(cohortid, 'cohortids', num)
            num += 1
        return self.connect(function, param)
    
    def update_cohorts(self, cohorts):
        ''' Updates existing cohorts.
        @param cohorts: 1 or more user cohorts to create.
            - id (double)   - ID of the cohort
            - type (string) - new category type field name. Possible values are:
                - "id"  - numeric value of course category id
                - "idnumber" - alphanumeric value of idnumber course category
                - "system" - value ignored
            - value (string) - new value for the category type filed (this parameter is necessary even if you select the "system" cohort type)
            - name (string) - new cohort name
            - idnumber (string) - new cohort idnumber
            - description (string)  Optional - new cohort description
            - descriptionformat (int)  Default to "1" - new description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @type cohorts: List of Dictionary
        @raise TypeError: if cohorts input parameter type is not a list or is an empty list.
        '''
        if type(cohorts)!=type([]) or cohorts==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "id", "type", "value", "name" and "idnumber"')
        function = 'core_cohort_update_cohorts'
        param = ''
        num=0
        reqParameters = ['id','name','idnumber']
        optParameters = ['description','descriptionformat']
        for cohort in cohorts:
            if num!=0:
                param += '&'
            param += urllib.urlencode({'cohorts['+str(num)+'][categorytype][type]': cohort['type']}) + '&'
            param += urllib.urlencode({'cohorts['+str(num)+'][categorytype][value]': cohort['value']}) + '&'
            param += self.add_reqParameters(cohort, 'cohorts', num, reqParameters)
            param += self.add_optParameters(cohort, 'cohorts', num, optParameters)
            num += 1
        return self.connect(function, param)
