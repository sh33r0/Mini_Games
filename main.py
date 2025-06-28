from gtn import GTN
from rps import RPS
from tictactoe import TicTacToe
from pig import PlayerCount
from math_prob import play
while True:
    txt = """\nMini Games!!!
    - Guess The Number (1)
    - Rock, Paper, Scissors (2)
    - Tic Tac Toe (3)
    - Pig Game (4)
    - Math Problem Solver (5)
Select a game (press a number or 'q' to quit): """
    value = input(txt)
    if value == "1":
        GTN(50)
    elif value == "2":
        RPS()
    elif value == "3":
        game = TicTacToe()
        game.play()
    elif value == "4":
        PlayerCount()
    elif value == "5":
        play()
    else:
        break
