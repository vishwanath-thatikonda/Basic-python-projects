import random
number = random.randint(1,100)

def guess_number():
    count = 0
    while True:
        try:
            guess_number = int(input("Guess a number between 1 and 100: "))
            if not (0<=int(guess_number)<=100):
                print("Please guess a valid number between 1 and 100")
                continue

            count += 1
            if count > 1:
                suffix = "'s"


            if guess_number == number:
                print(f"You guessed the number {number} in {count} attempt{suffix}!")
                break
            elif guess_number < number:
                print("Your guss is lower than the computer guess!")
            else:
                print("Your guess is higher than the computer guess!")
        except ValueError:
            print("Enter a valid number not a string!")
guess_number()






    






