# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 19:35:49 2022

@author: paulh
"""

lists = ['apple', 'banana', 'pear', 'pear']

#append to a list
lists.append('cherry')

#insert item into a specific position 
lists.insert(1, 'grape')

#remove items in a list
lists.remove('pear')

#remove the last item in a list
lists.pop()

#working with dictionaries

mydict = {
    'name' : 'Peedee',
    'location' : 'Sneedville',
    'favcolor' : 'alligator',
    'luckynumber' : 7
    }

#access other keys
color = mydict['favcolor']
print(color)

#to get a list of keys
mydict.keys()

#to get a list of values
mydict.values()

#to add a new key/variable
mydict['gender'] = 'female'
print(mydict)