# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 18:25:54 2019

@author: MY PC
"""

import random
comp_score=0
player_score=0
def name_to_num(name):  #function to assign a no. againt name
    if name == "rock":
        res = 0
    elif name == "Spock":
        res = 1
    elif name == "paper":
        res = 2
    elif name == "lizard":
        res = 3
    else:
        res = 4
    return res
def num_to_name(num): #function convert num into name
    if num == 0:
        res = "rock"
    elif num == 1:
        res = "Spock"
    elif num == 2:
        res = "paper"
    elif num == 3:
        res = "lizard"
    else:
        res = "scissors"
    return res 
def game(): #main game
    global player_score #declare global variable
    global comp_score
    name=input("Enter your choice :") #ask choice
    player = name_to_num(name) #player given name converted to num
    comp= random.randrange(0, 5) #selection of  comp
    print ("Player chooses", name) #print player choice
    print ("Computer chooses", num_to_name(comp)) #comp selected in num so convertion to name and printing
    #mathematical calculation to make conclusion
    if (comp + 1) % 5 == player: #eg player selct paper(2) and comp spock(1) then 1+1 % 5= 2
        print ("you won!")
        player_score=player_score+1
    elif (comp + 2) % 5 == player:  #eg player selct paper(2) and comp rock(0) then 0+2 % 5= 2,for spock and lizard
        print ("you won!")
        player_score=player_score+1
    elif comp == player: #condition for tie no score to assign
        print ("its a tie!")
    else:
        print ("you lose!") #all other cases
        comp_score +=1
    
print("Welcome to game!!! ")
a="y"
while a=="yes" or a=="y":
    game()
    a=input("do you want to play more? if yes Press yes or y")
print("you score is %d and computr score is %d"%(player_score,comp_score))
print("thank u for playing")
    
    