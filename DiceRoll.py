#DiceRoll.py
#Name:Nola Nelson
#Date:10/05/25
#Assignment:Lab6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  number_rolls = 10000
  #Create two dice values ranging from 1 - 6 each
  for r in range(number_rolls):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    rolls[total - 2] = rolls[total - 2] + 1
  
  #print statictics for dice rolls
  for i in range(11):
    total = i + 2
    count = rolls[i]
    percent = (count / number_rolls) * 100
    print(total, ":", count, ":", round(percent,2), "%")



if __name__ == '__main__':
  main()

