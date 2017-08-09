"""
    Bowling Score
    -------------
    C is the varible that detemines the if the previus frame is a strike or
    spare
    c = 0 -> default
    c = 1 -> strike
    c = 2 -> spare
"""

score = 0
c = 0 

def print_score(frame,score):
    print("\n Score after {0} frame is {1}".format(frame+1,score))

for frame in range(10):
    roll_1 = int(input('\n Pin dropped in first roll: '))
    if roll_1 == 10:
        score += 10
        print_score(frame,score)
        if c == 1 or c == 2:
            score += 10
        c = 1
    else:
        roll_2 = int(input('\n Pin dropped in second roll: '))
        if c == 1:
            score += roll_1 + roll_2
        if c == 2:
            score += roll_1
        if (roll_1 + roll_2) == 10 :
            score += 10
            c = 2
            print_score(frame,score)
        else:
            score += roll_1 + roll_2
            c = 0
            print_score(frame,score)
        if frame == 10:
            if c == 1:
                r1 = int(input('\n Pin dropped in bonus first roll: '))
                if r1 == 10:
                    score += 10
                    print("Total score {}".format(score))
                else:
                    r2 = int(input('\nPin dropped in bonus second roll: '))
                    score += r1 + r2 
                    print("Total score {}".format(score))
