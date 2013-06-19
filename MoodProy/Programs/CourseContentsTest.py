'''
Created on 07/06/2013

@author: javi
'''
import urllib2
import urllib

if __name__ == '__main__':
    url = 'http://adry3000.dyndns.org/moodle/webservice/rest/server.php'
    function = 'core_course_get_contents'
    token = 'f03f665848ef2a85e3aee8a1db198ac0'
    param = urllib.urlencode({'wstoken':token,'wsfunction':function,'courseid':'2'})
    req = urllib2.Request(url, param)
    response = urllib2.urlopen(req)
    print response.read()