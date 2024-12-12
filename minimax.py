from mancala import Mancala
from game_tree import *


def minimax(mancala, depth, player):
    past_moves = mancala.moves
    this_game_tree = game_tree(past_moves, int(mancala.get_pits_per_player()), int(mancala.get_stones_per_pit()), depth)

    maxval = float('-inf')
    bestmove = None

    for child in this_game_tree.children:
        childval = minvalue(child, player)
        if childval > maxval:
            maxval = childval
            bestmove = child.past_moves[-1]

    return int(bestmove[1])
    

def minvalue(node, player):
    if len(node.children) == 0:
        if player == 1:
            return int(node.p1mancala - node.p2mancala)
        else:
            return int(node.p2mancala - node.p1mancala)
    
    v = float('inf')

    for child in node.children:
        v = min(v, maxvalue(child, player))

    return v


def maxvalue(node, player):
    if len(node.children) == 0:
        if player == 1:
            return int(node.p1mancala - node.p2mancala)
        else:
            return int(node.p2mancala - node.p1mancala)
    

    v = float('-inf')

    for child in node.children:
        v = max(v, minvalue(child, player))

    return v

