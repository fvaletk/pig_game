import random

players = 0
max_score = 20
scores = {}
keep_playing = True
quit_game = False
cancel_game_requests = 0

while(True):
  number_of_players = input('How many players are going to participate? (2 - 4): ')

  if number_of_players.isdigit():
    players = int(number_of_players) 
    if players >= 2 and players <= 4:
      print("Let's start!")
      scores = { i: 0 for i in range(players) }
      break
    else:
      print("The number of players must be between 2 and 4 players. Please try again\n")
  else:
    print("The number of players must be a digit. Please try again\n")

while (keep_playing):
  for i in range(players):
    if quit_game:
      keep_playing = False
      break

    print(f"\nPlayer number {i+1} you are up next!")
    print(f"Your score is {scores[i]}")
    current_score = scores[i]

    while current_score < max_score:
      keep_rolling = input(f"Do you want to roll? (For quitting type 'q'): ")
      if keep_rolling.lower() != 'y':
        if keep_rolling.lower() == 'q':
          quit_game = True
        break
      result = random.randint(1, 6)
      if result == 1:
        print(f"\nGot 1. Your score is now 0\n")
        current_score = 0
        break
      else:
        current_score += result
        print(f"\nGot {result}. Your current score is: {current_score}")
    
    scores[i] += current_score
    if scores[i] >= max_score:
      print(f"Congratulations Player {i+1} you are the winner!")
      print(f"Your score: {scores[i]}")
      print(f"Winning score: {max_score}")
      quit_game = True
    
print("\nThanks for playing!")