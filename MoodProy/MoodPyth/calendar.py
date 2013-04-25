from MoodPyth import MoodClass
import urllib

class calendar(MoodClass):
    def create_calendar_events(self, events):
        ''' Create calendar events '''
        function = 'core_calendar_create_calendar_events'
        if type(events)!=type([]) or events==[]:
            raise TypeError('Input must be a list of dictionaries with, at least, 1 dictionary with the key "name"')
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
        '''Delete calendar events '''
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
        ''' Get calendar events '''
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
        print param
        return self.connect(function, param)
