# Copyright 2013 Javier Benito Garcia-Mochales
######################## BEGIN LICENSE BLOCK ########################
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with MoodPyth.  If not, see <http://www.gnu.org/licenses/>.
######################### END LICENSE BLOCK #########################
'''
Auxiliar external functions
'''
def _tabulate(tab):
    ''' Returns the number of tabulations indicated in a string '''
    buf = ''
    for tab in range(tab):
        buf += "\t"
    return buf

def _showt(data, tab):
    ''' Recursive function that returns printable JSON converted to python string '''
    buf = ''
    if (type(data)==type({})):
        buf += _tabulate(tab)
        buf += "{" + "\n"
        for a in data.keys():
            buf += _tabulate(tab)
            buf += str(a) + ": " + _showt(data[a], tab+1)
        buf += _tabulate(tab)
        buf += "}" + "\n"
    elif (type(data)==type([])):
        buf += "[\n"
        for a in data:
            buf += _showt(a, tab)
        buf += _tabulate(tab)
        buf += "]" + "\n"
    else:
        buf += str(data) + "\n"
    return buf

def show(data):
    ''' Prints JSON converted to tabulated python data '''
    print _showt(data,0)
