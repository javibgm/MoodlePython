from MoodPyth import MoodClass
import urllib

class Cohorts(MoodClass):
    def add_cohort_members(self):
        function = 'core_cohort_add_cohort_members'
    
    def create_cohorts(self, cohorts):
        ''' Creates new cohorts
        @return: List of Dictionary
            - id int - cohort id
            - name string - cohort name
            - idnumber string - cohort idnumber
            - description string - cohort description
            - descriptionformat int - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        @param cohorts: 1 or more user cohorts to create.
        @type userids: List of Dictionary.
            - type string - category type field name. Possible values are:
                - id - numeric value of course category id
                - idnumber - alphanumeric value of idnumber course category
                - system - value ignored
            - value string - the value of the category type filed
            - name string - cohort name
            - idnumber string - cohort idnumber
            - description string  Optional - cohort description
            - descriptionformat int  Default to "1" - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
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
        print param
        return self.connect(function, param)
    
    def delete_cohort_members(self):
        function = 'core_cohort_delete_cohort_members'
    
    def delete_cohorts(self):
        function = 'core_cohort_delete_cohorts'
    
    def get_cohortsget_cohort_members(self):
        function = 'core_cohort_get_cohort_members'
    
    def get_cohorts(self):
        function = 'core_cohort_get_cohorts'
    
    def update_cohorts(self):
        function = 'core_cohort_update_cohorts'
    