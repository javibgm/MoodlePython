from MoodProy import *

class string(MoodClass):
    def get_string(self):
    # Return a translated string - similar to core get_string() call
        function = 'core_get_string'

	def get_strings(self):
    # Return some translated strings - like several core get_string() calls
        function = 'core_get_strings'
	
	def get_component_strings(self):
	# Return all raw strings (with {$a->xxx}) for a specific component - similar to core get_component_strings() call
        function = 'core_get_component_strings'
