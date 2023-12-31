# -*- coding: utf-8 -*-
"""Project-1 (GTN)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wZ-ALTIgcGAlSzNXNzhTi_3sy3GWaJzj

# **Guess The Number**
*a python project by Keerthi Potluri*
"""

import random
import math

#step-1 Introduction and Instructions
print('\033[1m' + "Welcome to the game GUESS THE NUMBER")
print('\033[1m' +"\nBefore we dive into the game, get acquainted with the rules and regulations!!!\n")
print("When a player starts the game he/she will be awarded with intial pointa based on the choosen level. \nEach level is differentiated by the range of the highest number.\n")
print("Available levels:\n LEVEL 1:-\t Range: 1-50 \t Score:500 \n LEVEL 2:-\t Range: 1-100 \t Score:700 \n LEVEL 3:-\t Range: 1-200 \t Score:1000 \n LEVEL 4:-\t Range: 1-500 \t Score:1500 ")

#step-2 Choosing level and input low and high values
lev= int(input("\nChoose the level you wish to play from the above options: "))

if lev==1:
  print("\nBasic and Safe :)")
  print("LEVEL-1")
  print("SCORE-500")
  in_sc=500
  low_num=0
  high_num=50
elif lev==2:
  print("\nAdventure and  safe :)")
  print("LEVEL-2")
  print("SCORE-700")
  in_sc=700
  low_num=0
  high_num=100
elif lev==3:
  print("\nRisk and fun ;)")
  print("LEVEL-3")
  print("SCORE-1000")
  in_sc=1000
  low_num=0
  high_num=200
else:
  print("\nRisk is fun ;)")
  print("LEVEL-4")
  print("SCORE-1500")
  in_sc=1500
  low_num=0
  high_num=500

#generate random number
x= random.randint(low_num, high_num)
print("\nYou have only 5 chances to win the game !!\nALL THE BEST")
print("SCORE",in_sc)
ges_no=0

while ges_no<5:
  ges_no += 1
  ges= int(input("Guess the number:-"))
  print("\nChances left for you to guess the number is:",5-ges_no)

  if x==ges:
    print("congo u did it in",
          ges_no,"try")
    break

  else:
    print("OOPS!! Wrong Answer :(\n")
    print("\nYou can choose\n1.Next attempt\n2.HINT\nin your next step")
    k=int(input("\nchoose your next step\t"))
    if k==1:
      ges_no += 1
      ges= int(input("Guess the number:-"))
      print("\nChances left for you to guess the number is:",5-ges_no)
    else:
      print("choose the hint you wanna use.\n 1.Low/High\n 2.Prime number\n 3.Even/odd\n")
      y=int(input("Choose the hint type"))
      if y==1:
        if x>ges:
          print("you guessed too small")
          in_sc -= 100
          print("SCORE",in_sc)

        else:
          print("you guessed too high!!")
          in_sc -= 100
          print("SCORE",in_sc)
      if y==2:
        def is_prime(x):
          if x <= 1:
            return False
          elif x == 2:
            return True
          for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
              return False
          return True
        if __name__ == "__main__":
          try:
            if is_prime(x):
              print("it is a prime number.")
            else:
              print("it is not a prime number.")
          except ValueError:
            print("Invalid input. Please enter a valid integer.")
      if y==3:
        if x%2==0:
          print("it is an even number")
        else:
          print("it is an odd number")



if ges_no>=5:
  print("\nOOPS! YOUR CHANCES ARE OVER :(")
  print("\nTHE NUMBER IS ",x)
  print("\nBETTER LUCK NEXT TIME4")

