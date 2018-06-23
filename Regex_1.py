import re
string = input("Please enter a testing string: ")
pattern = r"([a-zA-Z0-9]+$)"
if re.match(pattern,string):
    print("You have entered a valid string!")
else:
    print("You have entered an invalid string!")