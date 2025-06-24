import random
def RPS():
    print("Let's play Rock Paper Scissors")

    r = "rock"
    p = "paper"
    s = "scissors"
    ch = [r,p,s]

    u = input("Enter a choice (rock, paper, scissors): ")

    if u not in ch:
        print("Invalid choice")
        return
    c = random.choice(ch)

    print("\nUser chose ",u, "\ncomputer chose ",c)

    # r>s, p>r, s>p

    if u == c:
        print("Tie")
    elif (u == r and c == s) or (u == p and c == r) or (u == s and c == p):
        print("You won!")
    else:
        print("You lost")

