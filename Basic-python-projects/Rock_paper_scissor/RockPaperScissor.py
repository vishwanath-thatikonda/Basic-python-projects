import random




def play_game():
    game_lst = ['R','P','S']
    com_choice = random.choice(game_lst)
   
    while True:
        
        user_choice = input("To play 'Rock' enter - R, To play 'Paper' enter - P, To play 'Scissor' enter - S:  ").upper()

        if user_choice not in game_lst:
            print("Enter a valid Input to play!")
            continue

        if user_choice == com_choice:
            print(f"GAME TIED!, you both have choosed: {user_choice}")
        elif ((user_choice == 'S' and com_choice == 'P') or (user_choice =='R' and com_choice == 'S') or (user_choice =='P' and com_choice == 'R')):
            print(f"You Won the Game, The computer choice is: {com_choice}")
         

        else:
            print(f"You Lost the game and the computer choice is: {com_choice}")

        break   

for i in range(5):
    play_game()



