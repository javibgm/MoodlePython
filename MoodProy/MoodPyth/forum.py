''' Forum class module '''
from MoodPyth import MoodClass

class Forum(MoodClass):
    '''
    Class with Moodle web services functions that work with forums
    '''
    def get_forum_discussions(self, forumids):
        ''' Returns a list of forum discussions contained within a given set of forums.
        @param forumids: 1 or more forum identifiers.
        @type forumids: List of Integer
        @return: List of Dictionary - list of forum discussions:
            - id (int)   - Forum id
            - course (int)   - Course id
            - forum (int)   - The forum id
            - name (string)   - Discussion name
            - userid (int)   - User id
            - groupid (int)   - Group id
            - assessed (int)   - Is this assessed?
            - timemodified (int)   - Time modified
            - usermodified (int)   - The id of the user who last modified
            - timestart (int)   - Time discussion can start
            - timeend (int)   - Time discussion ends
            - firstpost (int)   - The first post in the discussion
            - firstuserfullname (string)   - The discussion creators fullname
            - firstuserimagealt (string)   - The discussion creators image alt
            - firstuserpicture (int)   - The discussion creators profile picture
            - firstuseremail (string)   - The discussion creators email
            - subject (string)   - The discussion subject
            - numreplies (string)   - The number of replies in the discussion
            - numunread (string)   - The number of unread posts, blank if this value is not available due to forum settings.
            - lastpost (int)   - The id of the last post in the discussion
            - lastuserid (int)   - The id of the user who made the last post
            - lastuserfullname (string)   - The last person to posts fullname
            - lastuserimagealt (string)   - The last person to posts image alt
            - lastuserpicture (int)   - The last person to posts profile picture
            - lastuseremail (string)   - The last person to posts email
        @raise TypeError: if forumids input parameter type is not a list or is an empty list.
        '''
        if type(forumids)!=type([]) or forumids==[]:
            raise TypeError('Input must be a list of forum IDs (integer)')
        function = 'mod_forum_get_forum_discussions'
        param = ''
        num=0
        for forumid in forumids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(forumid, 'forumids', num)
            num += 1
        return self.connect(function, param)

    def get_forums_by_courses(self, courseids=''):
        ''' Returns a list of forum instances in a provided set of courses,
        if no courses are provided then all the forum instances the user has access to will be returned. 
        @param courseids: 0 or more course identifiers to get their forums.
        @type courseids: List of Integer
        @return: List of Dictionary - list of forum instances:
            - id (int)   - Forum id
            - course (string)   - Course id
            - type (string)   - The forum type
            - name (string)   - Forum name
            - intro (string)   - The forum intro
            - introformat (int)   - intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
            - assessed (int)   - Aggregate type
            - assesstimestart (int)   - Assess start time
            - assesstimefinish (int)   - Assess finish time
            - scale (int)   - Scale
            - maxbytes (int)   - Maximum attachment size
            - maxattachments (int)   - Maximum number of attachments
            - forcesubscribe (int)   - Force users to subscribe
            - trackingtype (int)   - Subscription mode
            - rsstype (int)   - RSS feed for this activity
            - rssarticles (int)   - Number of RSS recent articles
            - timemodified (int)   - Time modified
            - warnafter (int)   - Post threshold for warning
            - blockafter (int)   - Post threshold for blocking
            - blockperiod (int)   - Time period for blocking
            - completiondiscussions (int)   - Student must create discussions
            - completionreplies (int)   - Student must post replies
            - completionposts (int)   - Student must post discussions or replies
            - cmid (int)   - Course module id
        @raise TypeError: if courseids input parameter type is not a list.
        '''
        if type(courseids)!=type([]) and courseids!='':
            raise TypeError('Input must be a list of course IDs (integer)')
        function = 'mod_forum_get_forums_by_courses'
        param = ''
        num=0
        for courseid in courseids:
            if num!=0:
                param += '&'
            param += self.add_reqParameters(courseid, 'courseids', num)
            num += 1
        return self.connect(function, param)

