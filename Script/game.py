import Script.Useful as U
from os import system as S
def game():
    while True:
        U.InputMenu(U.Fetch("save.txt"),"")
        S("clear")
        