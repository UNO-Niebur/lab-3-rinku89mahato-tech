#RPS.py
#Name:Rinku Mahato
#Date:02/06/2026
#Assignment: Play Rock, Paper, Scissor game as long as the user wants to play.
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  #Create a loop that continues as long as the user wants to play.
  playAgain = "Y"
  while playAgain == "Y":
  
  #User can play as many games as they wish.
  #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice( ["R",  "P",  "S"] )
    player = input("Pick your weapon (R, P, S): ")
  
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
    if computer == "R":
      print ("Computer Chose Rock")
    elif computer == "P":
      print ("computer choose Paper")
    else:
      print ("computer choose Scissors") 

    if player == "R" :
      print ("Player choose Rock")
    elif player == "P" :
      print ("Player choose Paper")
    else:
      print ("Player choose Scissors")

    if player == "R" and computer == "R":
      print ("Tie")
      ties = ties + 1
    if player == "R" and computer == "P":
      print("Computer Wins.")
      losses = losses +1
    if player == "R" and computer == "S":
      print("You Win!")
      wins = wins + 1

    if player == "P" and computer == "P":
      print ("Tie")
      ties = ties + 1
    if player == "P" and computer == "S":
      print("Computer Wins.")
      losses = losses +1
    if player == "P" and computer == "R":
      print("You Win!")
      wins = wins + 1

    if player == "S" and computer == "S":
      print ("Tie")
      ties = ties + 1
    if player == "S" and computer == "R":
      print("Computer Wins.")
      losses = losses +1
    if player == "S" and computer == "P":
      print("You Win!")
      wins = wins + 1
    
  #Ask the user if they would like to play again.
    playAgain = input("Play again? (Y/N): ")
  #play_again =input("would you like to play again" : {yes/No})

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
