from getpass import getpass as input

# Welcome to the ultimate Rock, Paper, Scissors showdown!

# Players, choose your destiny!
player_1 = input("Player 1, make your move! (R/P/S): ").upper()
player_2 = input("Player 2, show your strength! (R/P/S): ").upper()

# Check the outcome of the battle
if player_1 == player_2:
    print("It's a tie! 🤝 The battlefield remains unchanged.")

elif player_1 == 'R':
    if player_2 == 'P':
        print("Player 2 claims victory! 🎉 Paper wraps rock. Player 1, your rock crumbles.")
    elif player_2 == 'S':
        print("Player 1 emerges triumphant! 💪 Rock smashes scissors. Player 2, shattered into pieces.")
    else:
        print("Invalid move by Player 2! Player 1 wins by default! 🎊")

elif player_1 == 'P':
    if player_2 == 'R':
        print("Player 1 claims victory! 🎉 Paper wraps rock. Player 2, your rock is powerless.")
    elif player_2 == 'S':
        print("Player 2 emerges triumphant! 💪 Scissors cut through paper. Player 1, torn to bits.")
    else:
        print("Invalid move by Player 2! Player 1 wins by default! 🎊")

elif player_1 == 'S':
    if player_2 == 'R':
        print("Player 2 claims victory! 🎉 Rock crushes scissors. Player 1, your scissors are defeated.")
    elif player_2 == 'P':
        print("Player 1 emerges triumphant! 💪 Scissors cut through paper. Player 2, torn to bits.")
    else:
        print("Invalid move by Player 2! Player 1 wins by default! 🎊")

else:
    print("Invalid move by Player 1! The battle is a chaotic mess. No winner! 😵")

# The battle has concluded. Thanks for playing!
