''' Grade class module '''
from MoodPyth import MoodClass
import urllib

class Grade(MoodClass):
    '''
    Class with Moodle web services functions that works with grades.
    '''
    def get_definitions(self, cmids, areaname, activeonly=0):
        ''' Get grading definitions.
        @param cmids: 1 or more course module ids.
        @type cmids: List of Integer
        @param areaname: area name.
        @type areaname: string
        @param activeonly: Only the active method.
        @type activeonly: Integer
        @return: Dictionary. Returns the definitions for the requested course module ids and warnings if happened:
            - areas (List of Dictionary)  - list of grading areas:
                - cmid (int)   - course module id
                - contextid (int)   - context id
                - component (string)   - component name
                - activemethod (string)  Optional - active method
                - definitions (List of Dictionary)  - definitions
                    - id (int)   - definition id
                    - method (string)   - method
                    - name (string)   - name
                    - description (string)   - description
                    - descriptionformat (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
                    - status (int)   - status
                    - copiedfromid (int)  Optional - copied from id
                    - timecreated (int)   - creation time
                    - usercreated (int)   - user who created definition
                    - timemodified (int)   - last modified time
                    - usermodified (int)   - user who modified definition
                    - timecopied (int)  Optional - time copied
                    - guide (Dictionary) Optional - items
                        - guide_criteria (List of Dictionary)
                            - id (int)   - criterion id
                            - sortorder (int)   - sortorder
                            - description (string)  Optional - description
                            - descriptionformat (int)  Optional - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
                            - shortname (string)   - description
                            - descriptionmarkers (string)  Optional - markers description
                            - descriptionmarkersformat (int)  Optional - descriptionmarkers format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
                            - maxscore double   - maximum score
                        - guide_comment (List of Dictionary) Optional - comments
                            - id (int)   - criterion id
                            - sortorder (int)   - sortorder
                            - description (string)  Optional - description
                            - descriptionformat (int)  Optional - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
                    - rubric (Dictionary) Optional - items
                        - rubric_criteria (List of Dictionary) Optional - definition details
                            - id (int)   - criterion id
                            - sortorder (int)   - sortorder
                            - description (string)  Optional - description
                            - descriptionformat (int)  Optional - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
                            - levels (List of Dictionary) Optional - levels
                                - id (int)   - level id
                                - score double   - score
                                - definition (string)  Optional - definition
                                - definitionformat (int)  Optional - definition format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - warnings (List of Dictionary) Optional - list of warnings
                - item (string)  Optional - item
                - itemid (int)  Optional - item id
                - warningcode (string)   - the warning code can be used by the client app to implement specific behaviour
                - message (string)   - untranslated english message to explain the warning
        @raise TypeError: if cmids input parameter type is not a list or is an empty list.
        @bug: areaname parameter functionality unknown
        '''
        if type(cmids)!=type([]) or cmids==[]:
            raise TypeError('Input must be a list of course module ids (int)')
        function = 'core_grade_get_definitions'
        param = ''
        num=0
        for cmid in cmids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(cmid, 'cmids', num)
            num += 1
        param += '&' + urllib.urlencode({'areaname': areaname})
        if activeonly!=0:
            param += '&' + urllib.urlencode({'activeonly': activeonly})
        return self.connect(function, param)