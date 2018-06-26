# Write a Python program where a string will start with a specific number.
import re
string = input('Please enter a word: ')
pattern = r"\d+(\w)+"
match = re.search(pattern, string)
if match:
   print (match.group())
else:
    print ("No match")