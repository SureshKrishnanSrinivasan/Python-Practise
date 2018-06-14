# 1
# 1 2
# 3 4 5 
# 6 7 8 9

num = 1 
count = 1

user_input = int(input("Please enter a number"))
# print(num)
while user_input !=0:
    for i in range(count):
        print(num)
        num+=1
        if count==1:
            num=1
        
    count+=1
    user_input-=1