#!/usr/bin/python
# -*- coding: UTF-8 -*-

# URJC Moodle web service functions test
# Javier Benito García-Mochales

import MoodLib

#web = "docencia.etsit.urjc.es"
web = 'http://campusonline.urjc.es'

token="77246fc17e1198dbd171e7f467dfa908"
service="moodle_mobile_app"

if __name__ == "__main__":
    """
    Programa principal
    """
    print 'Insert user'
    user = raw_input()
    print 'Insert pasword'
    pasw = raw_input()
    m = MoodLib.MoodLib(web, user, pasw, service)
