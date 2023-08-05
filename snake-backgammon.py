import random
p= [0,0] # Players are in 2 teams. p[0] means the score of team a, and p[1] means the score of team b.
while True:
    for r in [0,1]: # A for statement for team a and team b to play once in every round (r).
        k=random.choice('123456') # Randomly extract numbers between 1 and 6 by rolling dice.
        i=p[r] # Put the score of the previous round into i.
        i+=int(k) # Add the dice numbers.
        #Below is a change in position due to the rules of the Snakes and Backgammon board.
        if i==4:
            i=16
        elif i==8:
            i=12
        elif i==18:
            i=38
        elif i==20:
            i=74
        elif i==22:
            i=2
        elif i==24:
            i=36
        elif i==28:
            i=6
        elif i==30:
            i=1
        elif i==32:
            i=56
        elif i==34:
            i=46
        elif i==40:
            i=60
        elif i==44:
            i=26
        elif i==48:
            i=54
        elif i==58:
            i=42
        elif i==66:
            i=14
        elif i==68:
            i=52
        elif i==70:
            i=88
        elif i==72:
            i=50
        elif i==76:
            i=86
        elif i==80:
            i=100
        elif i==84:
            i=62
        elif i==90:
            i=82
        elif i==94:
            i=64
        elif i==96:
            i=82
        elif i==98:
            i=78
        p[r]=i # Add the final score for this edition.
    print(str(p[0])+" "+str(p[1])) # Score at the end of a round
    if p[0]>=100 or p[1]>=100: # If either team wins, the game is over.
        break
# print final result
if p[0]>p[1]:
    print("a가 이겼습니다.")
elif p[0]>=100 and p[1]>=100:
    print("다시 하세요")
else:
    print("b가 이겼습니다.")