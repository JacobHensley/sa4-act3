number = 10
attempts_left = 5
print("I'm thinking of a number...")

while True:
    guess = input(f"What number am I thinking of? You have {attempts_left} attempts left.")
    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print("Try again! or type q to exit.")
        attempts_left -= 1
        if attempts_left <= 0:
            print("You have run out of attempts.")
            break