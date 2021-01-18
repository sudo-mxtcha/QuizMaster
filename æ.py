import time
import random
def progINIT():
  greetlst=["Hey there","Hiya","Hey","Hello","Salutations"]
  greet=random.choice(greetlst)
  name=str(input(greet+"! What is your name? "))
  greet=random.choice(greetlst)
  time.sleep(0.5)
  print(greet+", "+name+"! Welcome to the Quiz!")

