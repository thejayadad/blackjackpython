

from my_games.blackjack import Blackjack


def game_menu():
    print("""
        Games Are Us

        1) Blackjack
        2) Number Guess
        3) Rock Paper Scissors
        4) Exit
    
    """)
    game_choice = int(input("Which game would you like to play? "))
    match game_choice:
        case 1:
            print("------------ Welcome to Blackjack ------------")
            balance = 0
            balance = int(input("How much do you want to deposit? "))
            wager = 0
            wager = int(input("How much do you want to wager? "))
            
            game = Blackjack()
            game.play_game()
        case 2:
            print("Guess the number")
        case 3:
            print("Rock paper scissors")
        case 4:
            print("exit")
            print("bye")
            



game_menu()
# game = Blackjack()
# game.play_game()
