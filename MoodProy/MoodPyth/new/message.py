from MoodPyth import MoodClass

class message(MoodClass):
    def send_instant_messages(self):
    # Send instant messages
        function = 'core_message_send_instant_messages'
    
    def create_contacts(self):
    # Add contacts to the contact list
        function = 'core_message_create_contacts'
    
    def delete_contacts(self):
    # Remove contacts from the contact list
        function = 'core_message_delete_contacts'
    
    def block_contacts(self):
    # Block contacts
        function = 'core_message_block_contacts'
    
    def unblock_contacts(self):
    # Unblock contacts
        function = 'core_message_unblock_contacts'
    
    def get_contacts(self):
    # Retrieve the contact list
        function = 'core_message_get_contacts'
    
    def search_contacts(self):
    # Search for contacts
        function = 'core_message_search_contacts'
