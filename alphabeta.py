from mancala import Mancala
from game_tree import *


def alphabeta(mancala, depth, player):
    past_moves = mancala.moves
    this_game_tree = game_tree(past_moves, int(mancala.get_pits_per_player()), int(mancala.get_stones_per_pit()), depth)

    alpha = float('-inf')
    beta = float('inf')

    maxval = float('-inf')
    bestmove = None

    for child in this_game_tree.children:
        childval = minvalue(child, player, alpha, beta)
        if childval > maxval:
            maxval = childval
            bestmove = child.past_moves[-1]


    return bestmove[1]
    

def minvalue(node, player, alpha, beta):
    if len(node.children) == 0:
        if player == 1:
            return int(node.p1mancala - node.p2mancala)
        else:
            return int(node.p2mancala - node.p1mancala)
    
    val = float('inf')

    for child in node.children:
        childval = maxvalue(child, player, alpha, beta)
        if childval < val:
            val = childval
        
        if val <= alpha:
            return val
        
        beta = min(val, beta)

    return val


def maxvalue(node, player, alpha, beta):
    if len(node.children) == 0:
        if player == 1:
            return int(node.p1mancala - node.p2mancala)
        else:
            return int(node.p2mancala - node.p1mancala)
    

    val = float('-inf')


    for child in node.children:
        childval = minvalue(child, player, alpha, beta)
        if childval > val:
            val = childval
        
        if val >= beta:
            return val
        
        alpha = max(val, alpha)

    return val