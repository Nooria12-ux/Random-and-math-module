import random
playing = True

number = random.randint(0,20)

print("I will guess a number from 0 to 20, you have to guess it one digit at a time")
print("The game ends when the is guess\n\n")

while playing:
    guess = int(input("Enter your guess: "))
    
    if guess < number :
        print("Your guess number is LESSER that the correct number")
        
    elif guess > number :
        print("Your guess number is HIGHER than the correct number")
        
    elif number == guess:
        print("Your guess is correct!")
        print(f"The number was {number}")
        break