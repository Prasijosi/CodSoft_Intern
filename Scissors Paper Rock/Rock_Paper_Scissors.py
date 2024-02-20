# TASK 4
# ROCK PAPER SCISSORS GAME

def hand_game(player1, player2):
    """
    Given Function prompts the user to input three choices of indoor
    and quick game of rock,papers and scissors.For draw between two
    players when they enter same choicess it shows /It's a tie!/ and
    for other cases it shows the clear winner.
    """
    
    if player1 == player2:
        return "It's a tie!"

    elif (player1 == "Rock" and player2 == "Scissors") or \
         (player1 == "Paper" and player2 == "Rock") or \
         (player1 == "Scissors" and player2 == "Paper"):
        return "Player 1 wins!"
    
    else:
        return "Player 2 wins!"
    
while True:
    try:
        player1 = input("Enter your choice Rock,Paper or Scissors :  ").lower()
        
        if player1 in ("rock","paper","scissors"):
         break
     
        else:
            print("Choose Rock, Paper or Scissors.\n")
            
    except ValueError:
     print("Invalid Input.")
     
        
while True:
    try:
        player2 = input("Enter your choice Rock,Paper or Scissors :  ").lower()
        
        if player2 in ("rock","paper","scissors"):
            break
    
        else:
            print("Choose Rock, Paper or Scissors.\n")
        
    except ValueError:
     print("Invalid Input.")
        
winner = hand_game(player1,player2)
print(winner)


