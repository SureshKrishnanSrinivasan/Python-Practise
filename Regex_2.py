# match a string with an 'a' followed by zero or more 'b's
import re
string = input("Please enter a testing string: ")
pattern = r"^a(b)*$"
if re.match(pattern,string):
    print("Valid!")
else:
    print("Invalid!")