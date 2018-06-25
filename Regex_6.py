# match a lower case string joined using underscore 

import re
string = input('Please enter a number: ')
pattern = r"[a-z]+_[a-z]+$"

match = re.match(pattern, string)
if match:
   print ("Match")
else:
    print ("No match")