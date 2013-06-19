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
''' Calendar class module '''
from MoodPyth import MoodClass
import urllib

class Calendar(MoodClass):
    '''
    Class with Moodle web services functions that work with calendar events
    '''
    def create_calendar_events(self, events):
        ''' Create calendar events
        @param events: 1 or more events to create:
            - name (string)  - event name
            - description (string)  Default to "null" - event description
            - format (int)  Default to "1" - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - courseid (int)  Default to "0" - course id
            - groupid (int)  Default to "0" - group id
            - repeats (int)  Default to "0" - number of repeats
            - eventtype (string)  Default to "user" - Event type
            - timestart (int)  Default to actual time - starting event time
            - timeduration (int)  Default to "0" - event duration
            - visible (int)  Default to "1" - visibility
            - sequence (int)  Default to "1" - sequence
        @type events: List of Dictionary
        @return: A dictionary with the events created and possible warnings:
            - events (List of Dictionary) - list of events created:
                - id (int)   - event id
                - name (string)   - event name
                - description (string)  Optional - event description
                - format (int)   - description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
                - courseid (int)   - course id
                - groupid (int)   - group id
                - userid (int)   - user id
                - repeatid (int)  Optional - repeat id
                - modulename (string)  Optional - module name
                - instance (int)   - instance id
                - eventtype (string)   - Event type
                - timestart (int)   - timestart
                - timeduration (int)   - time duration
                - visible (int)   - visible
                - uuid (string)  Optional - unique id of ical events
                - sequence (int)   - sequence
                - timemodified (int)   - time modified
                - subscriptionid (int)  Optional - Subscription id
            - warnings (List of Dictionary) Optional - list of possible warnings for each event created:
                - item (string)  Optional - item
                - itemid (int)  Optional - item id
                - warningcode (string)   - the warning code can be used by the client app to implement specific behavior
                - message (string)   - untranslated English message to explain the warning
        @raise TypeError: if events input parameter type is not a list or is an empty list.
        '''
        if type(events)!=type([]) or events==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "name"')
        function = 'core_calendar_create_calendar_events'
        param = ''
        num=0
        reqParameters = ['name']
        optParameters = ['description','format','courseid','groupid', 'repeats','eventtype','timestart','timeduration','visible','sequence']
        for event in events:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(event, 'events', num, reqParameters)
            param += self.add_optParameters(event, 'events', num, optParameters)
            num += 1
        return self.connect(function, param)

    def delete_calendar_events(self, events):
        '''Delete calendar events
        @param events: 1 or more events to delete:
            - eventid (int)  - Event ID
            - repeat 0/1  - Delete complete series if repeated event
        @type events: List of Dictionary
        @raise TypeError: if events input parameter type is not a list or is an empty list.
        '''
        function = 'core_calendar_delete_calendar_events'
        if type(events)!=type([]) or events==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the keys "eventid" and "repeat"')
        param = ''
        num=0
        reqParameters = ['eventid', 'repeat']
        for event in events:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(event, 'events', num, reqParameters)
            num += 1
        return self.connect(function, param)

    def get_calendar_events(self, eventids=[], courseids=[], groupids=[], userevents=1, siteevents=1, timestart=0, timeend='', ignorehidden=1):
        ''' Get calendar events.
        @param eventids: 0 or more event ids
        @type eventids: List of Integer
        @param courseids: 0 or more course ids for which events will be returned
        @type courseids: List of Integer
        @param groupids: 0 or more group ids for which events should be returned
        @type groupids: List of Integer
        @param userevents: Set to true to return current user's user events
        @type userevents: Integer
        @param siteevents: Set to true to return global events
        @type siteevents: Integer
        @param timestart: Time from which events should be returned
        @type timestart: Integer
        @param timeend: Time to which the events should be returned
        @type timeend: Integer
        @param ignorehidden: Ignore hidden events or not
        @type ignorehidden: Integer
        @return: a dictionary with the events which match with the search parameters and warnings.
        @raise TypeError: if eventids, courseids or groupids input parameters types are not lists.
        @bug: This function only returns events that have been created with web services '''
        function = 'core_calendar_get_calendar_events'
        if type(eventids)!=type([]) or type(courseids)!=type([]) or type(groupids)!=type([]):
            raise TypeError('Input must be lists of integers')
        param = ''
        num=0
        for eventid in eventids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(eventid, 'events[eventids]', num)
            num += 1
        if num!=0 and courseids!=[]:
            param += '&'
        num=0
        for courseid in courseids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(courseid, 'events[courseids]', num)
            num += 1
        if num!=0 and groupids!=[]:
            param += '&'
        num=0
        for groupid in groupids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(groupid, 'events[groupids]', num)
            num += 1
        if userevents==0:
            param += '&' + urllib.urlencode({'options[userevents]': userevents})
        if siteevents==0:
            param += '&' + urllib.urlencode({'options[siteevents]': siteevents})
        if timestart!=0:
            param += '&' + urllib.urlencode({'options[timestart]': timestart})
        if timeend!='':
            param += '&' + urllib.urlencode({'options[timeend]': timeend})
        if ignorehidden==0:
            param += '&' + urllib.urlencode({'options[ignorehidden]': ignorehidden})
        return self.connect(function, param)
