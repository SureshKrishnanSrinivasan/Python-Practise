import random # Import random module 
while True:
    user_input = input("Please enter a number between 0 and 9: ")
    if user_input == "exit":
        break
    comp_guess = random.randint(0,9)

    guess = {'1':"Too close!","2":"Two steps more!", "3":"Drink some three roses tea!", "4":"Quater mile away!" ,"5":"You have cut me into half!" ,"6":"The ultimate sense of humans", "7":"You must go visit the seven wonders of the world, before you canm see me!" , "8":"People are out on the street!" ,"9":"Every one is working" }
    
    if int(user_input) == comp_guess:
        print("you guessed it right!Bingo")
    else:
        print(guess[str(abs(int(user_input)-comp_guess))])