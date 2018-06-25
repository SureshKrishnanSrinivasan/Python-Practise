# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'

import re
string = input('Please enter a word: ')
pattern = r"[a].*b$"

match = re.match(pattern, string)
if match:
   print ("Match")
else:
    print ("No match")