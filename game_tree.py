
from mancala import Mancala


class Node:
    def __init__(self, past_moves, p1mancala, p2mancala, possible_moves):
        self.past_moves = past_moves
        self.children = []
        self.p1mancala = p1mancala
        self.p2mancala = p2mancala
        self.possible_moves = possible_moves

    def add_child(self, child):
        self.children.append(child)
        
      
def game_tree(past_moves = [], pits_per_player=6, stones_per_pit=4, depth=5):
    startgame = Mancala(pits_per_player, stones_per_pit)

    for move in past_moves:
        startgame.play(move[1])


    p1mancala = startgame.board[startgame.p1_mancala_index]
    p2mancala = startgame.board[startgame.p2_mancala_index]


    root_node = Node(past_moves, p1mancala, p2mancala, startgame.possible_moves())

    node_q = [(root_node, 0)]
    
    current_layer = 0

    
    while node_q:
        current_parent, current_layer  = node_q.pop(len(node_q)-1)

        if current_layer >= depth:
            continue

        for move in current_parent.possible_moves:
            currentgame = Mancala(pits_per_player, stones_per_pit)
            for past_move in current_parent.past_moves:
                currentgame.play(past_move[1])
            currentgame.play(move)
            
            p1mancala = currentgame.board[currentgame.p1_mancala_index]
            p2mancala = currentgame.board[currentgame.p2_mancala_index]
            temp_possible_moves = currentgame.possible_moves()
            terminal = currentgame.winning_eval()
            
            if terminal:
                current_node = Node(currentgame.moves, p1mancala, p2mancala, [])
                current_parent.add_child(current_node)
            
            else:
                current_node = Node(currentgame.moves, p1mancala, p2mancala, temp_possible_moves)
                current_parent.add_child(current_node)
                node_q.append((current_node, current_layer+1))

            del currentgame

    return root_node
