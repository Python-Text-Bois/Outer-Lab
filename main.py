import os
os.system("clear")
print("Welcome to a board game! \nWIP\n")

import Script.Useful as U
import random

#main menu
I=U.InputMenu("""
/p\\
|t|
\\b/
Python Text Bois
""","[N]ew game\n[I]mport\n\n")

#Overwrites save with template
if I == "N":
    U.NewSave()
#overwrites save with input
elif I == "I":
    e=U.InputMenu("","Insert code in here. INSERTING SOMETHING ELSE WILL BREAK THE GAME.")
    l=open("save.txt","w")
    l.write(e)
    l.close()
    del e;del l
    
#Game loop
os.system("clear")
#to see what goes on after this visit the game.py file
import Script.game as g
g.game()