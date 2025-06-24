import random

def GTN(x):
    print("Let's play Guess The Number")

    r = random.randint(0, x)

    n = 0
    while True:
        g = int(input("Guess a number between 0 and 50: "))
        n += 1

        if g == r:
            print("Congrats, the number is ",r)
            break
        elif g < r:
            print("Too low!")
        else:
            print("Too high!")
