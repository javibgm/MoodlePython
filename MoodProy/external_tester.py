'''
'''
from MoodPyth.MoodLib import MoodLib
from MoodPyth.aux import show
from config import info,users

def test_get_string(test):
    if test == '0':
        # Get a string manually
        print "Required parameter: stringid"
        show(t.get_string(raw_input()))
    elif test == '1':
        # Get a string manually with optional parameters
        print "Required parameter: stringid, component, lang, stringparams name, stringparams value"
        show(t.get_string(raw_input(), raw_input(), raw_input(),
                          [{'name':raw_input(),'value':raw_input()}]))
    elif test == '2':
        show(t.get_string('groups',
                          stringparams=[{'name':'stringname','value':'id'}]))
    elif test == '3':
        show(t.get_string('groups'))
        
def test_get_strings(test):
    if test == '0':
        # Get a string manually
        print "Required parameter: stringid"
        show(t.get_strings([{'stringid':raw_input()}]))
    elif test == '1':
        # Get a string manually with optional parameters
        print "Required parameter: stringid, component, lang, stringparams name, stringparams value"
        show(t.get_strings([{'stringid':raw_input(),
                           'component':raw_input(),
                           'lang': raw_input(),
                           'stringparams':[{'name':raw_input(),'value':raw_input()}]
                          }]))
    elif test == '2':
        print "Required parameter: stringid, component, lang, stringparams name, stringparams value"
        show(t.get_strings([{'stringid':'groups',
                           'stringparams':[{'name':'stringname','value':'stringvalue'}]
                          }]))
    elif test == '3':
        show(t.get_strings([{'stringid':'groupid'}]))
    #Errors
    elif test == '4':
        #Produces a 500 internal server error
        print "Required parameter: stringid, component, lang, stringparams name, stringparams value"
        show(t.get_strings([{'stringid':'groups',
                           'stringparams':[{'name':'','value':'stringvalue'}]
                          }]))

def test_get_component_strings():
    print "Required parameter: component"
    show(t.get_component_strings(raw_input()))

if __name__ == '__main__':
    t = MoodLib(info['web'], users['manager']['token'])
    #test_get_string(raw_input())
    #test_get_strings(raw_input())
    #test_get_component_strings()