import random

def computer_guess_game(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        lst = ['l','h','c']
        feedback = input(f"If {guess} is low(L), High(H) or correct(C)?? ").lower()
        if feedback not in lst:
            if feedback.isdigit():
                print(f"Invalid input! please conform the number{guess} is low(L), High(H) or correct(C)?? ")
                feedback = input(f"If {guess} is low(L), High(H) or correct(C)?? ").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
        
    print(f"Yayyyy I guessed it right")
#  need to be modified   
#another comment


computer_guess_game(100)
