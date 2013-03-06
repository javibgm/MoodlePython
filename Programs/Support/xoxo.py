# -*- coding: utf-8 -*-
"""xoxo.py - a utility module for transforming to and from the XHTMLOutlines format XOXO
toXOXO takes a Python datastructure (tuples, lists or dictionaries, arbitrarily nested) and returns a XOXO representation of it.
fromXOXO parses an XHTML file for a xoxo list and returns the structure
"""
__version__ = "0.8"
__date__ = "2004-10-05"
__author__ = "Kevin Marks <kmarks@technorati.com>"
__copyright__ = "Copyright 2004, Kevin marks & Technorati"
__license__ = "http://creativecommons.org/licenses/by/2.0/ CC-by-2.0], [http://www.apache.org/licenses/LICENSE-2.0 Apache 2.0"
__credits__ = """Tantek Çelik and Mark Pilgrim for data structure"""
__history__ = """
TODO: add <title> tag
TODO: add a proper profile link
0.8 work in unicode then render to utf-8
0.7 initial encoding support - just utf-8 for now
0.6 support the special behaviour for url properties  to/from <a>
0.5 fix some awkward side effects of whitespace and text outside our expected tags; simplify writing code
0.4 add correct XHTML headers so it validates
0.3 read/write version; fixed invlaid nested list generation;
0.1 first write-only version
 """

try:
    True, False
except NameError:
    True, False = not not 1, not 1
containerTags={'ol':False,'ul':False,'dl':False}
import sgmllib, urllib, urlparse, re
def makeXOXO(struct,className=None,depth=0):
    s=u''
    if isinstance(struct,list) or isinstance(struct,tuple):
        if className:
            s += u'<ol class="%s">' % className
        else:
            s+= u"<ol>"
    if isinstance(struct,dict):
        d=struct.copy()
        if d.has_key('url'):
            s+=u'<a href="%s" ' % d['url']
            text =  d.get('text',d.get('title',d['url']))
            for attr in ('title','rel','type'):
                if d.has_key(attr):
                    xVal = makeXOXO(d[attr],None,depth+1)
                    s +=u'%s="%s" ' % (attr,xVal)
                    del d[attr]
            s +=u'>%s</a>' % makeXOXO(text,None,depth+1)
            if d.has_key('text'):
                del d['text']
            del d['url']
        if len(d):
            s +=u"<dl>"
            for key,value in d.items():
                xVal = makeXOXO(value,None,depth+1)
                s+= u'<dt>%s</dt><dd>%s</dd>' % (key, xVal)
            s +=u"</dl>"
    elif type(struct) ==type((1,))or type(struct) ==type([1,]):
        for item in struct:
            s+=u"<li>" + makeXOXO(item,None,depth+1)+"</li>"
        s +=u"</ol>"
    elif type(struct) == type(u'unicode'):
        s+=struct
    else:
        if not type(struct)==type(' '):
            struct=str(struct)
        try:
            s+=unicode(struct,'utf-8')
        except:
            s+=unicode(struct,'windows_1252')
    return s
class xoxoParser(sgmllib.SGMLParser):
    def __init__(self):
        sgmllib.SGMLParser.__init__(self)
        self.structs=[]
        self.xostack=[]
        self.textstack=['']
    def normalize_attrs(self, attrs):
        attrs = [(k.lower(), sgmllib.charref.sub(lambda m: chr(int(m.groups()[0])), v).strip()) for k, v in attrs]
        attrs = [(k, k in ('rel','type') and v.lower() or v) for k, v in attrs]
        return attrs
    def pushStruct(self,struct):
        if type(struct) == type({}) and len(struct)==0 and len(self.structs) and type(self.structs[-1]) == type({}) and self.structs[-1].has_key('url'):
            self.xostack.append(self.structs[-1]) # put back the <a>-made one for extra def's
        else:
            self.structs.append(struct)
            self.xostack.append(self.structs[-1])
    def start_a(self,attrs):
        attrsD = dict(self.normalize_attrs(attrs))
        attrsD['url']= attrsD.get('href','')
        del attrsD['href']
        self.pushStruct(attrsD)
        self.textstack.append('')
    def end_a(self):
        val = self.textstack.pop()
        if val: 
            if self.xostack[-1].get('title','') == val:
                val=''
            if self.xostack[-1]['url'] == val:
                val=''
            if val:
                self.xostack[-1]['text']=val
        self.xostack.pop()
    def start_dl(self,attrs):
        self.pushStruct({})
    def end_dl(self):
        self.xostack.pop()
    def start_ol(self,attrs):
        self.pushStruct([])
    def end_ol(self):
        self.xostack.pop()
    def start_ul(self,attrs):
        self.pushStruct([])
    def end_ul(self):
        self.xostack.pop()
    def start_li(self,attrs):
        self.textstack.append('')
    def end_li(self):
        val = self.textstack.pop()
        if self.structs[-1] != self.xostack[-1]:
            val = self.structs.pop()
        self.xostack[-1].append(val)
    def start_dt(self,attrs):
        self.textstack.append('')
    def end_dt(self):
        pass
    def start_dd(self,attrs):
        self.textstack.append('')
    def end_dd(self):
        val = self.textstack.pop()
        key = self.textstack.pop()
        if self.structs[-1] != self.xostack[-1]:
            val = self.structs.pop()
        self.xostack[-1][key]=val
    def handle_data(self, text):
        if len(self.stack) and containerTags.get(self.stack[-1],True): #skip text not within an element
            self.textstack[-1] += text
def toXOXO(struct,addHTMLWrapper=False,cssUrl=''):
    if type(struct) ==type((1,))or type(struct) ==type([1,]):
        inStruct = struct
    else:
        inStruct = [struct]
    if addHTMLWrapper:
        s= '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN
http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head profile=""><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'''
        if cssUrl:
            s+='<style type="text/css" >@import "%s";</style>' % cssUrl
        s+="</head><body>%s</body></html>" % makeXOXO(inStruct,'xoxo')
        return s.encode('utf-8')
    else:
        return makeXOXO(inStruct,'xoxo').encode('utf-8')
    
import sys

def fromXOXO(html):
    parser = xoxoParser()
    parser.feed(unicode(html,'utf-8'))
    #print >>sys.stderr, parser.structs
    structs=[struct for struct in parser.structs if struct]
    #print >>sys.stderr, structs
    while (len(structs) ==1 and type(structs)==type([1,])):
        structs=structs[0]
    return structs

# Allow direct invocation
# Read HTML from URL, parse into data structures, then re-output

if __name__ == "__main__":
  if len(sys.argv) < 2: raise SystemExit("Usage: "+sys.argv[0]+" url\n"+__doc__)
  url=sys.argv[1]
  file = urllib.urlopen(url)
  html=file.read(-1)
  file.close
  s=fromXOXO(html)
  p=toXOXO(s,True)
  print p
