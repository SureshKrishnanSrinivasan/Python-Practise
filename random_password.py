# random password genetrator
import random
passwordList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9']

user_input = int(input("Please enter passwordLength: "))
password=""
for i in range(user_input):
    char = random.randint(0, len(passwordList)-1)
    password+= passwordList[char]

print(password)

