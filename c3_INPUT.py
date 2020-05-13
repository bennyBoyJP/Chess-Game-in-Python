def main_input(turn, origin, destination, board, printboard, space):
    """
    :param turn: WHITE or BLACK's turn
    :param origin: starting coordinate of piece in X/Y form
    :param destination: ending coordinate of piece in X/Y form
    :param board: full board current layout
    :param printboard: function from c3_BOARD to print the board
    :param space: variable from c3_BOARD of the 'space' parameter ("  ")
    :return: True if format is correct and parameters are acceptable
    """

    # print('input: start')
    xParameters, yParameters = "ABCDEFGH", '12345678'

    while True:

        if origin == '1' and destination == '1':  # <-- reset board
            return False
        elif origin == '2' and destination == '2':  # <-- manual turn switch
            return False
        elif origin == '3' and destination == '3':  # <-- print history
            return False
        elif len(origin) != 2 or len(destination) != 2:
            # printboard(board)
            print('Invalid entry - entry formatting (A1,A2)')
            return False
        elif origin[-1] not in yParameters or destination[-1] not in yParameters:
            # printboard(board)
            print('Invalid entry - outside of Y parameters')
            return False
        elif origin[0] not in xParameters or destination[0] not in xParameters:
            # printboard(board)
            print('Invalid entry - outside of X parameters')
            return False
        elif origin == destination:
            # printboard(board)
            print('Invalid entry - cannot attack oneself')
            return False
        elif board[origin] == space:
            # printboard(board)
            print('Invalid entry - no piece selected')
            return False
        elif board[origin][0] == board[destination][0]:
            # printboard(board)
            print('Invalid entry - cannot attack own side')
            return False
        elif turn == "WHITE":
            if board[origin][0] == "b":
                # printboard(board)
                print('Invalid entry - player WHITE turn')
                return False
            else:
                # print('input: valid')
                return True
        elif turn == "BLACK":
            if board[origin][0] == "w":
                # printboard(board)
                print('Invalid entry - player BLACK turn')
                return False
            else:
                # print('input: valid')
                return True
        else:
            # printboard(board)
            print('input error')
            return False
