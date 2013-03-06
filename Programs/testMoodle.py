#!/usr/bin/python
# -*- coding: UTF-8 -*-

# URJC Moodle web service functions test
# Javier Benito García-Mochales

import sys, urllib, httplib, ast, json

web = "docencia.etsit.urjc.es"

token="77246fc17e1198dbd171e7f467dfa908"

user='jbgmbl'
pasw=''           # !!!!!!!! IMPORTANTE: PONER LA CONTASEÑA CORRECTA ¡¡¡¡¡¡¡¡¡¡¡
service="moodle_mobile_app"

if __name__ == "__main__":
    """
    Programa principal
    """
    url="/moodle/login/token.php?username=" + user + "&password=" + pasw + "&service=" + service
    conn = httplib.HTTPConnection(web,80)
    conn.request('GET',url)
    resp = conn.getresponse()
    print resp.read()
    
    conn.close()
