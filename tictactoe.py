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
    pass
