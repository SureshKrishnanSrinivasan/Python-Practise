# Write a Python program that matches a word at end of string, with optional punctuation. 

import re
string = input('Please enter a word: ')
pattern = r"\w+([.]|\w)$"

match = re.search(pattern, string)
if match:
   print (match.group())
else:
    print ("No match")