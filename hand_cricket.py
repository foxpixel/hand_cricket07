import random as random
score = []
overss = int(input("enter no. of overs"))
for i in range(overss*6):
    print("DElivery %d:", (i+1))
    player = int(input("enter score on the ball played"))
    comp = random.randrange(0, 6, 1)
    if player != comp:
        print("s:", player)
        score.append(player)
    else:
        break
print(score)
