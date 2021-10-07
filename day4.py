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
winner = "você ganhou!"
loser = "você perdeu ):"

#i was supposed to use lists but i felt like using a list was more complicated than string concat

person = input("Rock, Paper, Scissors! Choose your fighter!\n 0 for Rock, \n 1 for Paper \n 2 for Scissors \n")

print("Você escolheu... \n")
if person == "0":
    print(rock)
elif person =="1":
    print(paper)
else:
    print(scissors)

computer = str(random.randint(0,2))
print("o computador escolheu... \n")
if computer == "0":
    print(rock)
elif computer =="1":
    print(paper)
else:
    print(scissors)

match = person+computer

if person == computer:
    print("empate!")
elif match == "10" or match == "21" or match == "10":
    print(winner)
else:
    print(loser)
