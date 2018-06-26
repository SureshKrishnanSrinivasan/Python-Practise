#  Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re
string = input('Please enter a word: ')
pattern = r"[a-zA-Z_]+"
match = re.search(pattern, string)
if match:
   print (match.group())
else:
    print ("No match")