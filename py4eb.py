import random
user_score = 0
comp_score = 0
print("Game Rules are as follows:\n 1) Rock wins Scissor\n2) Scissor wins Paper\n 3) Paper wins Rock\n\n\n\n Choose: \n a) 1 - for Rock\n b) 2 - for Paper\n c) 3 - for Scissors\n d) quit - To get results")
while True:
  user_input = input("Enter input: ")
  if user_input == "quit":
    if user_score>comp_score:
      print("You scored",user_score)
      print("Computer scored",comp_score)
      print("You beat the computer by",user_score - comp_score,"points")
    elif user_score < comp_score:
      print("You scored",user_score)
      print("Computer scored",comp_score)
      print("Computer beat you by",comp_score - user_score,"points")
    else:
      print("You scored",user_score)
      print("Computer scored",comp_score)
      print("It was a draw")
    break
  values = ["rock","paper","scissor"]
  comp = values[random.randint(0,2)]
  user = values[int(user_input)-1]
  if user == "rock" and comp == "scissor" or user =="scissor" and comp =="paper" or user == "paper" and comp == "rock" :  
    user_score +=1
  if comp == "rock" and user == "scissor" or comp =="scissor" and user =="paper" or comp == "paper" and user == "rock" :  
    comp_score +=1
  


# rock scissor paper
# rock scissor,  scissor paper, rock paper, 
# rock rock, paper paper, scissor scissor   