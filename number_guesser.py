#import random module
import random

top_of_range = input("Set the top of the range: ")

#isdigit returns true if top_of_range is a number
if top_of_range.isdigit():
    #if it is a digit, parse as an int
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.") 
    quit()



random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
        
    if user_guess.isdigit():
        
        user_guess = int(user_guess)

    else:
        print("Please type a number.") 
        #continue brings up back to the top of the loop
        continue

    if user_guess == random_number:
        print("Good job! You guessed correctly!")
        break
    else:
        print("You got it wrong! Try again.")

        if user_guess < random_number:
            print("Guess a higher number")
        else:
            print("Guess a lower number")

print(f"You got it in {guesses}, guesses.")