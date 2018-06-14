a =["First",10,15,20,"last"]
new_list = list()
def firstLast(lst):
    new_list= [lst[0], lst[len(lst)-1]]
    print(new_list)

firstLast(a)