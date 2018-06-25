# match one upperCase letter followed by  lower-case letters 

import re
string = input('Please enter a word: ')
pattern = r"[a].+b$"

match = re.match(pattern, string)
if match:
   print ("Match")
else:
    print ("No match")