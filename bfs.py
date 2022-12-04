from main import *
from board import Board


def main():
    initial_board = create_peg_solitaire_board()
    board = Board(initial_board)
    frontier = [board]
    explored = []
    
    explored_node_count = 0
    while frontier:
        node = frontier.pop(0)
        explored.append(node)
        explored_node_count += 1
        moves = get_possible_moves(node.board)
        if not moves:
            print('No solution on this path')
            print(node.depth)
        for start, end in moves:
            child = Board(move_peg(node.board, start, end), node, node.depth + 1)
            if child in explored or child in frontier:
                continue
            # if child.state is goal, return solution
            if check_if_board_is_solved(child.board):
                print('Solution found')
                print('Explored node count: ', explored_node_count)
                print('Solution depth: ', child.depth)
                print_board(child.board)
                return
            frontier.append(child)
           

if __name__ == '__main__':      
    main()