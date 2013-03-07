#!/usr/bin/python
# -*- coding: UTF-8 -*-

# URJC Moodle web service functions test
# Javier Benito García-Mochales

import MoodLib

#web = "docencia.etsit.urjc.es"
web = 'http://campusonline.urjc.es'

token="77246fc17e1198dbd171e7f467dfa908"

user='j.benitogar'
pasw='J@vi3r008'           # !!!!!!!! IMPORTANTE: PONER USUARIO Y CONTASEÑA ¡¡¡¡¡¡¡¡¡¡¡
service="moodle_mobile_app"

if __name__ == "__main__":
    """
    Programa principal
    """
    url="/moodle/login/token.php?username=" + user + "&password=" + pasw + "&service=" + service
    m = MoodLib.MoodLib(web, user, pasw, service)
    
    conn.close()
