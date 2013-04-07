import sys, urllib, urllib2, json

class MoodClass():
    def create_token(self, user='', pasw='', service=''):
    # Returns your token asking to moodle and
    # save it in the token variable
        if(user=='' or pasw=='' or service==''):
            raise ValueError('Parameters necesary: user, password, service_short_name')
        url= self.conn + "/moodle/login/token.php?username=" + user + "&password=" + pasw + "&service=" + service
        response = urllib2.urlopen(url)
        response = json.load(response)
        try:
            self.token = response['token']
        except KeyError:
            print 'Connection response: ' + str(response)
            raise ValueError('Incorrect parameters: usename, password or service_short_name')
        return self.token

    def __init__(self, web, token='', user='', pasw='', service=''):
    # Creates the connection with Moodle
        self.conn = web
        self.token = token
        if (self.token==''):
            self.token = self.create_token(user, pasw, service)

    def set_token(self, token):
    # Sets the value of the token
        self.token = token

    def get_token(self):
    # Return token's value
        return self.token

    def connect(self, function, param):
    # POST to Moodle the function and parameters specified
        url = self.conn + '/moodle/webservice/rest/server.php?wstoken='+self.token+"&wsfunction="+function+"&moodlewsrestformat=json"
        req = urllib2.Request(url, param)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        req.add_header("Accept", "application/json")
        response = urllib2.urlopen(req)
        source = json.load(response)
        print response.getcode()
        try:
            raise ValueError('Moodle exception:' + source['errorcode'] + '\n Message: ' + source['message'])
        except TypeError:
            pass
        return source
    
    def close(self):
    # Close the connection with Moodle
        self.conn.close()
    