def pick_string(option):
    if option == 0:
        return "rock"
    elif option == 1:
        return "paper"
    elif option == 2:
        return "scissors"
    else:
        exit(1)


while True:
    print("Select a number!")
    print("0 --> rock")
    print("1 --> paper")
    print("2 --> scissors")
    player_1 = int(input("Player 1 > "))
    player_1 = pick_string(player_1)
    player_2 = int(input("Player 2 > "))
    player_2 = pick_string(player_2)
    if player_1 == player_2:
        print("Draw")
    elif player_1 == "rock":
        if player_2 == "paper":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    elif player_1 == "scissors":
        if player_2 == "rock":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    else:
        if player_2 == "scissors":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    option = str(input("Do you wanna play again!Type yes or no > "))
    if "n" in option:
        break
