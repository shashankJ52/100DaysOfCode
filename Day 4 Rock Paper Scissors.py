import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_input = int(input())

print(options[user_input])

computer = random.randint(0,2)

print("Computer choose: \n", options[computer])

flag  = False

if user_input == computer:
    print("It's a DRAW...")
    flag = True
else:
    if computer == 0 :
        if user_input  == 1:
            flag = True
            # print("You WON !!!")
    if computer == 1 :
        if user_input  == 2:
            flag = True
            # print("You WON !!!")
    
    if computer == 2 :
        if user_input  == 0:
            flag = True
            # print("You WON !!!")

if flag and user_input != computer:
    print("You've WON !!! ")
elif not flag and user_input != computer:
    print("You've LOST ....")

