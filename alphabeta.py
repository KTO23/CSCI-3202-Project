from mancala import Mancala
from game_tree import *


def alphabeta(mancala, depth, player):
    past_moves = mancala.moves
    this_game_tree = game_tree(past_moves, int(mancala.get_pits_per_player()), int(mancala.get_stones_per_pit()), depth)

    alpha = float('-inf')
    beta = float('inf')

    maxval = float('-inf')
    bestmove = None

    
    if player == 1:
        this_game_tree.children.sort(key=lambda child: child.p1mancala - child.p2mancala, reverse=True)
    else:
        this_game_tree.children.sort(key=lambda child: child.p2mancala - child.p1mancala, reverse=True)
    

    for child in this_game_tree.children:
        childval = minvalue(child, player, alpha, beta)
        if childval > maxval:
            maxval = childval
            bestmove = child.past_moves[-1]


    return bestmove[1]
    

def minvalue(node, player, alpha, beta):
    if player == 1:
        if len(node.children) == 0:
            return int(node.p1mancala - node.p2mancala)
        else:
            node.children.sort(key=lambda child: child.p1mancala - child.p2mancala)
    else:
        if len(node.children) == 0:
            return int(node.p2mancala - node.p1mancala)
        else:
            node.children.sort(key=lambda child: child.p2mancala - child.p1mancala)
    
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
    if player == 1:
        if len(node.children) == 0:
            return int(node.p1mancala - node.p2mancala)
        else:
            node.children.sort(key=lambda child: child.p1mancala - child.p2mancala, reverse=True)
    else:
        if len(node.children) == 0:
            return int(node.p2mancala - node.p1mancala)
        else:
            node.children.sort(key=lambda child: child.p2mancala - child.p1mancala, reverse=True)

    val = float('-inf')


    for child in node.children:
        childval = minvalue(child, player, alpha, beta)
        if childval > val:
            val = childval
        
        if val >= beta:
            return val
        
        alpha = max(val, alpha)

    return val