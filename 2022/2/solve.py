#!/usr/bin/env python

with open("2\\input.txt") as f:
    strat_guide = f.read().splitlines()

score_you=0
outcome=0

for round in strat_guide:
        opp, outcome = round.split(' ')
       
        #Evaluating Round
        if outcome == "Y": #Draw
            score_you += 3
            you = opp
            #print('Draw')
        elif outcome == "X":
            if opp == "A": you = "C"
            elif opp == "B": you = "A"
            elif opp == "C": you = "B"
            #print("Loss")
        elif outcome == "Z":
            score_you += 6
            if opp == "A": you = "B"
            elif opp == "B": you = "C"
            elif opp == "C": you = "A"
            #print("Win!")

        #Assigning opp choice & score:
        if you == "A": score_you += 1 #Rock
        elif you == "B": score_you += 2 #Paper
        elif you == "C": score_you += 3 #Scissors

""" #Previous code for part 1 of day
for round in strat_guide:
        opp, you = round.split(' ')
        # Assigning your choice & score
        if you == "X": #Rock
            you = "A"
            score_you += 1
        elif you == "Y": #Paper
            you = "B"
            score_you += 2
        elif you == "Z": #Scissors
            you = "C"
            score_you += 3
        
        #Assigning opp choice & score:
        if opp == "A": score_opp += 1 #Rock
        elif opp == "B": score_opp += 2 #Paper
        elif opp == "C": score_opp += 3 #Scissors
        
        #Evaluating Round
        if opp == you: #Draw
            score_you += 3
            score_opp += 3
            #print('Draw')
        elif (opp == "A" and you == "C") or (opp == "B" and you == "A") or (opp == "C" and you == "B"):
            score_opp += 6
            #print("Loss")
        else: #Assuming Win
            score_you += 6
            #print("Win!")
"""

print(score_you)