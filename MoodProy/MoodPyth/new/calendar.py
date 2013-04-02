from MoodPyth import MoodClass

class calendar(MoodClass):
    def delete_calendar_events(self):
    # Delete calendar events
        function = 'core_calendar_delete_calendar_events'
        return function

    def get_calendar_events(self):
    # Get calendar events
        function = 'core_calendar_get_calendar_events'

    def create_calendar_events(self):
    # Create calendar events
        function = 'core_calendar_create_calendar_events'