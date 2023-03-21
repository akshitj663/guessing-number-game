from random import randint
Easy_Level_Turns = 10
Hard_Level_Turns = 5
global turns
def checker(guess, answer,turns):
  if guess>answer:
    print("Too High")
    return turns - 1
  elif guess<answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You Got it!. The answer is {answer}")

def difficulty_set():
  user_level = input("Choose a Difficulty. Type 'easy' or 'hard': ")
  if user_level=="easy":
    return Easy_Level_Turns
  else:
    return Hard_Level_Turns
    
# """choosing a random no. for computer"""
def game():
  print("Welcome to the Number guessing game")
  print("I'm Thinking the number b/w 1 and 100.")
  answer = randint(1,100)
  turns = difficulty_set()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the no.")
    guess = int(input("Make a guess"))
    turns = checker(guess,answer,turns)
    if turns == 0:
      print("You Lose!")
      return 
      
game()