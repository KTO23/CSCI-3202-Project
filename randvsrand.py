from mancala import Mancala
import time

starttime = time.perf_counter()

results = []
num_games = 100

for x in range(num_games):
    newgame = Mancala(pits_per_player = 6, stones_per_pit = 4)

    while(newgame.winning_eval() == False):
        move = newgame.random_move_generator()
        newgame.play(move)

    
    player1mancala = newgame.board[newgame.p1_mancala_index]
    player2mancala = newgame.board[newgame.p2_mancala_index]
    winner=""
    
    if(player1mancala > player2mancala):
        winner="player1"
    elif(player2mancala > player1mancala):
        winner="player2"
    else:
        winner="tie"
    
    num_moves = len(newgame.moves)
    
    results.append([winner, num_moves])
    
endtime = time.perf_counter()

player1wins = 0
player2wins = 0
tie = 0
totalmoves = 0
for x in results:
    if x[0] == "player1":
        player1wins = player1wins + 1
    elif x[0] == "player2":
        player2wins = player2wins + 1
    else:
        tie = tie + 1
    
    totalmoves = totalmoves + x[1]

totaltime = endtime - starttime
averagemoves = totalmoves/num_games
print(f"Player 1 wins: {player1wins}")
print(f"Player 2 wins: {player2wins}")
print(f"Ties: {tie}")
print(f"Average Moves: {averagemoves}")
print()
print(f"Player 1 win %: {player1wins*100/num_games}")
print(f"Player 2 win %: {player2wins*100/num_games}")
print(f"Tie %: {tie*100/num_games}")
print(f"Time taken: {totaltime}")

