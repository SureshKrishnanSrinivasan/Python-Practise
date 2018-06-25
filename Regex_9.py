# Write a Python program that matches a word at the beginning of a string

import re
string = input('Please enter a word: ')
pattern = r"^\w+"

match = re.search(pattern, string)
if match:
   print (match.group())
else:
    print ("No match")