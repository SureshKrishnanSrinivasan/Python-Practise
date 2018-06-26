# Matches a word containing 'z', not start or end of the word

import re
string = input('Please enter a word: ')
pattern = r"\Bz\B"
match = re.search(pattern, string)
if match:
   print (match.group())
else:
    print ("No match")