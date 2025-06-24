def PlayerCount():
    totalPlayer=input("Enter no. of players who will play the game(2-4): ")
    if totalPlayer.isdigit():
        totalPlayer=int(totalPlayer)
        if 1<totalPlayer<5:
            Pig(totalPlayer)
        else:
            print('Enter a val between 2 and 4 next time!!')
    else:
        print('Enter a number next time!!')

def roll():
    import random
    return random.randint(1,6)
def Pig(players):
    winscore=50
    scores=[0 for _ in range(players)]

    while max(scores)<winscore :
        for player in range(players):
            print(f"\nPlayer no. {player + 1} turn has just started!")
            print("Your total score is:", scores[player], "\n")
            currScore = 0

            while True:
                wantRoll=input("Would you like to roll (y)? ")
                if wantRoll.lower() not in "yY":
                    break

                val = roll()
                print("You rolled a:", val)  
                
                if val == 1:
                    print(f"You rolled a 1! Turn over for Player {player+1}!")
                    currScore = 0
                    break
                else:
                    currScore += val

                print("Your turn score is:", currScore)
            
            scores[player] += currScore
            print("Your total score is now:", scores[player])
            if scores[player] >= winscore:
                break

        if max(scores) >= winscore:
            break
    max_score = max(scores)
    winners = [i+1 for i, s in enumerate(scores) if s == max_score]
    
    if len(winners) == 1:
        print(f"Player {winners[0]} wins with {max_score} points!")
    else:
        print(f"Players {', '.join(map(str, winners))} tie with {max_score} points!")
