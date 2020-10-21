print("Welcome to a board game! \nWIP\n")
#other files
import Useful as U
#packages and that
import random
import sys

I=U.InputMenu("""
/t\\
|b|
\\b/
Text Based Bois
Indepentant member project
""","[N]ew game\n[I]mport\n\n")

if I == "N":
    U.NewSave()
#else I == "I":
    #U.InputMenu("","Insert code in here.")