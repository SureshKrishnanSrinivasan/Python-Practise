#Write a Python program that matches a word containing 'z' 

import re
string = input('Please enter a word: ')
pattern = r"\w*[zZ].\w*"

match = re.search(pattern, string)
if match:
   print (match.group())
else:
    print ("No match")