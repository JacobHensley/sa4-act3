number = 10
print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? (type q to exit) ")
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    elif int(guess) > number:
        print("Lower, try again!")
    elif int(guess) < number:
        print("Higher, try again!")