import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
computer_score = 0
player_score = 0
final_score = 3

while True:
    final_score > player_score and final_score > computer_score
    player = input("Rock, Paper or  Scissors?").capitalize()


    if player == computer:
        print(0)
    elif player == "Rock":
        if computer == "Paper":
            print(-1, computer, "covers", player)
            computer_score +=1
        else:
            print( 1 , player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print(-1 , computer, "cut", player)
            computer_score += 1
        else:
            print( 1 , player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print(-1 , computer, "smashes", player)
            computer_score += 1
        else:
            print(1 , player, "cut", computer)
            player_score += 1
    elif player == 'End':
        print("Final Scores:")
        print(f"CPU:{computer_score}")
        print(f"Player:{player_score}")

        if player_score > computer_score:
            print("CONGRATS, YOU WON!")
        elif player_score == computer_score:
            print("IT'S A TIE")
        else:
            print("OH NO :( THE COMPUTER WON...")
        break

