from mancala import Mancala
from minimax import *
from random import randint
import time

starttime = time.perf_counter()

results = []
num_games = 100
depth=5

for x in range(num_games):
    game = Mancala(pits_per_player = 6, stones_per_pit = 4)

    randnum = randint(0, 1)

    if randnum == 0:
        turn = 0
        while(game.winning_eval() == False):
            if turn == 0:
                move = game.random_move_generator()
                game.play(move)
                turn+=1
            else:
                move = int(minimax(game, depth, player=2))
                game.play(move)
                turn=0

    else:
        turn = 0
        while(game.winning_eval() == False):
            if turn == 0:
                move = int(minimax(game, depth, player=1))
                game.play(move)
                turn+=1
            else:
                move = game.random_move_generator()
                game.play(move)
                turn=0
    

    if(randnum == 0):
        randommancala = game.board[game.p1_mancala_index]
        minimaxmancala = game.board[game.p2_mancala_index]
        winner=""
        
        if(randommancala > minimaxmancala):
            winner="random"
        elif(minimaxmancala > randommancala):
            winner="minimax"
        else:
            winner="tie"
        
        num_moves = len(game.moves)
        results.append([winner, num_moves])
    
    else:
        randommancala = game.board[game.p2_mancala_index]
        minimaxmancala = game.board[game.p1_mancala_index]
        winner=""
        
        if(randommancala > minimaxmancala):
            winner="random"
        elif(minimaxmancala > randommancala):
            winner="minimax"
        else:
            winner="tie"
        
        num_moves = len(game.moves)
        results.append([winner, num_moves])

    print(f"game {x+1} completed")

endtime = time.perf_counter()

randomwins = 0
minimaxwins = 0
tie = 0
totalmoves = 0
for x in results:
    if x[0] == "random":
        randomwins += 1
    elif x[0] == "minimax":
        minimaxwins += 1
    else:
        tie += 1

    totalmoves = totalmoves + x[1]

totaltime = endtime - starttime
averagemoves = totalmoves/num_games
print(f"Random Player Wins: {randomwins}")
print(f"Minimax wins: {minimaxwins}")
print(f"Ties: {tie}")
print(f"Average Moves: {averagemoves}")
print()
print(f"Random Player win %: {randomwins*100/num_games}")
print(f"Minimax win %: {minimaxwins*100/num_games}")
print(f"Tie %: {tie*100/num_games}")
print(f"Time taken: {totaltime}")