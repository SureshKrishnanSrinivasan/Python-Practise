# match a string with an 'a' followed by three 'b'

import re
string = input('Please enter a number: ')
pattern = r"^a(b){3,3}$"

match = re.match(pattern, string)
if match:
   print ("Match")
else:
    print ("No match")