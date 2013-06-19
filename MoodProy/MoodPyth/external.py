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
''' External class module '''
from MoodPyth import MoodClass
import urllib

class External(MoodClass):
    '''
    Class with Moodle web services functions that provide external functionalities.
    '''
    def get_string(self, stringid, component='', lang='', stringparams=[]):
        ''' Return a translated string - similar to core get_string() call
        @param stringid: string identifier
        @type stringid: string
        @param component: component
        @type component: string
        @param lang: language
        @type lang: string
        @param stringparams: the definition of a string parameter (i.e. {$a->name})
            - name (string)  Optional - parameter name. if the string expect only one $a parameter then don't send this field, just send the value.
            - value (string)   - parameter value
        @type stringparams: List of Dictionary
        @return: String. Translated string.
        @raise TypeError: if stringid input parameter type is not a string or is an empty string.
        @bug: always return an invalidparameter exception
        '''
        if type(stringid)!=type('') or stringid=='':
            raise TypeError('stringid input parameter must be a string.')
        function = 'core_get_string'
        param = urllib.urlencode({'stringid': stringid})
        if component!='':
            param += '&' + urllib.urlencode({'component': component})
        if lang!='':
            param += '&' + urllib.urlencode({'lang': lang})
        num=0
        optParameters = ['name','value']
        for stringparam in stringparams:
            param += self.add_optParameters(stringparam, 'stringparams', num, optParameters)
            num += 1
        return self.connect(function, param)
    
    def get_strings(self, strings):
        ''' Return some translated strings.
        @param strings: List of strings to translate:
            - stringid (string)   - string identifier
            - component (string)  Default to "moodle" - component
            - lang (string)  Default to "null" - lang
            - stringparams (List of Dictionary) Default to "Array()" - the definition of a string parameter (i.e. {$a->name})
                - name (string)  Optional -  parameter name. if the string expect only one $a parameter then don't send this field, just send the value.
                - value (string)   - parameter value
        @type strings: List of Dictionary
        @raise TypeError: if strings input parameter type is not a list or is an empty list.
        '''
        if type(strings)!=type([]) or strings==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "stringid"')
        function = 'core_get_strings'
        param = ''
        num=0
        reqParameters = ['stringid']
        optParameters = ['component','lang']
        for string in strings:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(string, 'strings', num, reqParameters)
            param += self.add_optParameters(string, 'strings', num, optParameters)
            if 'stringparams' in string:
                numformat = 0
                for stringparam in string['stringparams']:
                    param += self.add_optParameters(stringparam,'strings['+str(num)+'][stringparams]',numformat,['name','value'])
                    numformat += 1
            num += 1
        return self.connect(function, param)

    
    def get_component_strings(self, component, lang=''):
        ''' Return all raw strings (with {$a->xxx}) for a specific component
        @param component: component
        @type component: string
        @param lang: language
        @type lang: string
        @return: List of Dictionary. Raw component strings:
            - stringid (string)   - string id
            - string (string)   - translated string
        @raise TypeError: if component input parameter type is not a string or is an empty string.
        '''
        if type(component)!=type('') or component=='':
            raise TypeError('component input parameter must be a string.')
        function = 'core_get_component_strings'
        param = urllib.urlencode({'component': component})
        if lang!='':
            param += '&' + urllib.urlencode({'lang': lang})
        return self.connect(function, param)