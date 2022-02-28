INITIAL_STATE = '.........'


def successor(board, player, index):
    """
    :param board: A string
    :param player: 'X' or 'O'
    :param index: 0 through 8
    :return: The board that would result if player played at index.
    """
    return board[:index] + player + board[index+1:]


def legal_moves(board, player):
    """
    :param board: A string
    :param player: 'X' or 'O'
    :return: A sequence of legal moves (indices) for player from baord
    """
    return tuple([i for i in range(len(board)) if board[i] == '.'])


def winner(board):
    """
    :param board: A string
    :return: 1 if 'X' has won, -1 if 'O' has won, 0 otherwise
    """
    winning_lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))
    for a, b, c in winning_lines:
        if board[a] == board[b] == board[c]:
            if board[a] == 'X':
                return 1
            if board[a] == 'O':
                return -1
    return 0


def value_for_o(board):
    """
    :param board: A string
    :return: The value of board if it is O's turn.
    """
    # TODO Check that value of winner is 0 -- the game may already be over!
    moves = legal_moves(board, 'O')
    if moves:
        return min([value_for_x(successor(board, 'O', move)) for move in moves])
    return winner(board)


def value_for_x(board):
    """
    :param board: A string
    :return: The value of board if it is O's turn.
    """
    moves = legal_moves(board, 'X')
    if moves:
        return max([value_for_o(successor(board, 'X', move)) for move in moves])
    return winner(board)
