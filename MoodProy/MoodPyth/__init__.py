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
        except (TypeError, KeyError):
            pass
        return source
    
    def close(self):
    # Close the connection with Moodle
        self.conn.close()
    
    def check_reqParameters(self, item, paramnames):
    # Auxiliary function: checks if all required parameters(paramnames) are in the dictionary(item) and prints missing parameters (not used)
        check = True
        notfound = ''
        for paramname in paramnames:
            check = check and (paramname in item)
            if not (paramname in item):
                notfound += paramname + ' '
        if (not check):
            print 'Required parameters not found: ' + notfound
        return check
    
    def add_reqParameters(self, item, itemname, num, paramnames=''):
    # Auxiliary function: adds required function parameters
        param = ''
        paramnum = 0
        if(paramnames!=''):        # if we have more than 1 required parameter in a dictionary
            for paramname in paramnames:
                if paramnum != 0:   # add a & if is not the first parameter
                    param += '&'
                param += urllib.urlencode({itemname + '['+str(num)+'][' + paramname + ']': item[paramname]})
                paramnum+=1
        elif (paramnames==''):
            param = urllib.urlencode({itemname + '['+str(num)+']': item})
        return param
    
    def add_optParameters(self, item, itemname, num, paramnames=''):
    # Auxiliary function: adds optional function parameters contained in item
        param = ''
        for paramname in paramnames:
            param += self.add_optParameter(item, itemname, num, paramname)
        return param

    def add_optParameter(self, item, itemname, num, paramname=''):
    # Auxiliary function: add an optional function parameter if exists in the item dictionary
        param = ''
        if((paramname in item) and (paramname!='')):
            param = '&' + urllib.urlencode({itemname + '['+str(num)+'][' + paramname + ']': item[paramname]})
        elif ((paramname in item) and (paramname=='')):
            param = '&' + urllib.urlencode({itemname + '['+str(num)+']': item})
        return param