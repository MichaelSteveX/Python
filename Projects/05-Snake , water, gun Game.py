#**************************** SNACK , WATER , GUN , GAME ********************************
import random
"""
1 for snake 
-1 for water 
0 for gun 
"""
computer = random.choice([-1,0,1])
youstr = input("ENter Your Choice: ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
you = youDict[youstr]

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")


if (computer == you):
    print("itS a draw")

else:

    if (computer ==-1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("YOU Lose!")

    elif(computer == 1 and you == -1):
        print("YOU Lose !")

    elif(computer == 1 and you == 0):
        print("YOU win !")

    elif(computer == 0 and you == -1):
        print("YOU win !")

    elif(computer == 0 and you == 1):
        print("YOU lose!")

    else:
     print("somethig Went WronG")




     # Here the over all code done   