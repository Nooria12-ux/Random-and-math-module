import random

options = ["Rock", "Paper", "Scissors"]
playing = True
score = 0

while playing : 
    comp_choice = random.choice(options)
    
    user_choice = input("Please choose Rock, Paper or Scissors (Ensure the spelling is correct): ")
    
    print("You chose:", user_choice)
    print("Computer chose:", comp_choice)
    
    if score < 6:
        if user_choice == comp_choice:
            print("It is a tie!")
            print("Score: ", score)
            
        elif user_choice == "Rock" and comp_choice == "Scissors":
            print("Rock smashes scissors. You win!")
            score = score + 1
            print("Score:",score)
            
        elif user_choice == "Paper" and comp_choice == "Rock":
            print("Paper covers Rock. You win!")
            score = score + 1
            print("Score:",score)
            
        elif user_choice == "Scissors" and comp_choice == "Paper":
            print("Scissors cuts paper. You win!")
            scpre = score + 1
            print("Score: ", score)
            
        else:
            print("You lose")
            print("Score: ", score)
            
    else:
        print("player wins! Score: ",score)
        break