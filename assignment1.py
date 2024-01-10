# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:54:09 2022

@author: Najmun Nahar
"""

#imports and variables
from random import randint
President = 'Craig Stephenson '
Chair = 'Predrag Pesikan'
Coordinator   = 'Ilia nika'
Motto = "Transforming lives and communities through learning"
numbers = [randint(5, 10) for _ in range(20)]

#-------------------Question1----------------------#

#a)create a set from the variable 'President' and print it
presidentSet = set(President)
print("President Set: ",presidentSet)

#b)	use the add() method to add  a character to the set and print it
presidentSet.add('B')
print("After adding element B the new Set is ",presidentSet)

#c)	use the remove() method to take '  '  from the set and print it
presidentSet.remove(' ')
print("After removing ' ' the new Set is ",presidentSet)

#d)	use the update() function to add 'x', 'y' and 'z' to the set  and print the result
presidentSet.update(['x','y','z'])
print("After inserting x.y and z the set",presidentSet)

#e)	use the len() function to get the number of elements in the set and print the result
length=len(presidentSet)
print("Length of the set is: ",length)

#------------------Question2--------------------------#
#a)	Create a tuple from the variable “chair” and print it
chairTuple=tuple(Chair)
print("Tuple created from Chair: ",chairTuple)

#b)	Show the output of using the following methods: count () , index(), max(), min(), len() 
#count()
aCount=chairTuple.count('a')
print("There are ",aCount," 'a' in the tuple")

#index()
gIndex=chairTuple.index('g')
print("'g' is found at index ",gIndex," of the tuple")

#max()
print("Max value element ",max(chairTuple))

#min
print("Minimun value element ",min(chairTuple))

#len()
chairTupleLength=len(chairTuple)
print("There are ",chairTupleLength," elements in the tuple")

#c)	 Use array-like indexing to print the third and fifth element of your tuple.
third=chairTuple[2]
fifth=chairTuple[4]
print("Third element is",third," and fifth element is ",fifth)

#-------------------------------Question 3------------------------------------#
#a)	create a list from the variable 'motto' using the split() method of the string class and print it 

mottoList = Motto.split()
print("Splitted List ", mottoList)

#b.1) use the append () method once to add 'Coordinator' to the end of the list

mottoList.append('Coordinator')

#b.2) use the insert () method to add your 'name and ID' at the start of the list

mottoList.insert(0, 'Najmun Nahar-301160081')

#b.3) use the remove () method to remove 'through' from the list
mottoList.remove('through')

#b.4) use the extend() method to add  “ Centennial” and “College” to the end of the list.  
mottoList.extend(['Centennial','College'])

#b.5) print the final list
print("Final List ",mottoList)

#c.1) Use the sort () method to order the list, and Print the list
mottoList.sort()
print("Sorted List",mottoList)

#c.2) Use the reverse () method to reverse the list, print the final list
mottoList.reverse()
print("Reversed List",mottoList)

#--------------------------------Question-4-------------------------------------#
#a)	Convert the below given lists into a dictionary in a way that item from list1 is the key and item from list2 is the value. Use the update () method and print the result.

keys = ['20', '22', '25','80','110','143','161']
Values = ['FTP', 'SSH', 'SMTP', 'HTTP', 'POP3', 'IMAP', 'SNMP']

dictionary=dict(zip(keys,Values))
print("Dictionary ",dictionary)

#b)	Check if the value SMTP exists in the dictionary, and print the result. 

value = 'SMTP'
if value in dictionary.values():
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exist in dictionary")
    
#c)	Use the get () method to retrieve the name of key 143, result to be shown.
print(dictionary.get('143'))

#d)	Delete the keys 80 and 143, print the dictionary to show the result. 

dictionary.pop('80')
dictionary.pop('143')
print("Dictionary after removing keys 80 and 143",dictionary)

#e)	Sort the dictionary by values in ascending order and display the result. 
import operator
sorted_d = sorted(dictionary.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)

#------------------------Question-5----------------------------------------------#
#a)	use the enumerate function to print the above collection: tuple, list and dict
print("Tuple: ", list(enumerate(chairTuple)))
print("List: ", list(enumerate(mottoList)))
print("Dictionary: ", list(enumerate(dictionary)))

#b)	 Use the items() method of the dict class to enumerate the above dictionary
print(dictionary.items())
